# Hangman

import os
import random
import hangman_words
from hangman_art import stages, logo_english, logo_portuguese, you_win, game_over

end_of_game = False
lives = 6
display = []

language = input("Please choose in which language you want to play. (Por favor, escolha em que idioma gostaria jogar.)\nEnter 1 for English, Digite 2 para Português (Brasil): ").strip()

# English
if language == "1":
    chosen_word = random.choice(hangman_words.word_list)
    word_length = len(chosen_word)
    print(logo_english)
    print("Welcome to the game! You have 5 guesses.")
    
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        os.system('cls')

        if guess in display:
            print(f"You've already guessed {guess}.")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(stages[lives])
        print(f"{' '.join(display)}\n")

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"The word was: {chosen_word}.\n")
                print("Game Over.")
                print(game_over)

        if "_" not in display:
            end_of_game = True
            print("You win!")
            print(you_win)

# Português (Brasil)
elif language == "2":
    chosen_word = random.choice(hangman_words.lista_de_palavras)
    word_length = len(chosen_word)
    print(logo_portuguese)
    print("Bem vindo(a) ao jogo! Você tem 5 chances.")

    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Digite uma letra: ").lower()
        os.system('cls')

        if guess in display:
            print(f"Você já adivinhou a letra {guess}.")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        print(stages[lives])
        print(f"{' '.join(display)}\n")

        if guess not in chosen_word:
            print(f"Você digitou {guess}, isso não se encontra na palavra. Você perdeu 1 vida.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"A palavra era: {chosen_word}.\n")
                print("Game Over.")
                print(game_over)

        if "_" not in display:
            end_of_game = True
            print("Você ganhou!")
            print(you_win)
else:
    print("Invalid answer. (Resposta Inválida).")
    quit()