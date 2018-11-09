#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv


TABU_CHARS = ["-", "k", "w", "y"]
SUBST_CHARS = {
    "á": "a",
    "à": "a",
    "â": "a",
    "ã": "a",
    "é": "e",
    "ê": "e",
    "í": "i",
    "î": "i",
    "ó": "o",
    "ô": "o",
    "õ": "o",
    "ú": "u",
    "ü": "u"
}


def main():
    with open(argv[1], "r", encoding="ISO-8859-1") as arq_in:
        with open(argv[2], "w") as arq_out:
            words = set()

            for line in arq_in:
                line = line.strip()

                if not 2 <= len(line) <= 15 or line[0].isupper():
                    continue

                for tabu in TABU_CHARS:
                    if tabu in line:
                        line = ""
                if not line:
                    continue

                for old, new in SUBST_CHARS.items():
                    if old in line:
                        line = line.replace(old, new)

                if line not in words:
                    words.add(line)
                    arq_out.write(line)
                    arq_out.write("\n")


if __name__ == "__main__":
    main()
