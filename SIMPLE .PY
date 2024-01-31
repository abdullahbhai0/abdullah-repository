import random
numbrer =randiom.randint(1,10)
for i in range (0,3):
    uer = int(input("guess the number :  "))
    if user == number:
        print("congraturations!!")
        print(f"{numbrer}is the correct guess")
        break
    if user != number:
        print(f"your guessis in correct,{number}is the correct guess")