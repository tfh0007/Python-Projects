#Thomas Hansknecht
#The purpose of this program is to create an interactive card game called Mad Gab.
import time
import sys
import random
import tkinter
from tkinter import *
outputDisplay = Tk()
userInput = StringVar()
time_selection = StringVar()
answerInput = userInput.get()
mEntry = Entry(outputDisplay)
from tkinter import messagebox

phrases = ["Know Sayer", "Up Arrow Tin Issues", "WANDER HER WOMB HEN", "APE HAND HUB HAIR", "PRETTY SHACK SCENT", "DEW WINO HUE", "MIKE RANCH HEALED WREN", "WEEDY MAN DONE ANT SIR", "HOUSE WHEAT THIS HOUND", "FIN SKATE", "AIL HUCK EACH ARM", "SEA CANT HIGHER DOVE FIT"] 
phrases_2 =["Hive Bin Gunnel Lung Thyme", "Bat Tree Snot Ink Looted","Fur Stings Versed", "Made Divorce Pea Whiff Ewe", "Gnu Your Cassidy", "Ray Dot Che Leap Hep Hearse", "Ohm They Eaters Hiss Dumb", "Come Pew Turf High Russ", "Flaw Coughs He Gals", "Lou Quad Hive Cot", "Abe Hole Hutch Hip Sand Hip", "Go Form Hints Pending", "Dawn Biafra Eight Duff Deed Arc", "Pair En Talc Hun Trolls" , "Pea Cup Tease Hope", "Pick Sin Herb Lank Hit","Heal Heck Trick Have A New","Strobe Bury Sink Ream","Lawn Guy Lend Diced He", "Oozer Fray Duff Deep Pig Pad Woof", "Neck Stayed Eel If Furry"] 
time = 0
difficulty = 0
points = 0
Answer = ""
phrase_1 = ""
Incorrect = 0
p = 0
q = 0



def entry_box(create,destroy):
    global userInput
    global answerInput
    global mEntry
    
    if( create == 1 ):
        m_Entry = Entry(outputDisplay,text ="clear",textvariable = userInput).place(x = 200, y=250)
        

    if(destroy == 1):
        userInput.set("")

def buttonContinue(event):
    run_Program_part_2()

def buttonSkip(event):
    skip_phrase()
    
def triggerHelp(event):
    # if messagebox.OKCANCEL('Explanation?', 'Would you like an explanation of how to play Mad Gab? If you need tips on how to use the program click no'):
    messagebox.showinfo('Mad Gab Game', "In Mad gab The puzzles, also known as mondegreens, contain small words that, when put together, make a word or phrase. Your job is to guess the phrase based on a combination of sylabols. You need to verbalize the sylabols in your mind or out loud in order to find the phrase.")

        
    #else:
#        showinfo('Mad Gab Game', "You need to select the time limit and game difficulty. When you are playing the game you need to type your answer in the box provided. You can submit the answer by either clicking continue or pressing the enter key. If you do not know the answer you can skip the phrase by pressing that button or by clicking the tab button on your keyboard.")
        

def Instructions():
    global difficulty
    if (difficulty == 1):
        messagebox.showinfo("Easy Mode" , "Instructions, In easy mode you will need to figure out the word or phrase provided. If you get the answer right you will receive 10 points. If you skip a phrase you will lose 5 points and if you get the answer wrong you will lose 2 points and be able to try and guess the answer. In easy mode you can only lose if you run out of time. Click continue to start the game.")
    else:
        messagebox.showwarning("Hard Mode" , "Instructions, In hard mode you will need to figure out the word or phrase provided. If you get the answer right you will receive 25 points. If you skip a phrase you will lose 5 points and if you get the answer wrong you will lose 6 points and be able to try and guess the answer up to three times. If you miss any phrase up to three times or if you run out of time you lose. Click continue to start the game.")
        
def time_picked():
    global q
    global p
    outputDisplay.unbind("<h>")
    time_final_decided = time_selection.get()
    if (time_final_decided == "30 seconds"):       
        q = 30
        p = 0
    if (time_final_decided == "45 seconds"):
        q = 45
        p = 0
    if (time_final_decided == "1 minute"):       
        q = 0
        p = 1
    if (time_final_decided == "2 minutes and 30 seconds"):
        q = 30
        p = 2
    if (time_final_decided == "5 minutes"):       
        q = 0
        p = 5

    func1()
 
