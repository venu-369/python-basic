#collect email from user
# slice email using the @, the first part as the username and the second part as the domain
#s plit the domain using the .  


def main():
    email = input("What is your email address?: ").strip()
    username = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    print("Your username is {} and your domain is {}".format(username, domain))