import random
import hangman_art
import hangman_words


end_of_game = False
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
stage = hangman_art.stage
life = 6

print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print('you have entered this already')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter        
    if letter != guess:   
        if guess not in chosen_word:
            life -= 1
            print(stage[life])
        if life == 0:
            print("you lost")
            break
  

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
