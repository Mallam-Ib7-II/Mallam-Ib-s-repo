from hangman_art import body_arts
from rich.traceback import install
from rich.console import Console
from wordlist import WORD_LIST_CATEGORIES, hidden_word, clue_display
import random



install()
console = Console()

options = '''
        1: Persons
        2: Animals
        3: Places
        4: Things
    '''

def display_man(wrong_guess:int):
    console.print('\n******************', style='bold blue')
    for line in body_arts[wrong_guess]:
        console.print(line, style='bold red')
    console.print('******************\n', style='bold blue')
   
    
def play_again():
    print()
    answer = input('Do you want to play again? (y/n): ').lower()
    if answer == 'y':
        main()
    elif not answer.isalpha() and len(answer) != 1:
        print('\nInvalid input! Enter y or n.')
        play_again()
        
        
def word_list_category():
    options_dict = {
        1: 'names',
        2: 'animals',
        3: 'places',
        4: 'things',
    }
        
    try:
        category = int(input('Select a category (1 - 4): '))
    except (TypeError, RecursionError):
        console.print('\nInvalid Input! Please, enter digit (1 - 4)\n', style='bold red')
        word_list_category()
    else:
        if 0 < category < 5:
            word_list_choice : str = WORD_LIST_CATEGORIES[options_dict[category]]
        else:
            console.print('\nNumber too large! Please, enter digit (1 - 4)\n', style='bold red')
            word_list_category()
    return word_list_choice
                

def main():
    console.print('\n------------------------------HangMan--------------------------------')
    
    console.print(options, style='bold yellow')
    
    chosen_word = random.choice(word_list_category()).lower()
    clue = clue_display(chosen_word)
    hint = ' '.join(clue)
    
    wrong_guess : int = 0
    game_on = True
    guessed_letters = set()
    
    while game_on:
        console.print(hint, style='bold yellow', emoji=True)
        print()
        
        guessed_letter = input('Guess a letter: ').lower()
        
        if len(guessed_letter) == 1 and guessed_letter.isalpha():
            if guessed_letter in chosen_word:
                guessed_letters.add(guessed_letter)
                for index in range(len(chosen_word)):
                    if guessed_letter == chosen_word[index]:
                        clue[index] = guessed_letter
                            
                hint = ' '.join(clue)
                    
                if '_' not in hint:
                    console.print('Congratulations🎉 You Win!👏', style='bold blue')
                    console.print(f'The word is...{' '.join(chosen_word)}.', style='bold yellow')
                    game_on = False
            else:
                    display_man(wrong_guess=wrong_guess)
                    wrong_guess += 1
                    if wrong_guess == 7:
                        console.print('Game over! You lose😢', style='bold red')
                        console.print(f'The word is...{' '.join(chosen_word)}.', style='bold yellow')
                        game_on = False
        else:
            console.print('Oops! Input has more than one letter or is a number.', style='bold red')
            continue
        
    play_again()
    
   
if __name__ == '__main__':
    main()

























