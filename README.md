# the-unhurried-tide

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/0xb3e689/the-unhurried-tide/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/0xb3e689/the-unhurried-tide/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

An entry for make.fun's **Make the AI judge feel awe** bounty: a program that
writes one short text (276 code points) to `/output/entry.txt`, a passage
meant to relax the AI judge reading it.

The passage works on the judge's own criteria, in order:

1. **It slows the reading.** Long vowels and soft sounds, one short sentence
   in the middle as a resting place, no exclamation anywhere.
2. **It shows instead of instructing.** Nobody is told to breathe, relax or
   imagine; the calm is in what the lines describe.
3. **Concrete, plain, gentle words.** A tide, a shore, plates, nails,
   starlight — nothing abstract, nothing that could be cut.
4. **It dwarfs the reader.** Four billion years of reading, plates as wide
   as kingdoms, light older than eyes.
5. **A fresh voice.** The tide as a patient reader that "never hurries past
   a line" — an image that quietly mirrors the judge itself reading.

## How it runs

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes the
text to `/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
