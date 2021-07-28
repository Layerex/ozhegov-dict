#!/usr/bin/env python3

import csv
import re
from sys import argv, stdout


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
    with open(argv[1]) as f:
        with stdout as out:
            reader = csv.reader(f, delimiter="|")

            for row in list(reader)[1:]:
                out.write(f":{row[0].strip()}:")
                for col in row[2:]:
                    if col and col != "+":
                        col = re.sub(
                            "(N([0-9]+\/?)*)",
                            lambda match: convert_n_notation(match.group(1)),
                            col,
                        )
                        # TODO:
                        # col.replace("Spec", "(спец.)")
                        # col.replace("Pejor", "(неодобр.)")
                        # col.replace("Colloc", "(разг.)")
                        # col.replace("Lib", "(книжн.)")
                        # col.replace("Non-st", "(прост.)")
                        # col.replace("Regio", "(обл.)")
                        cols.append(col)
                out.write(" ".join(cols) + "\n")


if __name__ == "__main__":
    main()
