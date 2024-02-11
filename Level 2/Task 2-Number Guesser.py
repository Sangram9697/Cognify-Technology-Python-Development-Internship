import random
def num_guess(low, high):
    #Generate a random number within the specified range
    secret_number = random.randint(low, high)
    print(f"Welcome to the Number Guessing Game! Try to guess the number between {low} and {high}.")
    attempts = 0
    while True:
        #Get the input from the user
        guess = int(input("Enter your guess: "))
        attempts += 1
        #Check if the guess is correct or not
        if(guess == secret_number):
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif(guess < secret_number):
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

if __name__ == "__main__":
    #Set the range for the random number (you can adjust this as needed)
    lower_limit = int(input("Enter the minimum number of the range: "))
    upper_limit = int(input("Enter the maximum number of the range: "))
    num_guess(lower_limit, upper_limit)
