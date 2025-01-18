print("Welcome to quiz game!")
Players = input("Do you want to play game? = ")
if Players != "Yes":
        quit()
print("Let's start:) ")
score = 0
Question = input("How many days are there in a week? = ")
if Question == "7":
    print("YES, you are correct")
    score += 1
else:
    print("You are wrong")
Questionn  = input("How many days are there in a month? = ")
if Questionn == "30":
    print("YES, you are correct")
    score += 1
else:
    print("You are wrong")
Questionnn = input("How many days are there in a year? = ")
if Questionnn  == "365":
    print("YES, you are correct")
    score += 1
else:
    print("You are wrong")
Questionnnn = input("How many days are there in a two month? = ")
if Questionnnn  == "60":
    print("YES, you are correct")
    score += 1
else:
    print("You are wrong")

print("You got " + str(score) + " questions! correct")