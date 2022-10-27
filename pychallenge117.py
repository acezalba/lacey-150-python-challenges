import csv
from random import randint

# Values to store
# User:
# Q1
# Correct Answer
# User Answer for Q1
# Q2
# Correct Answer
# User Answer for Q2
# Total Points

print("Welcome to the addition math quiz: ")
row = []

# User
user = str(input("What is your name: "))
row.append(user)

qItems = []
for item in range(4):
    qItems.append(randint(0, 100))
qAnswers = []
qAnswers.append(qItems[0] + qItems[1])
qAnswers.append(qItems[2] + qItems[3])

question0 = f"{qItems[0]} + {qItems[1]}? "
question1 = f"{qItems[2]} + {qItems[3]}? "
points = 0

# Question 1
uAnswer0 = int(input(question0))
row.append(question0)
row.append(qAnswers[0])
row.append(uAnswer0)
if uAnswer0 == qAnswers[0]:
    points = points + 1

# Question 2
uAnswer1 = int(input(question1))
row.append(question1)
row.append(qAnswers[1])
row.append(uAnswer1)
if uAnswer1 == qAnswers[1]:
    points = points + 1

# Points
print(f"You got {points} points!")
row.append(points)

# Write to file
with open("quiz.csv", "a", newline="") as file:
    csvWriter = csv.writer(file)
    csvWriter.writerow(row)
