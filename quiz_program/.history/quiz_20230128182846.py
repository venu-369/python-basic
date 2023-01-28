# a dictionary that stores questions and answers
# have  a vraibale that tracks the score of the palyer
# loop through the dictionary using the key value pairs
# display each question to the user and allow them to snwer
# tell them if they are correct or not
# show the final results when quiz is completed

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",  
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question4": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Greece?",
        "answer": "Athens"
    },
    "question7": {
        "question": "What is the capital of Poland?",
        "answer": "Warsaw"
    }
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("Answer: ")
    
    if answer.lower() == value["answer"].lower():
        print("Correct!")
        score += 1
        print("Score: " + str(score))
        print("")
        print("")
    else:
        print("Incorrect!")
        print("Correct answer: " + value["answer"])
        print("Score: " + str(score))
        print("")
        print("")

print("You got " + str(score) + "out of 7 questions!")
print("Your perentage is" + str(int(score/7*100)) + "%")
