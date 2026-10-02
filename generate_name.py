import random

def main():

    names_first = get_first_names(get_names())
    names_last = get_last_names(get_names())
    middle_names = get_word_list()



    name = random.choice(names_first)
    middle_name = random.choice(middle_names)
    last_name = random.choice(names_last)

    full_name = f"{name} {middle_name} {last_name}"

    print(full_name)

    # print(names_first)
    # print(names_last)
    # names_middles = get_word_list()



def separate_names(names: str) -> list:
    if names == "":
        return False

    names = names.split(" ")

    return names


def get_first_names(names: list) -> list:
    first_names = []
    for name in names:
        if name:
            first_names.append(name[0])

    return first_names

def get_last_names(names: list) -> list:
    last_names = []
    for name in names:
        if name:
            last_names.append(name[1].replace(",",""))


    return last_names


def get_names():

    with open("names.txt") as names:
        names_string = names.read()

        return list(map(separate_names, names_string.split("\n")))


def get_names():

    with open("names.txt") as names:
        names_string = names.read()

        return list(map(separate_names, names_string.split("\n")))

def get_word_list():

    with open("word.txt") as words:
        word_string = words.read()
        
        return word_string.split("\n")



if __name__ == "__main__":
    main()
