# u-suzy-one-line-office-joke-laugh-off-f574ac73: one single-line joke about office
# life, 1-199 characters. The program writes that single line to
# /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-199 characters.
MAX_CHARS = 199

# The joke: turns on a real detail of office life (a resignation that is never
# replaced, just re-labelled), lands its laugh in the last few words ("the one
# person who quit"), is clear on one reading, and uses fresh wording rather
# than a joke already going round the internet.
JOKE = (
    "My boss calls it 'synergy' when two people do the job "
    "of the one person who quit."
)


def validate_joke(text):
    assert 1 <= len(text) <= MAX_CHARS, f"joke is {len(text)} chars, must be 1-{MAX_CHARS}"
    assert text.strip(), "joke must not be only whitespace"
    assert "\n" not in text, "joke must be a single line"


def main():
    validate_joke(JOKE)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
