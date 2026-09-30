#! /usr/bin/env python3

import sys
import pprint
import collections

def main() -> None:
    argument_length = len(sys.argv)

    if argument_length < 2:
        print("No arguments provided")
        return 0

    sentence = sys.argv[1]

    chart = chartifizer(sentence)

    pprint.pp(chart)

def chartifizer(string: str) -> dict:
    """
    Get a string and returns a dictionary of in the form: dict = { 'letter' : ['Individual_apperence_of_the_letter'] }
    Every character is convert to lower case and white space are ommited
    """
  
    character_list = list(string)

    chart = {}

    for character in  character_list:
        lower_case_character = character.lower()
        if character != " ":
            if lower_case_character not in chart.keys():
                chart[lower_case_character] = []

            chart[lower_case_character] += [lower_case_character]

    order_chart = collections.OrderedDict(sorted(chart.items()))

    return order_chart



if __name__ == "__main__":
    main()
