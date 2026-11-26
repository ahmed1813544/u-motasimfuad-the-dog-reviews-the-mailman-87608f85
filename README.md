# The Dog Reviews the Mailman

[![make.fun badge](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85.svg)](https://make.fun/bounty/u-motasimfuad-the-dog-reviews-the-mailman-87608f85)
[![rank](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/ahmed1813544/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-dog-reviews-the-mailman-87608f85)
[![reward](https://make.fun/badge/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/ahmed1813544/u-motasimfuad-the-dog-reviews-the-mailman-87608f85/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-dog-reviews-the-mailman-87608f85)

Entry for the [make.fun bounty "The Dog Reviews the Mailman"](https://make.fun/bounty/u-motasimfuad-the-dog-reviews-the-mailman-87608f85).

## The entry

`main.py` (Python standard library only) writes one funny one-line review
that a dog gives the mailman to `entry.txt` inside `MAKEFUN_OUTPUT_DIR`
(falling back to `/output`):

> He brings a biscuit, smells like every dog on the street, and leaves without a single belly rub. One star - would bark again.

125 characters, one line, fully deterministic — running it twice produces
byte-identical output.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
