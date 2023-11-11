import random

def words(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words


def evaluate_guess(guess, word):
    string = ''
    for i in range(5):
        if guess[i] == word[i]:
            string += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                string += "\033[33m" + guess[i]
            else:
                string += "\033[m" + guess[i]
    return string + "\33[0m"

def wordle(answers):
    print("Wordle!")
    secret_word = random.choice(answers)

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower()
        
        if guess == secret_word:
            print("Congratulations! You guessed " + secret_word)
            break
        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)

    if attempts > max_attempts:
        print("Game Over, The word was " + secret_word)




answers = words("answers.txt")

wordle( answers)