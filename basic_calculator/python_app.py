#define the functions needed: add, sub, mul, div
#print options to the user
#ask for values
#call the functions
#while loop to continue the program untill the user wants to exit


def add(a, b):
    answer = a + b
    print(str(a) + '+' + str(b) + '=' + str(answer) + '\n')
    
def sub(a, b):
    answer = a - b
    print(str(a) + '-' + str(b) + '=' + str(answer) + '\n')

def mul(a, b):
    answer = a * b
    print(str(a) + '*' + str(b) + '=' + str(answer) + '\n')

def div(a, b):
    answer = a / b
    print(str(a) + '/' + str(b) + '=' + str(answer) + '\n')

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice =  input("Enter your choice: ")

    if choice == "a" or choice == "A":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        mul(a, b)
    elif choice == "d" or choice == "D":        
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Bye")
        quit()