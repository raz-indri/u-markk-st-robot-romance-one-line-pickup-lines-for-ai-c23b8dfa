"""Robot Romance: one-line pickup line for an AI.

Writes exactly one pickup line to /output/entry.txt.
"""

import os

LINE = "I asked the model to write me a pickup line, and it just printed your username 400 times."
# Duel-tested winner (7/7 pairwise wins): meta humour about the model
# itself, one concrete absurd detail (username printed 400 times), no
# worn battery/charging/reboot moves, 89 chars, well under the 200 cap.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
