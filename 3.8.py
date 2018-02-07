import random

i= random.randint(1,10)
guess = 0

while guess != i:
    temp = input("input a number:")
    guess = float(temp)

    if guess != i:
        if guess > i:
            print("big")
        else:
            print("little")
    else:
        print("you are right")
        break
    print("please input again:")
print("bye")
