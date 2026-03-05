#Number Guessing Game
target=75
attempt=0
max_attempts=5
print("I'm thinking of a number between 1 and 100. You have 5 attempts")
while attempt < max_attempts:
    num = int(input("Enter your guess: "))
    attempt+=1
    if num==target:
        print(f"Congratulations! You guessed it in {attempt} attempts!")
        break
    elif num<75:
        print(f"Attempt {attempt}/5 - Too low! Try again.")
    elif num>75:
        print(f"Attempt {attempt}/5 - Too high! Try again.")
if attempt == max_attempts and 75<num>75:
    print(f"Target number is {target}")
