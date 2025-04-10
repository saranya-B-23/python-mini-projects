# Python Quiz Game

# we need a tuple of questions, options and answers

questions = ("How many elements are in the periodic table?: ",
             "Which Animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ",
             "What is the Capital of India?: ",
             "How many Continents are there in the world?: ",
             "What is the Study of Teeth?",
             "Who wrote the book Wings of Fire?: ",
             "Which Country has the most Population around the world?: ")

# two dimensional tuple for adding the options
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           ("A. New Delhi", "B. Chennai", "C. Mumbai", "D. Hyderabad"),
           ("A. 6", "B. 7", "C. 10", "D. 9"),
           ("A. Cardiologist", "B. Neurologist", "C. Dentist", "D. Dermatologist"),
           ("A. Dr.Rajendra Prasad", "B. Mr.Gopalan", "C. Ms.Vidhya Devi", "D. Dr.APJ Abdul Kalam"),
           ("A. USA", "B. China", "C. Russia", "D. France"))
answers = ("C","D","A","A","B","A","B","C","D","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter  (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("--------------------------")
print("         RESULTS          ")
print("--------------------------")

print("answers: ",end="")
for answer in answers:
    print(answer,end=" ")
print()


print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"Your score is : {score}%")