#!/bin/python

import pandas as pd
import matplotlib.pyplot as plt
import sys

colors = ("#7C5869", "#886176", "#9A7197", "#9D96B8", "#AFD2E9")


def main():
    char_dict = {}
    for line in sys.stdin:
        filepath = line.rstrip()
        f = open(filepath, "r")
        for char in f.read():
            if char.isascii():
                if char.isspace():
                    continue
                # if char.isspace() or char.isalnum():
                #     continue
                c = char.lower()
                if c not in char_dict:
                    char_dict[c] = 0
                char_dict[c] += 1
    sorted_dict = {k: v for k, v in sorted(
        char_dict.items(), key=lambda item: item[1], reverse=True)}

    argv = sys.argv
    name = "data"
    if len(argv) > 1:
        name = str(argv[1])

    df = pd.DataFrame.from_records([sorted_dict])
    df.to_csv(name + ".csv", index=False, header=True)


if __name__ == "__main__":
    main()
