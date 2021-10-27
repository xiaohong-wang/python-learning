import time
import hangman_game.Hangman as hangman_code


def main():
    print('Welcome to Hangman game')
    print('\n')
    name = input('Enter your name:')
    time.sleep(1)
    print('Hello, %s! Best of Luck!' % name)
    time.sleep(2)
    print('     Let\'s play Hangman!')
    hangman_code.Hangman().play_one_game()


if __name__ == "__main__":
    main()
