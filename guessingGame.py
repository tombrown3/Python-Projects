import random
secret_number = random.randint(0,10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess=int(input("Enter your guess:"))
    if guess == secret_number:
        print("Your guess is right")
        break
    elif guess!= secret_number:
        print("You are wrong try again:")
    guess_count = guess_count + 1
