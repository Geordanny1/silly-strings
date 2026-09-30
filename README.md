# silly strings

This is a simply colection of small silly scripts to interact with strings

### usage

*pylatin*
```sh
./pylating.py <string>
```
if the first character of the string begins with a consonant. Moves the consonart to the end and then add "ay" prints it to terminal.
In case it does not beings with a consonart it adds way to the end of and then print the string to the terminal. 

Examples
```sh
./pylatin.py hello   # hellohay
./pylatin.py banana  # bananabay
./pylatin.py away    # awayway
```

*string bar chart*
```sh
./string_bar_chart.py <string>
```
Take the string and prints dictionary with the character and each independant apperence of it. 
Example:
```sh
./string_bar_chart.py "I like to eat chesse"

# Output:
# OrderedDict([('a', ['a']),
#              ('c', ['c']),
#              ('e', ['e', 'e', 'e', 'e']),
#              ('h', ['h']),
#              ('i', ['i', 'i']),
#              ('k', ['k']),
#              ('l', ['l']),
#              ('o', ['o']),
#              ('s', ['s', 's']),
#              ('t', ['t', 't'])])
# 
```

*compare sentence*
Takes two string and compares the first one the second printing if it larger, shorter or equal.
```sh
./compare_sentece.py <string> <string>
```

Example:
```sh
./compare_sentece.py "You are so foo" "I feel like I am bar"

# Output:
# The first sentence is shorter
# 'You are so foo' has {'a': [1], 'e': [1], 'f': [1], 'o': [4], 'r': [1], 's': [1], 'u': [1], 'y': [1]}
# 'I feel like I am bar' has {'a': [1], 'e': [1], 'f': [1], 'o': [4], 'r': [1], 's': [1], 'u': [1], 'y': [1]}
```

Personal solutions for the book Impractical Python Projects.
