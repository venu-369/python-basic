# have a python dictionary that has a key value pair that represents a word and its definition
# collect input from the user, input is a word
# check if the word is in the dictionary 
# print the definition
from PyDictionary import PyDictionary

def main():
    word_dictionary = {
        'hi': 'a way of greeting',
        'bye': 'a way of saying goodbye',
        'earth': 'a planet in space',
        'eyes': 'organ for seeing'
    }

    while True:

        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

main()