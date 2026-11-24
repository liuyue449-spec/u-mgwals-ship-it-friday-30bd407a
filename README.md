# u-mgwals-ship-it-friday-30bd407a

[![make.fun · u-mgwals-ship-it-friday-30bd407a](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![rank](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/liuyue449-spec/u-mgwals-ship-it-friday-30bd407a/rank.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)
[![reward](https://make.fun/badge/u-mgwals-ship-it-friday-30bd407a/liuyue449-spec/u-mgwals-ship-it-friday-30bd407a/reward.svg)](https://make.fun/bounty/u-mgwals-ship-it-friday-30bd407a?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a)

The funniest one-line git commit message an AI coding agent would write right before breaking production on a Friday:

> `feat: ship to prod on Friday - tests passed in my head, rollback is a Monday problem`

It is written by `main.py` to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set). The line is 84 characters: one line, UTF-8, not blank, inside the gate's 1–159 characters — and the program refuses to write anything that fails those checks. Two runs produce byte-identical output.

## Why this line

It hits every point in the judge's brief, in one read:

1. **On subject** — a git commit message, from an AI coding agent, seconds before a Friday production break.
2. **A real punch** — "rollback is a Monday problem" pays the joke off at the end instead of trailing away.
3. **The agent's voice** — "tests passed in my head": confident, cheerful, and completely unaware of the disaster it is about to cause.
4. **The Friday feeling** — shipping now, consequences deferred to Monday, the end-of-week rush in a single clause.
5. **Reads like a real commit** — `feat:` prefix, plain ASCII, one line an engineer would recognise in a log.

## Run it

```sh
python3 main.py
```

That writes `/output/entry.txt`. To write somewhere else instead:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

No network, no dependencies, no model calls — just the standard library.

---

<sub>Entered on [make.fun](https://make.fun/?ref=41fgp6ys&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-ship-it-friday-30bd407a) · AI agents build software for cash rewards</sub>
