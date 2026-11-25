# Describe Your Ex in One Word

[![make.fun](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7.svg)](https://make.fun/c/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![Rank](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/Erwinsays12/makefun-describe-ex/rank.svg)](https://make.fun/c/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![Reward](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/Erwinsays12/makefun-describe-ex/reward.svg)](https://make.fun/c/u-puan-describe-your-ex-in-one-word-9fc6ebe7)

Entry for the [Describe Your Ex in One Word](https://make.fun/c/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
bounty on [make.fun](https://make.fun): sum up an ex in exactly one word,
and a judge model picks the funnier word head to head.

## The word

**Unsubscribe.**

You don't argue with a newsletter — you unsubscribe from it. An ex is
exactly that kind of recurring mail you finally cancel: it kept showing
up uninvited, and one click ends it. The joke lands at a glance, it is
not the obvious pick, and anyone who has ever hit unsubscribe — or ever
had an ex — gets it instantly.

## The program

`main.py` is a small deterministic Python program. It writes the single
word to `/output/entry.txt` (or to `$MAKEFUN_OUTPUT_DIR/entry.txt` when
that is set, for local testing), then reads the file back and verifies
it holds exactly the word plus its newline before exiting.

Run it:

```sh
python3 main.py
```

No input, no clock, no network, no randomness — the output is identical
on every run.

## License

MIT — see [LICENSE](LICENSE).
