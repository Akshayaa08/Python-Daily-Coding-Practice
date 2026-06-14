#Python_Quiz_Game


questions = ("How many elements in a periodic table?: ",
             "Which animals lay the largest egg?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options= (("A. 116","B. 117","C. 118","D. 119"),
          ("A.Ostrich ", "B. Whale ","C. Crocodile ", "D. Elephant "),
          ("A.Nitrogen ", "B. Oxygen ","C. Carbon-Dioxide ", "D. Hydrogen "),
          ("A.206 ", "B.207 ","C.208 ", "D. 209"),
          ("A. Mercury ", "B. Venus ","C. Earth", "D. Mars"))

answers = ("C","A","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions: #This loop will run for all the questions and display the question for each iterations
    print("---------------------------")
    print(question)
    for option in options[question_num]: 
    #we will print every option in options at a given row number
        print(option)
    guess = input ("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT")
    else:
        print("INCORRECT")    
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("-------------------------")
print("         RESULTS         ")
print("-------------------------")


for answer in answers:
    print(answer, end=" ")
print()

for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(question)*100)
print(f"Your score is:{score}%")
