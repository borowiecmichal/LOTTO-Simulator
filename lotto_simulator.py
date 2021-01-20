import random

guess_numbers = []
while len(guess_numbers) < 6:
    try:
        guess = int(input("Guess the number: "))
        if guess < 1 or guess > 49:
            print("Your number should be between 1 and 49")
            continue
        elif guess in guess_numbers:
            print("Numbers can't repeat")
            continue
        else:
            guess_numbers.append(guess)
    except:
        print("Give a number between 1 and 49")
guess_numbers.sort()
print("Your numbers are:", guess_numbers)

winning_numbers = []
while len(winning_numbers) < 6:
    num = random.randint(1, 49)
    if num in winning_numbers:
        continue
    else:
        winning_numbers.append(num)
winning_numbers.sort()
print("Winning numbers are:",winning_numbers)

guessed = 0
for x in range(6):
    if guess_numbers[x] in winning_numbers:
        guessed += 1

print(f"You've chosen correctly {guessed} numbers!")