def run_Program():
    global time
    global difficulty
    global points
    global Answer
    global phrase_1
    global phrase_2
    global mEntry
    
 
    entry_box(1,0)
    outputDisplay.bind("<Return>", buttonContinue)
    outputDisplay.bind("<Tab>", buttonSkip)
    mEntry.focus_set()
    mlabel = Label(outputDisplay,text = '                                                                     ').place(x = 180, y =6)
    mlabel = Label(outputDisplay,text = '                                                                                                 ').place(x = 50, y =104)
    mlabel = Label(outputDisplay,text = '                              ').place(x = 180, y =134)
    mlabel = Label(outputDisplay,text = '                              ').place(x = 300, y =134)

    if (len(phrases) == 0):
        points_visual = str(points)
        outputDisplay.withdraw()
        messagebox.showinfo("Important" , " Wow you tried all avaliable phrases and there are no more phrases left to try. Your final score was " + points_visual + ". Try and beat that next time!")
        sys.exit()

    if (difficulty == 1):

        
        phrase_1 = random.choice(phrases)
    
        
 
        mlabel = Label(outputDisplay, text = "Here is your Phrase").place( x = 220, y = 20)
        mlabel1 = Label(outputDisplay, text = "         ").place( x = 200, y = 205)
        mbutton3 = Button(outputDisplay,text = 'Continue',command = run_Program_part_2).place(x = 210, y =200)
        mbutton = Button(outputDisplay,text = 'Skip this phrase', command = skip_phrase, bg = "red").place(x = 300, y =200)
        outputDisplay.geometry('600x300+380+150')
        mlabel = Label(outputDisplay, text = phrase_1 + "                                        ").place( x = 220, y = 50)
        mlabel = Label(outputDisplay, text = "Total points").place( x = 500, y = 30)
        mlabel = Label(outputDisplay, text = "____________").place( x = 500, y = 50)
        points_visual = str(points)
        mlabel = Label(outputDisplay, text = "  " + points_visual + "  ").place( x = 532, y = 70)
        
 
        
        if (phrase_1 == "Know Sayer"):
                Answer = "nose hair"
        if (phrase_1 == "Up Arrow Tin Issues"):
                Answer = "a pair of tennis shoes"
        if (phrase_1 == "DEW WINO HUE"):
                Answer = "do i know you"
        if (phrase_1 == "WANDER HER WOMB HEN"):
                Answer = "wonder woman"
        if (phrase_1 == "APE HAND HUB HAIR"):
                Answer = "a panda bear"
        if (phrase_1 == "PRETTY SHACK SCENT"):
                Answer = "british accent"
        if (phrase_1 == "MIKE RANCH HEALED WREN"):
                Answer = "my grandchildren"
        if (phrase_1 == "DWELL FRO SIS"):
                Answer = "twelve roses"
        if (phrase_1 == "AIL HUCK EACH ARM"):
                Answer = "a lucky charm"
        if (phrase_1 == "WEEDY MAN DONE ANT SIR"):
                Answer = "we demand an answer"
        if (phrase_1 == "HOUSE WHEAT THIS HOUND"):
                Answer = "how sweet the sound"
        if (phrase_1 == "FIN SKATE"):
                Answer = "fence gate"
        if (phrase_1 == "SEA CANT HIGHER DOVE FIT"):
                Answer = "sick and tired of it"

    

    if difficulty == 2:
        phrase_2 = random.choice(phrases_2)

        if (len(phrases_2) == 0):
            points_visual = str(points)
            outputDisplay.withdraw()
            messagebox.showinfo("Important" , " Wow you tried all avaliable phrases and there are no more phrases left to try. Your final score was " + points_visual + ". Try and beat that next time!")
            sys.exit()
        
        mlabel = Label(outputDisplay, text = "Here is your Phrase").place( x = 220, y = 20)
        mlabel1 = Label(outputDisplay, text = "                     ").place( x = 200, y = 205)
        mbutton3 = Button(outputDisplay,text = 'Continue',command = run_Program_part_2).place(x = 210, y =200)
        mbutton = Button(outputDisplay,text = 'Skip this phrase', command = skip_phrase, bg = "red").place(x = 300, y =200)
        outputDisplay.geometry('600x300+380+150')
        mlabel = Label(outputDisplay, text = phrase_2 + "                                        ").place( x = 220, y = 50)
        mlabel = Label(outputDisplay, text = "Total points").place( x = 500, y = 30)
        if (difficulty == 2):
            mlabel = Label(outputDisplay, text = "Number of incorrect").place( x = 450, y = 180)
            mlabel = Label(outputDisplay, text = "answers").place( x = 460, y = 200)
        mlabel = Label(outputDisplay, text = "____________").place( x = 500, y = 50)
        points_visual = str(points)
        mlabel = Label(outputDisplay, text = "  " + points_visual + "  ").place( x = 532, y = 70)
        if(phrase_2 == "Hive Bin Gunnel Lung Thyme"):
                Answer = "ive been gone a long time"
        if(phrase_2 == "Lawn Guy Lend Diced He"):
                Answer = "long island iced tea"
        if(phrase_2 == "Oozer Fray Duff Deep Pig Pad Woof"):
                Answer = "whos afraid of the big bad wolf"
        if(phrase_2 == "Neck Stayed Eel If Furry"):
                Answer = "next day delivery"
        if(phrase_2 == "Strobe Bury Sink Ream"):
                Answer = "strawberries and cream"
        if(phrase_2 == "Heal Heck Trick Have A New"):
                Answer = "electric avenue"
        if(phrase_2 == "Pick Sin Herb Lank Hit"):
                Answer = "pigs in a blanket"
        if(phrase_2 == "Pea Cup Tease Hope"):
                Answer = "pick of the soap"
        if(phrase_2 == "Pair En Talc Hun Trolls"):
                Answer = "parental controls"
        if(phrase_2 == "Dawn Biafra Eight Duff Deed Arc"):
                Answer = "dont be afraid of the dark"
        if(phrase_2 == "Go Form Hints Pending"):
                Answer = "government spending"
        if(phrase_2 == "Abe Hole Hutch Hip Sand Hip"):
                Answer = "a bowl of chips and dip"
        if(phrase_2 == "Lou Quad Hive Cot"):
                Answer = "look what i've got"
        if(phrase_2 == "Come Pew Turf High Russ"):
                Answer = "computer virus"
        if(phrase_2 == "Flaw Coughs He Gals"):
                Answer = "flock of seagulls"
        if(phrase_2 == "Ohm They Eaters Hiss Dumb"):
                Answer = "home theater system"
        if(phrase_2 == "Ray Dot Che Leap Hep Hearse"):
                Answer = "red hot chili peppers"
        if(phrase_2 =="Gnu Your Cassidy"):
                Answer = "new york city"
        if(phrase_2 == "Made Divorce Pea Whiff Ewe"):
                Answer = "may the force be with you"
        if(phrase_2 == "Fur Stings Versed"):
                Answer = "first things first"
        if(phrase_2 == "Bat Tree Snot Ink Looted"):
                Answer = "batteries not included"
            
    if (difficulty == 1):
        phrases.remove(phrase_1)

    if (difficulty == 0):
        pause_program()
    if (difficulty == 2):
        phrases_2.remove(phrase_2)

 
    
