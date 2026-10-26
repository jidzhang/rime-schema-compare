'use strict';

// Mine word bigrams from a plain-text corpus, using our own dictionary for
// segmentation (no jieba at build time, no runtime dependency).
//
// The engine's offline decoder scores a reading by summing per-word unigram
// scores, so it has no way to prefer 我想请你吃 over 我详情你吃: every word is
// scored in isolation. Classic Google Pinyin ships a bigram language model
// for exactly this, and so must we. This script produces the pair counts that
// pinyin-engine/tools/build-dict.js --lm turns into the runtime table.
//
// Usage:
//   node build_bigram_from_text.js <corpus.txt[.gz]> <entries.json> <out.txt>
//        [--t2s TSCharacters.txt] [--minfreq 100] [--mincount 2] [--topk 20]
//        [--recount unigrams.txt] [--trigram out.txt] [--trigramHead 30]
//
// Recount mode (--recount): instead of bigrams, emit word occurrence counts
// (word\tcount, descending) from the same Viterbi segmentation. This is how
// entry frequencies are re-estimated on real text without jieba: the
// converter's applyRecount replaces base-dict frequencies with these counts
// (white-frost 745M-corpus renormalization route, with our own segmenter).
// Single characters are counted too; the converter only applies the counts
// to multi-char rows (singles stay governed by the classic curated dict).
//
// Corpus: OPUS OpenSubtitles zh_cn mono (conversational; ~10% of its lines
// still use traditional characters). --t2s converts them with the OpenCC
// character table:
//   curl -sL -o TSCharacters.txt \
//     https://raw.githubusercontent.com/BYVoid/OpenCC/master/data/dictionary/TSCharacters.txt
//
// Output format matches tools/predict/build_predict.js so the same
// parseBigramText() reader can consume it:
//   n\t<word>\t<next>:<count> <next>:<count> ...

const fs = require('fs');
const zlib = require('zlib');
const readline = require('readline');
const { PassThrough } = require('stream');

const MAX_WORD_LEN = 4;

function parseArgs(argv) {
  const opts = {
    minfreq: 100, mincount: 2, topk: 20, maxlen: MAX_WORD_LEN,
    trigramHead: 30,
  };
  const pos = [];
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--t2s') opts.t2s = argv[++i];
    else if (a === '--minfreq') opts.minfreq = parseInt(argv[++i], 10);
    else if (a === '--mincount') opts.mincount = parseInt(argv[++i], 10);
    else if (a === '--topk') opts.topk = parseInt(argv[++i], 10);
    else if (a === '--maxlen') opts.maxlen = parseInt(argv[++i], 10);
    else if (a === '--recount') opts.recount = argv[++i];
    else if (a === '--recount-start') opts.recountStart = argv[++i];
    else if (a === '--trigram') opts.trigram = argv[++i];
    else if (a === '--trigramHead') opts.trigramHead = parseInt(argv[++i], 10);
    else if (a === '--presegmented') opts.presegmented = true;
    else pos.push(a);
  }
  opts.src = pos[0];
  opts.entries = pos[1];
  opts.out = pos[2];
  return opts;
}

// OpenCC TSCharacters.txt: "<traditional>\t<simplified> ..." per line. Only
// the first candidate is used, which is what a zh-cn conversion needs.
function loadT2S(path) {
  const map = new Map();
  if (!path) return map;
  for (const line of fs.readFileSync(path, 'utf8').split('\n')) {
    if (!line || line[0] === '#') continue;
    const parts = line.split('\t');
    if (parts.length < 2) continue;
    const simplified = parts[1].trim().split(/\s+/)[0];
    if (simplified) map.set(parts[0], simplified);
  }
  return map;
}

function isCJK(code) {
  return (code >= 0x4e00 && code <= 0x9fff) ||
    (code >= 0x3400 && code <= 0x4dbf) ||
    (code >= 0xf900 && code <= 0xfaff);
}

