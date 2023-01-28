# a function that takes a list and target parameter
# multiple variables : middle, start, end, steps
# recursion or while loop 
# increase the steps each time a split is made
# conditions to track target positon


def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("Step", steps, ":" , list[start:end]) 