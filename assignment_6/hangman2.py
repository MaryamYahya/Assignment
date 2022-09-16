import random
import emoji
# from termcolor import colored
from pyfiglet import Figlet
import pyfiglet
# f=Figlet(font='isometric1')
# print(colored(f.renderText("\nhello"), 'red'))
print(pyfiglet.figlet_format('HANGMAN', font = '5lineoblique'))
print(emoji.emojize("hello my friend :red_heart:"))
print("Welcome to hangman game.\nPlease choose one of the categories to play.")
# print(emoji.emojize('Python is :thumbs_up:'))

def categury(categur):
    names = ['ali', 'atefeh', 'Sohrab', 'homa', 'roshanak', 'pouria',
             'sara', 'mohammad', 'hossein', 'samin', 'abbas', 'dariush']
    animals = ['cat', 'frog', 'chicken', 'turtle', 'crab', 'rabbit', 'shark', 'crocodile',
               'giraffe', 'cow', 'horse', 'butterfly', 'bull', 'pig', 'rhino', 'sheep', 'snake', 'panda']
    food = ['cheeseburger', 'spaghetti', 'steak',
            'sandwich', 'hamburger', 'pizza', 'sausage', 'pasta']
    body = ['eyes', 'teeth', 'toes', 'head', 'ears', 'eyebrow', 'hair', 'shoulder', 'tongue',
            'hand', 'finger', 'knee', 'moustache', 'ankle', 'nose', 'leg', 'thumb', 'neck']
    fruits = ["apple", 'watermelon', 'orange', 'pear', 'cherry', 'strawberry',
              'nectarine', 'grape', 'mango', 'pomegranate', 'banana', 'pineapple', 'peach']
    computer = ['mouse', 'microphone', 'battery', 'calculator', 'socket', 'controller', 'monitor',
                'printer', 'line', 'switch', 'laptop', 'keyboard', 'speakers', 'disc', 'tablet', 'phone', 'bug']
    music = ['violin', 'keyboard', 'saxophone', 'trumpet', 'clarinet', 'piano',
             'drums', 'guitar', 'accordion', 'tambourine', 'harp', 'harmonica', 'banjo', 'bow']
    countries = ['american', 'australia', 'canada', 'ireland', 'africa', 'france', 'spain',
                 'thailand', 'egypt', 'chaina', 'india', 'italy', 'turkey', 'russia', 'germany', 'japan']
    color = ['red', 'yellow', 'black', 'orange', 'purple',
             'blue', 'green', 'white', 'grey', 'brown']

    mach = {1: names, 2: animals, 3: food, 4: body, 5: fruits,
            6: computer, 7: music, 8: countries, 9: color}
    return mach[categur]


def show():
    for i in range(len(final_answer)):
        showlist.append('-')
    print("\nWord: "+''.join(showlist))


def Validation(word):
    while True:
        Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        if word in Alphabet:
            return True
        else:
            print("Please be careful in choosing the input!\n")
            return False


def repetition(word):
    while True:
        if word in showlist:
            print("The input letter has already been entered. Please enter another word.\n")
            return False
        else:
            return True


def guess(final_answer):
    answ = input("Can you guess what the correct answer is?! ")
    if answ == final_answer:
        print(emoji.emojize('You guessed right, congratulations :thumbs_up:'))
    else:
        print(f"I'm sorry dear, your guess was wrong. The correct word was {final_answer}.")


def caricature(coun):
    if coun == 1:
        print("________\n|\n|"+5*" "+"O"+"\n|\n|\n|\n")
    elif coun == 2:
        print("________\n|\n|"+5*" "+"O"+"\n|"+5*" "+"|"+"\n|\n|\n")
    elif coun == 3:
        print("________\n|\n|"+5*" "+"O"+"\n|"+4*" "+"/"+"|"+"\n|\n|\n")
    elif coun == 4:
        print("________\n|\n|"+5*" "+"O"+"\n|"+4*" "+"/"+"|"+"\\"+"\n|\n|\n")
    elif coun == 5:
        print("________\n|\n|"+5*" "+"O"+"\n|"+4 *
              " "+"/"+"|"+"\\"+"\n|"+4*" "+"/"+"\n|\n")
    elif coun == 6:
        print("________\n|\n|"+5*" "+"O"+"\n|"+4*" "+"/" +
              "|"+"\\"+"\n|"+4*" "+"/"+" "+"\\"+"\n|\n")
    elif coun == 7:
        print("________\n|"+5*" "+"|"+"\n|"+5*" "+"O"+"\n|"+4 *
              " "+"/"+"|"+"\\"+"\n|"+4*" "+"/"+" "+"\\"+"\n|\n")
        print("...Game Over...\n")
        return False


def end():
    play = input("\nDo you want to play again? yes or no? ... ")
    if play[0] == "y":
        return True
    else:
        print(emoji.emojize("\nHoping to meet my friend :red_heart:\n"))
        return False


while True:

    categur = int(input("\n1)names \n2)animals \n3)food \n4)body \n5)frouts \n6)computer \n7)music \n8)countries \n9)color \n:... "))
    sele = categury(categur)
    final_answer = random.choice(sele)
    showlist = []
    wronglist = []
    coun = 0
    print('If you want to guess the word, you can enter the word "guess"!')
    show()

    while True:
        if len(wronglist) == 7:
            caricature(7)
            break
        else:
            while True:
                word = input("Enter the chosen letter: ")
                word = word.lower()
                if word == 'guess':
                    guess(final_answer)
                    break
                else:
                    y_or_n = Validation(word)
                    if y_or_n == False:
                        continue
                    else:
                        repe = repetition(word)
                        if repe == False:
                            continue
                        else:
                            if final_answer.find(word) == -1:
                                wronglist.append(word)
                                coun += 1
                                comic=caricature(coun)
                                if comic==False:
                                    break
                            else:
                                for i in range(len(final_answer)):
                                    if final_answer[i] == word:
                                        showlist[i] = word
                                    else:
                                        continue
                            print("".join(showlist))
                            print(f"List of wrong letters={wronglist}")

                if "-" in showlist:
                    continue
                else:
                    print("\nyour win"+" \U0001F60D")
                    break
            break
    Result = end()
    if Result == True:
        continue
    else:
        break