function main() {
  const opts = parseArgs(process.argv.slice(2));
  if (!opts.src || !opts.entries || !opts.out) {
    console.error('usage: node build_bigram_from_text.js <corpus.txt[.gz]> ' +
      '<entries.json> <out.txt> [--t2s TSCharacters.txt] [--minfreq N] ' +
      '[--mincount N] [--topk N]');
    process.exit(1);
  }
  const t2s = loadT2S(opts.t2s);
  // Vocabulary: dictionary words above the frequency floor. Rare words never
  // disambiguate anything, and dropping them keeps the pair table (and the
  // runtime dictionary) small.
  const freq = new Map();
  for (const e of JSON.parse(fs.readFileSync(opts.entries, 'utf8'))) {
    const prev = freq.get(e.w);
    if (prev === undefined || e.f > prev) freq.set(e.w, e.f);
  }
  const vocab = new Map();
  for (const [w, f] of freq) {
    if (f >= opts.minfreq && Array.from(w).length <= opts.maxlen) vocab.set(w, f);
  }
  // Words indexed by first character, longest first, so the DP below only
  // ever looks at a handful of candidates per position.
  const byFirst = new Map();
  for (const w of vocab.keys()) {
    const c = w[0];
    if (!byFirst.has(c)) byFirst.set(c, []);
    byFirst.get(c).push(w);
  }
  for (const list of byFirst.values()) {
    list.sort((a, b) => b.length - a.length || vocab.get(b) - vocab.get(a));
  }
  // Unigram log-probability: log(freq / total). Normalising by the corpus
  // total matters: without it the DP compares a word's log-frequency against
  // the *sum* of its characters' log-frequencies and therefore always prefers
  // single characters, which is how the first run produced a 4k-word token
  // stream out of a 35k-word vocabulary.
  let total = 0;
  for (const f of freq.values()) total += f;
  const logTotal = Math.log(total);
  const logFreq = (w) => Math.log(vocab.get(w)) - logTotal;

  // Per-word cost, mirroring the runtime decoder's WORD_PENALTY (500 on
  // the -800*ln scale = 0.625 nats). Without it the counter systematically
  // undercounts mid-frequency words: bare log-frequency sums always prefer
  // two singles over one word (考研 2095 -> 6), while the runtime decoder
  // penalises the extra word and decodes the unit. Counting must segment
  // the way the decoder reads, or the recount fights the runtime.
  const WORD_COST = 0.625;
  // Viterbi segmentation of one CJK run, maximising the sum of log
  // frequencies minus the per-word cost. An unknown character scores as a
  // rare single character and is kept, so bigrams across it are still
  // counted.
  const best = [];
  const from = [];
  const seg = (chars) => {
    const n = chars.length;
    // Both arrays are reused across lines, so every slot the DP can read has
    // to be cleared: a stale score from a longer previous line silently
    // blocked updates and produced garbage segmentations.
    best.length = n + 1;
    from.length = n + 1;
    best.fill(undefined);
    from.fill(-1);
    best[0] = 0;
    for (let i = 0; i < n; i++) {
      if (best[i] === undefined) continue;
      const cands = byFirst.get(chars[i]) || [];
      let advanced = false;
      for (const w of cands) {
        const L = w.length;
        if (i + L > n) continue;
        if (chars.substr(i, L) !== w) continue;
        const score = best[i] + logFreq(w) - WORD_COST;
        if (best[i + L] === undefined || score > best[i + L]) {
          best[i + L] = score;
          from[i + L] = i;
        }
        advanced = true;
      }
      if (!advanced || best[i + 1] === undefined) {
        const score = best[i] + Math.log(0.5) - logTotal - WORD_COST;
        if (best[i + 1] === undefined || score > best[i + 1]) {
          best[i + 1] = score;
          from[i + 1] = i;
        }
      }
    }
    const out = [];
    let i = n;
    while (i > 0) {
      const j = from[i];
      if (j < 0) break;
      out.push(chars.slice(j, i));
      i = j;
    }
    return out.reverse();
  };

  const pair = new Map();
  const uni = new Map();
  // Trigram counts, numeric keys (idx1*1e10 + idx2*1e6 + idx3; idx < 1e6 so
  // the product stays under 2^53). Only pairs whose RUNNING bigram count has
  // reached --trigramHead contribute, which keeps the table to heads that
  // actually carry context and bounds memory on the 25M-token wiki corpus.
  const wordIdx = new Map();
  for (const w of vocab.keys()) wordIdx.set(w, wordIdx.size);
  // Two-level map: key12 = idx1 * 1e6 + idx2 (idx < 1e6, exact in a double),
  // inner idx3 -> count. A single packed idx1*1e12+... would overflow 2^53,
  // and idx1*1e10 + idx2*1e6 aliases whenever idx2 >= 1e4 (vocab is 300k+).
  const tri = new Map();
  const triHead = opts.trigramHead;
  // Sentence-start words: first token of every CJK run. Typing distribution
  // at position 0 differs wildly from overall (吧 almost never starts a
  // sentence, 把 often does); the decoder has no left context there, so a
  // dedicated start table beats any global unigram.
  const starters = new Map();
  let lines = 0;
  let tokens = 0;
  const consume = (line) => {
    lines++;
    let text = line;
    if (t2s.size) {
      let conv = '';
      for (const ch of text) conv += t2s.get(ch) || ch;
      text = conv;
    }
    if (opts.presegmented) {
      // Gold-segmented corpus (words separated by whitespace, e.g. SIGHAN
      // PKU People's Daily): tokens are words as-is, no Viterbi. This is a
      // third segmentation signal source for union mining (see report
      // section 10: the 'dirty' jieba segmentation was load-bearing).
      const words = text.split(/\s+/).filter((w) => w && vocab.has(w));
      if (words.length < 2) { lines++; return; }
      for (const w of words) uni.set(w, (uni.get(w) || 0) + 1);
      if (vocab.has(words[0])) {
        starters.set(words[0], (starters.get(words[0]) || 0) + 1);
      }
      for (let i = 0; i + 1 < words.length; i++) {
        const w1 = words[i];
        const w2 = words[i + 1];
        if (!vocab.has(w1) || !vocab.has(w2)) continue;
        const key = w1 + '\u0001' + w2;
        pair.set(key, (pair.get(key) || 0) + 1);
        tokens++;
        if (opts.trigram && i + 2 < words.length) {
          const c12 = pair.get(key) || 1;
          if (c12 >= triHead && vocab.has(words[i + 2])) {
            const key12 = wordIdx.get(w1) * 1e6 + wordIdx.get(w2);
            let inner = tri.get(key12);
            if (!inner) { inner = new Map(); tri.set(key12, inner); }
            const i3 = wordIdx.get(words[i + 2]);
            inner.set(i3, (inner.get(i3) || 0) + 1);
          }
        }
      }
      lines++;
      return;
    }
    // Split into CJK runs; punctuation and latin end a run so pairs never
    // span them.
    let run = '';
    const runs = [];
    for (const ch of text) {
      if (isCJK(ch.codePointAt(0))) run += ch;
      else if (run) { runs.push(run); run = ''; }
    }
    if (run) runs.push(run);
    for (const r of runs) {
      if (r.length < 2) continue;
      const words = seg(r);
      for (const w of words) {
        if (vocab.has(w)) uni.set(w, (uni.get(w) || 0) + 1);
      }
      if (words.length && vocab.has(words[0])) {
        starters.set(words[0], (starters.get(words[0]) || 0) + 1);
      }
      for (let i = 0; i + 1 < words.length; i++) {
        const w1 = words[i];
        const w2 = words[i + 1];
        if (!vocab.has(w1) || !vocab.has(w2)) continue;
        const key = w1 + '\u0001' + w2;
        const c12 = (pair.get(key) || 0) + 1;
        pair.set(key, c12);
        tokens++;
        if (opts.trigram && i + 2 < words.length && c12 >= triHead) {
          const w3 = words[i + 2];
          if (vocab.has(w3)) {
            const key12 = wordIdx.get(w1) * 1e6 + wordIdx.get(w2);
            let inner = tri.get(key12);
            if (!inner) { inner = new Map(); tri.set(key12, inner); }
            const i3 = wordIdx.get(w3);
            inner.set(i3, (inner.get(i3) || 0) + 1);
          }
        }
      }
    }
  };

  const src = fs.createReadStream(opts.src);
  const gunzip = opts.src.endsWith('.gz') ? zlib.createGunzip() : new PassThrough();
  src.pipe(gunzip);
  // A truncated .gz still yields usable data; stop at the first error instead
  // of throwing so partial corpora can be mined.
  gunzip.on('error', () => src.unpipe(gunzip));
  const rl = readline.createInterface({ input: gunzip, crlfDelay: Infinity });
  rl.on('line', consume);
  rl.on('close', () => {
    if (opts.recount) {
      const rows = Array.from(uni.entries())
        .sort((a, b) => b[1] - a[1] || (a[0] < b[0] ? -1 : 1));
      fs.writeFileSync(opts.recount,
        rows.map(([w, c]) => w + '\t' + c).join('\n') + '\n');
    }
    if (opts.trigram) {
      const idxWord = new Array(wordIdx.size);
      for (const [w, i] of wordIdx) idxWord[i] = w;
      const lines = [];
      for (const [key12, inner] of tri) {
        const i1 = Math.floor(key12 / 1e6);
        const i2 = key12 - i1 * 1e6;
        for (const [i3, c] of inner) {
          lines.push('t\t' + idxWord[i1] + '\t' + idxWord[i2] + '\t' +
            idxWord[i3] + '\t' + c);
        }
      }
      let triples = 0;
      for (const inner of tri.values()) triples += inner.size;
      fs.writeFileSync(opts.trigram, lines.join('\n') + '\n');
      console.log('trigram triples: ' + triples + ' (heads>=' + triHead + ')');
    }
    if (opts.recountStart) {
      const rows = Array.from(starters.entries())
        .sort((a, b) => b[1] - a[1] || (a[0] < b[0] ? -1 : 1));
      fs.writeFileSync(opts.recountStart,
        rows.map(([w, c]) => w + '\t' + c).join('\n') + '\n');
    }
    // Group by head word, keep the strongest continuations.
    const heads = new Map();
    for (const [key, c] of pair) {
      if (c < opts.mincount) continue;
      const tab = key.indexOf('\u0001');
      const w1 = key.slice(0, tab);
      const w2 = key.slice(tab + 1);
      if (!heads.has(w1)) heads.set(w1, []);
      heads.get(w1).push([w2, c]);
    }
    const out = ['{"v":1}'];
    let written = 0;
    for (const [w1, list] of heads) {
      list.sort((a, b) => b[1] - a[1]);
      const top = list.slice(0, opts.topk);
      out.push('n\t' + w1 + '\t' + top.map((x) => x[0] + ':' + x[1]).join(' '));
      written += top.length;
    }
    fs.writeFileSync(opts.out, out.join('\n') + '\n');
    console.log(JSON.stringify({
      lines,
      vocab: vocab.size,
      unitokens: uni.size,
      tokens,
      distinctPairs: pair.size,
      heads: heads.size,
      pairs: written,
    }));
  });
}

if (require.main === module) main();
