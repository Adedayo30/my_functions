
def hangman(secret='', num_guesses=''):
    """
    This function allows user to input a guess letter. 
    If the letter is found in the secret desired word it prints, '\You won'\ with the remaining trials otherwise, it prints '\You lost'\. 
    The program stops when the number of given trials is exhausted.
    """
    #Instruction
    print('\nYou have', num_guesses, 'trials in this game. Input \'0\' to quit at anytime.')
    while num_guesses>0: 
        user = input('\nEnter your guessed letter here: ')
        if user == '0': #for emergency stop
            break 
        if user in secret:
            print(user)
            num_guesses -=1
            print('You guessed right!')
            break
        else:
            num_guesses -=1
            print('_')
            print('You guessed wrong')
            print('Trial remains:', num_guesses)

    y = 'The secret word is: ' + secret
    return y
                
print(hangman(secret = 'unilag', num_guesses= 8))
