import random

number = random.randint(1,100)

print("\n=== Welcome to Number Guessing Game ===")
print("Guess the number from 1 to 100")

guess = 0

while guess != number:
	guess = int(input("Enter your Guess: "))

	if guess > number:
		print("Too High,try again")

	elif guess < number:
		print("Too low,try again")

	else:
		print("Congratutions you guessed the number") 