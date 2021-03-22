epsilon = 0.01
y = 120.0
guess = y/2.0
num_guesses = 0

# Using guess - (g**2 - y)/(2g)

while abs(guess*guess - y) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - y) / (2*guess))
print('numGuesses = ', str(num_guesses))
print('Square root of ' + str(y) + ' is about ' + str(guess))
