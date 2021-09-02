import pyttsx3
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()



speak("This is a game of Rock,Paper and Scissors")
speak("Winning Rules of the Rock paper scissor game as follows:")
speak("Rock versus paper implies paper wins")
speak("Rock versus scissor implies rock wins")
speak("paper versus scissor implies scissor wins")


while True:

    speak("Choose one element from 1)Rock,2)Paper, 3)Scissors")
    speak('Enter your choice:')
    choice = int(input("User Choice: "))
    while choice > 3 or choice < 1:
        speak("Enter valid choice ")
        choice=int(input())
    if choice == 1:
        cname = 'Rock'
    elif choice == 2:
        cname = 'Paper'
    elif choice == 3:
        cname = 'Scissors'

    speak("Users Choice is " + cname)


    speak('Computers turn..')
    comp_choice = random.randint(1, 3)
    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        cpname = 'Rock'
    elif comp_choice == 2:
        cpname = 'Paper'
    elif comp_choice == 3:
        cpname = 'Scissors'

    speak("Computers Choice is " + cpname)

    print(cname +  " versus "  + cpname)

    if (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        speak("Paper wins")
        result = 2
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        speak('Scissors wins')
        result = 3
    elif (choice == 3 and comp_choice == 1) or (comp_choice == 3 and choice == 1):
        result = 1
        speak('Rock wins')

    if result == choice:
        speak("User wins!")
    elif result == comp_choice:
        speak("Computer wins!")
    speak('Do you want to play another round?')
    speak('Enter y for Yes and n for No')
    ans=input()
    if ans=='n' or ans=='N':
        break
speak("Thank you for playing")










