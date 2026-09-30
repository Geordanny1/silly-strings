#! /usr/bin/env python3

from string_bar_chart import chartifizer
import pprint
import sys

def main():

    argument_length = len(sys.argv)

    if argument_length < 3:
        print("not enought arguments")
        return 0

    sentence_first  = sys.argv[1]
    sentence_second = sys.argv[2]

    chart_first = chartifizer(sentence_first)
    chart_second = chartifizer(sentence_second)

    fc_character_number = len(chart_first.keys())
    sc_character_number = len(chart_first.keys())

    fc_string_length = len(sentence_first)
    sc_string_length = len(sentence_second)

    fc_character_letter_apperence = {}
    sc_character_letter_apperence = {}

    for key, value in chart_first.items():
        fc_character_letter_apperence[key] = [len(value)]

    for key,value in chart_second.items():
        sc_character_letter_apperence[key] = [len(value)]

    if fc_string_length == sc_string_length:
        print("Each sentence has the same lenght")

    elif fc_string_length > sc_string_length:
        print(f"The first sentence is larger")
    else:
        print(f"The first sentence is shorter")

    print(f"'{sentence_first}' has {fc_character_letter_apperence}")
    print(f"'{sentence_second}' has {fc_character_letter_apperence}")

if __name__ == "__main__" :
    main()

