#collect email from user
# slice email using the @, the first part as the username and the second part as the domain
#s plit the domain using the .  


def main():
    print("Welcome to the meail slicer")
    print("")

    email_input = input("inpu your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

