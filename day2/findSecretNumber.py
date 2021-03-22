
epsilon = 0.01
numGuesses = 0
low = 1.0
high = 100

while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    a = input(
        'Enter H if guess is too high, enter L if guess is low. Enter c if correct:  ')
    if a == 'c':
        print('El juego se acabó. Tu número secreto es', str(guess))
        break
    elif a == 'l':
        low = guess
    elif a == 'h':
        high = guess
    else:
        print('Sorry, your input is invalid')
