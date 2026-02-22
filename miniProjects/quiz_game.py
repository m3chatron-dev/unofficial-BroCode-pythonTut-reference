# Python quiz game

questions = ("What is the most abundant gas in Earth's atmosphere?: ",
             "When did Apollo 11 occur?: ",
             "Which planet in the solar system is the hottest?",
             "What plant has a visible hurricane known as the 'Big Red Spot'?: ",
             "What type of cell has a nucleus?: ")

options = (("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 1963", "B. 1974", "C. 1960", "D. 1969"),
           ("A. Mercury", "B. Jupiter", "C. Venus", "D. Mars"),
           ("A. Saturn", "B. Mercury", "C. Jupiter", "D. Mars"),
           ("A. Prokaryotic", "B. Eukaryotic", "C. Multicellular", "D. Unicellular"))

answers = ("A", "D", "C", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} was the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end = "")
for answer in answers:
    print(answer, end = " ")
print()

print("guesses: ", end = "")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")