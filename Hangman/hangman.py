#HangmanGame
#Need to guess the word before the man gets hanged

#Taking random words from external wordlist
import random
def game():
    words = list(open("wordlist.txt"))
    guess_word = words[random.randint(0, len(words)-1)]
    dashes = ["_"]*(len(guess_word)-1)
    tries = len(str(guess_word))-1
    reset = []
    print(*dashes)
    
    while tries > 0:
        guess= str(input('Enter a value:'))
        if guess in str(guess_word) and len(guess) == 1:
            for i in guess_word:
                if i == guess:
                    dashes[guess_word.index(i)] = guess
            print(*dashes)
        else:
            tries -= 1
            print('You have', tries, ' tries left!')
            if tries == 0:
                print("You're out of tries!")
                reset.append(str(input('Restart? y/n :')))
                if 'y' in reset:
                    game()
            elif not "_" in dashes:
                print("You Guessed it!! The word was", guess_word)
                reset.append(str(input('Restart? y/n :')))
                if 'y' in reset:
                    game()
                    
game()
            
