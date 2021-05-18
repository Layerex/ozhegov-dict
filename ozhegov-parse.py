#!/usr/bin/env python3

import re
import csv
from sys import stdout


def main():
    with open("ozhegov.txt") as f:
        with stdout as out:
            reader = csv.reader(f, delimiter="|")

            for row in list(reader)[1:]:
                out.write(f":{row[0].strip()}:")
                for col in row[2:]:
                    if col and col != "+":
                        re.sub("\ ?N[0-9][0-9]?\/?[0-9][0-9]?", "", col)
                        # TODO:
                        # col.replace("Spec", "(спец.)")
                        # col.replace("Pejor", "(неодобр.)")
                        # col.replace("Colloc", "(разг.)")
                        # col.replace("Lib", "(книжн.)")
                        # col.replace("Non-st", "(прост.)")
                        # col.replace("Regio", "(обл.)")
                        out.write(col.strip() + " ")
                out.write("\n")


if __name__ == "__main__":
    main()