def run_Program_part_2():
    global Answer
    global points
    global mEntry
    global Incorrect
    import time
    

    animal_output = userInput.get()
    animal2_output = str.lower(animal_output)
    answerInput = str.replace(animal2_output, "'" , "")
    if (answerInput == Answer):
        print( "Correct the answer was " + answerInput + "!")
        print (points)
        mlabel = Label(outputDisplay, text = "                                                                     ").place( x = 200, y = 50)
        if (difficulty == 1):
            points = 10 + points
            print (points)
            mlabel = Label(outputDisplay, text = "Correct  + 10 points   ", fg = "green", bg = "black").place( x = 450, y = 104)
        if(difficulty == 2):
            points = 25 + points
            print (points)
            mlabel = Label(outputDisplay, text = "Correct  + 25 points   ", fg = "green", bg = "black").place( x = 450, y = 104)
        run_Program()
        func3()
    else:
 
        visual_points = str(points)
        mlabel = Label(outputDisplay, text = "                                                                    ").place( x = 200, y = 50)
        if (difficulty == 1):
            mlabel = Label(outputDisplay, text = phrase_1 + "                       ").place( x = 200, y = 50)
            points = points - 2
            print ("Incorrect you just lost two points")


        if(difficulty == 2):
            mlabel = Label(outputDisplay, text = phrase_2 + "                       ").place( x = 200, y = 50)
            points = points - 6
            Incorrect = Incorrect + 1
            print ("Incorrect you just lost six points")
        mlabel = Label(outputDisplay, text = "  "+ visual_points + "      ").place( x = 532, y = 70)

        if(difficulty == 1):
            mlabel = Label(outputDisplay, text = "Incorrect  - 2 points   ", fg = "red", bg = "black").place( x = 450, y = 104)
        if(difficulty == 2):
            mlabel = Label(outputDisplay, text = "Incorrect  - 6 points   ", fg = "red", bg = "black").place( x = 450, y = 104)

        if (Incorrect == 1 and difficulty != 1):
            mlabel = Label(outputDisplay, text = u"\u274C", bg = "white").place( x = 450, y = 220)
        if (Incorrect == 2 and difficulty != 1):
            mlabel = Label(outputDisplay, text = u"\u274C", bg = "white").place( x = 475, y = 220)
        if (Incorrect == 3 and difficulty != 1):
            mlabel = Label(outputDisplay, text = u"\u274C", bg = "white").place( x = 500, y = 220)
            end_program2()
        print (points)
        func3()
    entry_box(0,1)
        



        

