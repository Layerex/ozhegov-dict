#!/usr/bin/env python3

import csv
import re
from sys import argv, stdout

abbreviations = {
    "Admin": "офиц.",
    "Anti": "противоп.",
    "Arch": "стар.",
    "Colloq": "разг.",
    "Deprec": "презр.",
    "Indic": "указ.",
    "Iron": "ирон.",
    "Jest": "шутл.",
    "Lib": "книжн.",
    "Maxime": "преимущ.",
    "Non-st": "прост.",
    "Obs": "устар.",
    "Ordin": "числ.",
    "Pejor": "неодобр.",
    "Poet": "поэт.",
    "Primo": "первонач.",
    "Regio": "обл.",
    "Spec": "спец.",
}


def convert_n_notation(string: str) -> str:
    """
    Конвертирование ссылок на другие значения слова в словаре в удобоваримый формат.
    N2 => (во 2 знач.)
    N1/3 => (в 1 и 3 знач.)
    N1/2/4 => (в 1, 2 и 4 знач.)
    """
    if len(string) > 1:
        numbers = tuple(map(int, string[1:].split("/")))
        prefix = "во" if numbers[0] == 2 else "в"
        number_string = (
            str(numbers[0])
            if len(numbers) == 1
            else " и ".join((", ".join(map(str, numbers[:-1])), str(numbers[-1])))
        )
        return "".join(("(", " ".join((prefix, number_string, "знач.")), ")"))
    else:
        return string


def main():
    slob_format = len(argv) in (3, 4)
    if slob_format:
        import slob

    entries = []

    with open(argv[1]) as f:
        reader = csv.reader(f, delimiter="|")

        for row in list(reader)[1:]:
            word = row[0].strip()

            cols = []
            for col in row[2:]:
                if col and col != "+":
                    col = re.sub(
                        "(N([0-9]+\/?)*)",
                        lambda match: convert_n_notation(match.group(1)),
                        col,
                    )
                    for k, v in abbreviations.items():
                        col = col.replace(k, v)
                    cols.append(col.strip())
            definition = " ".join(cols) + "\n"
            entries.append((word, definition))

        if slob_format:
            with slob.create(argv[2]) as s:
                if len(argv) == 4:
                    s.tag("label", argv[3])
                for word, definition in entries:
                    s.add(definition.encode("utf-8"), word, content_type="text/plain; charset=utf-8")
        else:  # jargon file
            for word, definition in entries:
                print(f":{word}:{definition}")


if __name__ == "__main__":
    main()
