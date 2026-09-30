#! /usr/bin/env python3

import sys, pprint

def main():
    argument_length = len(sys.argv)

    if argument_length < 2:
        print("No arguments provided")
        return 0

    sentence = sys.argv[1]

    chart = chartifizer(sentence)

    pprint.pp(chart)

def chartifizer(string: str) -> dict:
  
    character_list = list(string)

    chart = {}

    for character in  character_list:
        if character != " ":
            if character not in chart.keys():
                chart[character] = []

            chart[character] += [character]

    return chart



if __name__ == "__main__":
    main()