def difficulty_1():
    global difficulty
    difficulty = 1
    Instructions()

def difficulty_2():
    global difficulty
    difficulty = 2
    Instructions()


def skip_phrase():
    global points
    points = points - 5
    print (points)
    mlabel = Label(outputDisplay, text = "                                                            ").place( x = 200, y = 50)
    mlabel = Label(outputDisplay, text = "- 5 points for skipping", fg = "red", bg = "Black").place( x = 450, y = 104)
    entry_box(0,1)
    run_Program()    
    func3()
import threading

def func1():
    t = threading.Thread(target=func2)
    t.start()
    run_Program()
def func2():
    import time
    global p
    global q
    i=p
    j=q
    k=0
    while True:
        mbutton = Label(outputDisplay,text = u"\u23F2").place(x = 560, y =5)
        if(j==-1):
            j=59
            i -=1
        if(j > 30 or i > 0):
            if (j < 10):
                mbutton = Label(outputDisplay,text = str(k)+str(i)+":"+str(k)+str(j), fg = "black", bg = "green").place(x = 510, y =5)
            else:
                 mbutton = Label(outputDisplay,text = str(k)+str(i)+":"+str(j), fg = "black", bg = "green").place(x = 510, y =5)
            

        else:
            mbutton = Label(outputDisplay,text = "            ", fg = "red").place(x = 510, y =5)
            time.sleep(0.15)
            if (j < 10):
                mbutton = Label(outputDisplay,text = str(k)+str(i)+":"+str(k)+str(j), fg = "black", bg = "red").place(x = 510, y =5)
            else :
                mbutton = Label(outputDisplay,text = str(k)+str(i)+":"+str(j), fg = "black", bg = "red").place(x = 510, y =5)
                
            time.sleep(0.85)
            j -= 1
            if(i==0 and j==-1):
            
                break
            if(i==0 and j==-1):
                end_program()
            continue
 
        
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            
            break
    if(i==0 and j==-1):
        end_program()
        
        
        
        time.sleep(1)
#countdown(p,q) #countdown(min,sec)

def func3():
    t = threading.Thread(target=func4)
    t.start()
    return
def func4():
    import time
    i=0
    j=4
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            
            break
    if(i==0 and j==-1):
        mlabel = Label(outputDisplay, text = "                                             ", fg = "red", bg = "white").place( x = 450, y = 104)
        
        
        time.sleep(1)
#countdown(p,q) #countdown(min,sec)



def end_program():
    global points
    points_visual = str(points)
    outputDisplay.withdraw()
    messagebox.showinfo("Important" , " Uh Oh You ran out of time. Your final score was " + points_visual + ". Try and beat that next time!")
    sys.exit()
    
def end_program2():
    global points
    points_visual = str(points)
    outputDisplay.withdraw()
    messagebox.showinfo("Important" , " Uh Oh You had too many incorrect answers. Your final score was " + points_visual + ". Try and beat that next time!")
    sys.exit()
    
def pause_program():
    
    outputDisplay.withdraw()
    messagebox.showinfo("Important" , " You need to select a difficulty before pressing continue")
    sys.exit()      

def main():
    global difficulty
    outputDisplay.resizable(0,0)
    outputDisplay.geometry('600x350+380+150')
    outputDisplay.title('Mad Gab Game')
    mlabel1 = Label(outputDisplay,text='Please set the rules you would like').pack()
    mlabel3 = Label(outputDisplay,text='').pack()
    mlabel4 = Label(outputDisplay,text='').pack()
    
    time_selection.set("    Please select the time limit    ") # default value

    w = OptionMenu(outputDisplay, time_selection, "Please select the time limit", "30 seconds", "45 seconds", "1 minute", "2 minutes and 30 seconds", "5 minutes")
    w.place(x = 175, y=100)

    mbutton = Button(outputDisplay,text = 'easy difficulty',command = difficulty_1).place(x = 180, y =130)
    mbutton = Button(outputDisplay,text = 'hard difficulty',command = difficulty_2).place(x = 300, y =130)
    
    mbutton3 = Button(outputDisplay,text = 'Continue',command = time_picked).place(x = 210, y =200)

 
                
    outputDisplay.bind("<h>", triggerHelp)
    mlabel = Label(outputDisplay, text = "press h on your keyboard for info on how to play", bg = "red", fg = "white").place( x = 170, y = 300)
    
    outputDisplay.mainloop()


main()

