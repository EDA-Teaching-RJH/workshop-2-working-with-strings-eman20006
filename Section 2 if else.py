import random

answer = int(input("What is the secret number?"))
secret_number = random.randint(1, 10) 

if answer == secret_number:
    print("Well done, you guessed right!")

elif answer > secret_number:
    print("Too High!")

elif answer < secret_number:
    print("Too low!")    