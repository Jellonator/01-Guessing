# MSCH-C220-guessing-game
A simple guessing game.

Run `main.py` to play a guessing game. The game will choose a random number between 1 and 100, and you have to guess what it is. If your guess is lower than the number, the game will tell you "Your guess is too low," and if your guess is larger than the number, the game will tell you "Your guess is too high." If you guess correctly, then the game will tell you that your answer is correct, how many guesses you took, and how much time it took you to guess correctly.

If you run `main.py --mode hotcold`, then the game will run in hot-cold mode instead. In this mode, you make a first guess. On all of your subsequent guesses, if your guess is closer to the answer than your previous guess, then the game will say "Warmer"; otherwise, if your answer is further from the answer than your previous guess, then the game will say "Colder". If you guess correctly, then the game will tell you that your answer is correct, how many guesses you took, and how much time it took you to guess correctly.
