import random
import hangman_words
import hangman_arts

print(hangman_arts.logo)

chosen_word = random.choice(hangman_words.words_list)
print(f"Hint: The word has {len(chosen_word)} letters.")

display = []
for i in range(0, len(chosen_word)):
    display.append("_")

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Enter a letter: ").lower()
    if guess in display:
        print(f"You guessed {guess}, which you have already entered.")
    for i in range(0, len(chosen_word)):
        if (guess == chosen_word[i]):
            display[i] = guess
    print(display)
    
    if guess not in chosen_word:
        print(hangman_arts.stages[lives-1])
        lives = lives - 1
        print(f"Remaining lives: {lives}")
        if lives == 0:
            end_of_game = True
            print(f"The correct was {chosen_word}.\nYou have lost your lives. You lose.")

    if "_" not in display:
        end_of_game = True
        print(f"You guessed {chosen_word} right.")
        print("You Win.")