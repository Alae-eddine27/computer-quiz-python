print("Welcome to my computer quiz!")
player = input("Do you want to play? ").lower()

if player != 'yes':
    quit()

print("Okay! Let's play!\n")

questions = {
    "What does CPU stand for?": "central processing unit",
    "What does RAM stand for?": "random access memory",
    "What does GPU stand for?": "graphics processing unit",
    "What does SSD stand for?": "solid state drive",
    "What does HTTP stand for?": "hypertext transfer protocol",
    "What does OS stand for?": "operating system",
    "What does USB stand for?": "universal serial bus",
    "What does IP stand for in IP address?": "internet protocol",
    "What does BIOS stand for?": "basic input output system",
    "What does LAN stand for?": "local area network",
}

score = 0

for question, correct_answer in questions.items():
    user_answer = input(f"{question} ").lower()
    if user_answer == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Incorrect! The answer is {correct_answer.title()}.\n")

total = len(questions)
print(f"Quiz complete! You scored {score}/{total}")

if score == total:
    print("Perfect score! Amazing!")
elif score >= 8:
    print("Great job!")
elif score >= 5:
    print("Not bad, keep learning!")
else:
    print("Better luck next time!")