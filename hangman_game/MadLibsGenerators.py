from tkinter import *
import time
class Mad_Libs():
    def __init__(self):
        window = Tk()
        window.title('Mad Libs Generator')
        window.geometry('400x500')

        lbl_Mad_libs = Label(master=window, text='Mad Lib Generator',font=('Arial', 30, 'bold'))
        lbl_Mad_libs.place(x=50, y=50)

        lbl_click = Label(master=window, text='Click Any One:', font=('Arial', 25, 'bold'))
        lbl_click.place(x=30, y=110)

        bnt_photo_shoot = Button(master=window, text='Photo Shot', font=('Arial', 20),command=self.photo_shoot)
        bnt_gingerbread = Button(master=window, text='Gingerbread Man', font=('Arial', 20), command=self.Gingerbread_Man)
        bnt_butterfly = Button(master=window, text='Butterflies', font=('Arial', 20), command=self.butterfly)

        bnt_photo_shoot.place(x=50, y=180)
        bnt_gingerbread.place(x=50, y=230)
        bnt_butterfly.place(x=50,y=280)

        window.mainloop()

    def photo_shoot(self):

        print('Fill out these questions to generate your own silly mad libs story instantly \n'
              'Hint: a Verb is an action. An adverb usually ends in “ly” and describes an action\n' 
              '(like slowly). A noun is a person/place/thing. An adjective describes a person/place/thing.)')

        animals = input('Animals:')
        feeling = input('Feeling:')
        things_1 = input('Things:')
        professional = input('A professional:')
        clothing = input('A piece of clothing:')
        things_2 = input('Things: ')
        person = input('A person:')
        place = input('A place:')
        verb = input('Verb(ending in "ing"')
        food = input('Food:')
        time.sleep(2)
        print('Say \'%s,\' the photographer said as the camera flashed! %s and I had gone to \n'
                       '%s to get our photos taken today. The first photo we really wanted was \n'
                       ' a picture of us dressed as %s pretending to be a %s. When we saw the \n'
                       'proofs of it, I was a bit %s because it looked different than in my \n'
                       'head. (I hadn\'t imagined so many %s behind us.) However, the second \n'
                       'photo was exactly what I wanted. We both looked like %s wearing %s and \n'
                       '%s--exactly what I had in mind!'%(food, person,place,animals,professional,feeling,things_1,things_2,clothing,verb))


    def Gingerbread_Man(self):
        print('Fill out these questions to generate your own silly mad libs story instantly! \n'
              '(Hint: a Verb is an action. An adverb usually ends in “ly” and describes an \n'
              'action (like slowly). A noun is a person/place/thing. An adjective describes \n'
              'a person/place/thing.)')

        place = input('Place:')
        adjective = input('Adjective:')
        verb = input('Verb(action):')
        food = input('Food:')
        things = input('Things:')
        profession = input('Profession:')
        thing = input('Thing:')
        color = input('Color:')
        celebrity = input('Celebrity or someone famous:')
        animal = input('Animal:')
        time.sleep(2)
        print('There once was a gingerbread man who had two %s for eyes and a %s for a nose. \n'
              'He always said, \'%s as fast as you can, you can\'t catch me I\'m the gingerbread \n'
              'man.\' One day he ran past a %s %s, but they couldn\'t catch him. He kept \n'
              'running until he passed a %s, but they couldn\'t catch him either. Suddenly, he \n'
              'came across a river near %s. How would he cross? Then he saw a %s  %s \n'
              'floating by. He jumped on it, but it was actually %s--who just so happened \n'
              'to love cookies :)' %(things,food,verb,adjective,profession,animal,place,color,thing,celebrity))

    def butterfly(self):
        print('Fill out these questions to generate your own silly mad libs story instantly! \n'
              '(Hint: a Verb is an action. An adverb usually ends in “ly” and describes an action \n'
              '(like slowly). A noun is a person/place/thing. An adjective describes a person/place/thing.)')


        things = input('Things:')
        insect = input('A insect:')
        verb = input('Verb:')
        phrase = input('Phrase/Lyrics/Saying:')
        color = input('Color:')
        adjective_1 = input('Adjective:')
        food = input('Food:')
        person = input('Person:')
        adjective_2 = input('Adjective:')
        place = input('Place:')
        time.sleep(2)
        print('Last night I dreamed I was a %s butterfly with %s splotches that \n'
              'looked like %s. I flew to %s with my best friend, %s, who was a \n'
              '%s %s. We ate some %s when we got there and then decided to %s. \n'
              'The dream ended when I said, \'%s\n'
              'boat.\''%(adjective_2, place,color,things,person,adjective_1,insect,food,verb,phrase))

Mad_Libs()


