# Ask the user if they want to generate a password or not
# if yes, ask for the length of the password
# generate a password with the length of the password
# print password
# if initial response is no, exit immediately


import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()" + string.punctuation)


def generate_password():
    password_length = int(input("How long do you want your password to be? "))

    random.shuffle(characters)

    password = []

    for i in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)


    password = """.join(password)