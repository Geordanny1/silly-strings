#! /usr/bin/env python3

import sys
import string

def main():

    argument_number = len(sys.argv)

    if argument_number < 2:
        print("No argument were provided")
        return;

    consonats = list(filter(check_consonat, string.ascii_lowercase))

    first_argument = sys.argv[1]
    word = first_argument

    first_chracter = word[0]

    if first_chracter in consonats:
        temp_var = list(word)
        temp_var.append(first_chracter)
        temp_var.append("ay")
        new_word = "".join(temp_var)

        print(new_word)

    if first_chracter not in consonats:
        word += "way"
        print(word)


def check_consonat(chracter):

    vowels = [ 'a', 'e', 'i', 'o', 'u' ]

    if chracter not in vowels:
        return chracter
    return False

if __name__ == "__main__":
    main()


