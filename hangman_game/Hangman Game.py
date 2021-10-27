import time
import random

print('Welcome to Hangman game')
print('\n')
name = input('Enter your name:')
time.sleep(1)
print('Hello, %s! Best of Luck!' % name)
time.sleep(2)
print('     Let\'s play Hangman!')


class Hangman():

    def __init__(self):
        self.words_list = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]


    def playloop(self):
        print('Do you want to play again? y = yes, n = no')
        ans = input('')
        if ans == 'y':
            self.hangman()
        elif ans=='n':
            print("Thanks For Playing! We expect you back again!")
            exit()


    def hangman(self):
        count = 0
        already_guessed = ''
        self.word_to_be_guessed = random.choice(self.words_list)
        for c in self.word_to_be_guessed:
            already_guessed += '_'
        max_count = len(self.word_to_be_guessed)
        while count <= 5:

            print('\n')
            print('This is the Hangman Word: %s Enter your guess:' % already_guessed)
            char_guessed = input()
            if not char_guessed.isalpha():
                print('Invalid Input, Try a letter')
            else:
                if char_guessed  in self.word_to_be_guessed:
                    new_guessed=''
                    for char_to_be_guessed, char_in_alreay_guessed in zip(self.word_to_be_guessed, already_guessed):
                        if char_to_be_guessed == char_guessed:
                            new_guessed += char_guessed
                        else:
                            new_guessed += char_in_alreay_guessed
                    already_guessed = new_guessed
                    if already_guessed ==self.word_to_be_guessed:
                        print(already_guessed)
                        print('\n')
                        print('Congrats! YOu have guessed the word correctly!')
                        break

                else:
                    count +=1
                    if count == 1:
                        time.sleep(1)
                        print ('  _____\n'
                               '  |    \n'
                               '  |    \n'
                               '  |    \n'
                               '  |    \n'
                               '  |    \n'
                               '  |    \n'
                               '  |    \n'
                               '__|__  \n')

                        print('Wrong guess. 4 guesses remaining')

                    elif count == 2:
                        time.sleep(1)
                        print('  _____\n'
                              '  |    |\n'
                              '  |    |\n'
                              '  |    \n'
                              '  |    \n'
                              '  |    \n'
                              '  |    \n'
                              '  |    \n'
                              '__|__  \n')

                        print('Wrong guess. 3 guesses remaining')
                    elif count == 3:
                        time.sleep(1)
                        print('  _____\n'
                              '  |    |\n'
                              '  |    |\n'
                              '  |    |\n'
                              '  |    \n'
                              '  |    \n'
                              '  |    \n'
                              '  |    \n'
                              '__|__  \n')

                        print('Wrong guess. 2 guesses remaining')

                    elif count == 4:
                        time.sleep(1)
                        print('  _____\n'
                              '  |    |\n'
                              '  |    |\n'
                              '  |    |\n'
                              '  |    o\n'
                              '  |    \n'
                              '  |    \n'
                              '  |    \n'
                              '__|__  \n')

                        print('Wrong guess. 1 guesses remaining')

                    elif count == 5:
                        time.sleep(1)
                        print('   ____\n'
                              '  |    |\n'
                              '  |    |\n'
                              '  |    |\n'
                              '  |    o\n'
                              '  |   /|\\\n'
                              '  |   / \\\n'
                              '  |    \n'
                              '__|__  \n')

                        print('Wrong guess. You are hanged!\n')

                        print('The word was:', self.word_to_be_guessed)
                        break

        self.playloop()





Hangman().hangman()
