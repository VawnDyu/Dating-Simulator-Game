from asyncio.windows_events import NULL
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def TypeAnimation(character, dialog, delta):
    scene1.create_text(310, 530, text=character, anchor=NW, fill="#3A9BDC", font=("Arial", 18), tags="character_textbox")
    text1 = scene1.create_text(310, 570, text="", anchor=NW, fill="#F5F5F5", font=("Arial", 16), tags="dialog_textbox")

    delay = 0

    for x in range(len(dialog)+1):
        s = dialog[:x]
        new_text = lambda s=s: scene1.itemconfigure(text1, text=s)
        scene1.after(delay, new_text)
        delay += delta

def ChangeBackground(path):
    scene1.itemconfig(SceneBg, image=path)

def EnableSkip():
    scene1.tag_bind('NextBtn', '<ButtonPress-1>', Scenario)

def DisableSkip():
    scene1.tag_unbind('NextBtn', '<ButtonPress-1>')


def ChoiceHover(event):
    current = event.widget.find_withtag("current")[0]

    if current == 4:
        event.widget.itemconfig(current, image=hoverchoice)
    elif current == 6:
        event.widget.itemconfig(4, image=hoverchoice)
    elif current == 5:
        event.widget.itemconfig(current, image=hoverchoice)
    elif current == 7:
        event.widget.itemconfig(5, image=hoverchoice)

def ChoiceLeave(event):
    current = event.widget.find_withtag("current")[0]

    if current == 4:
        event.widget.itemconfig(current, image=choice)
    elif current == 6:
        event.widget.itemconfig(4, image=choice)
    elif current == 5:
        event.widget.itemconfig(current, image=choice)
    elif current == 7:
        event.widget.itemconfig(5, image=choice)

def Options(choiceA, choiceB):
    global options

    options = True
    DisableSkip()

    scene1.itemconfigure(ImgChoiceA, state='normal')
    scene1.itemconfigure(ImgChoiceB, state='normal')

    scene1.itemconfigure(textChoiceA, state='normal', text=choiceA)
    scene1.itemconfigure(textChoiceB, state='normal', text=choiceB)


scene = 0
route = NULL
options = False
intro = NULL

def Scenario(event):

    global scene
    global options

    if (event) and (options == False):
        scene += 1
        scene1.delete("character_textbox")
        scene1.delete("dialog_textbox")
        
    # Me - Dialog 1
    if scene == 1:
        character = "Me"
        text = "Where am I? It's so dark in here..."
    elif scene == 2:
        character = "Me"
        text = "What am I doing here? This place is so scary."
    elif scene == 3:
        character = "Me"
        text = "Maybe I should go around and find some light..."
    elif scene == 4:
        character = "Me"
        text = "But which way should I go?"

        choiceA = "Go straight ahead."
        choiceB = "Go left through the dark woods."
        Options(choiceA, choiceB)

    elif scene == 5 and route == "A":
        ChangeBackground(dark_cliff)
        character = "Me"
        text = "Oh, I went into a dead end..."

    elif scene == 6 and route == "A":
        character = "Me"
        text = "It's pretty cool in here, I like it."

    elif scene == 7 and route == "A":
        character = "Me"
        text = "I should take a sit and rest here for a moment."

    elif scene == 8 and route == "A":
        character = "???"
        text = "*rustling bushes*"

    elif scene == 9 and route == "A":
        character = "Me"
        text = "What was that? Is anyone there?"

    elif scene == 10 and route == "A":
        character = "???"
        text = "*rustling bushes*"

    elif scene == 11 and route == "A":
        character = "Me"
        text = "I should check what's behind those rustling bushes."

    elif scene == 12 and route == "A":
        character = "???"
        text = "UWAHHH. I'm so sorry! I didn't mean to scare you."

        ShowCharacter(ysa_grin)
    
    elif scene == 13 and route == "A":
        character = "Me"
        text = "It's okay, it didn't scare me that much."

    elif scene == 14 and route == "A":
        character = "???"
        text = "Thank goodness! Anyways, what's your name?"

        ShowCharacter(ysa_smile)

        choiceA = "I'm Von"
        choiceB = "I'm your long lost friend..."
        Options(choiceA, choiceB)
    
    elif scene == 15 and route == "A" and intro == "Casual":
        character = "Me"
        text = "I'm Von. It's nice meeting you."

    elif scene == 16 and route == "A" and intro == "Casual":
        character = "Ysa"
        text = "Hi Von! I'm Ysa, it's nice meeting you, too."

    elif scene == 17 and route == "A":
        character = "Ysa"
        text = "What are you doing in this place? It's kinda dangerous in here."

    else:
        character = "No dialog"
        text = "Lorem Ipsum Penguin Malatek Kape Gatas Lorem Ipsum Penguin Malatek Kape Gatas Lorem Ipsum Penguin Malatek Kape Gatas"
    
    TypeAnimation(character, text, 30)
    print(scene)



def Start(event):                  
    canvas.pack_forget()
    scene1.pack()

    scene1.after(100, Scenario(event))
    EnableSkip()


def Exit(event):                  
    root.quit()

def onHover(event):
    current = event.widget.find_withtag("current")[0]
    event.widget.itemconfig(current, fill="white")

def onLeave(event):
    current = event.widget.find_withtag("current")[0]
    event.widget.itemconfig(current, fill="gray")

def HideChoice():
    scene1.itemconfigure(ImgChoiceA, state='hidden')
    scene1.itemconfigure(ImgChoiceB, state='hidden')
    scene1.itemconfigure(textChoiceA, state='hidden')
    scene1.itemconfigure(textChoiceB, state='hidden')

def HideCharacter():
    scene1.itemconfigure(character, state='hidden')

def ShowCharacter(path):
    scene1.itemconfigure(character, state='normal', image=path)

def PressChoiceA(self):
    global route
    global scene
    global options
    global intro

    if scene == 4:
        route = "A"
        options = False
        HideChoice()
        EnableSkip()
        Scenario(self)

    if scene == 14:
        intro = "Casual"
        options = False
        HideChoice()
        EnableSkip()
        Scenario(self)

def PressChoiceB(self):
    print("Route B")

cWidth = 1280
cHeight = 720

root = tk.Tk()

root.title("Dream")
root.resizable(0, 0)
root.geometry(str(cWidth) + "x" + str(cHeight))

canvas = tk.Canvas(root, width=cWidth, height=cHeight, bg="#000000", highlightthickness=0)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("img/background.jpg"))
img2 = ImageTk.PhotoImage(Image.open("img/main_menu.png"))

canvas.create_image(0, 0, anchor=NW,image=img)
canvas.create_image(0, 0, anchor=NW,image=img2)
start = canvas.create_text(80, 240, text="Start", fill="gray", font=("Arial", 24), tags="StartBtn")
help = canvas.create_text(79, 290, text="Help", fill="gray", font=("Arial", 24), tags="HelpBtn")
exit = canvas.create_text(72, 340, text="Exit", fill="gray", font=("Arial", 24), tags="ExitBtn")

canvas.tag_bind('StartBtn','<ButtonPress-1>', Start)
canvas.tag_bind('StartBtn','<Enter>', onHover)
canvas.tag_bind('StartBtn','<Leave>', onLeave)
canvas.tag_bind('HelpBtn','<Enter>', onHover)
canvas.tag_bind('HelpBtn','<Leave>', onLeave)
canvas.tag_bind('ExitBtn','<ButtonPress-1>', Exit)
canvas.tag_bind('ExitBtn','<Enter>', onHover)
canvas.tag_bind('ExitBtn','<Leave>', onLeave)

# Scene 1

scene1 = tk.Canvas(root, width=cWidth, height=cHeight, bg="#000000", highlightthickness=0)

# Image objects
ysa_smile = ImageTk.PhotoImage(Image.open("img/Ysa_smile.png"))
ysa_grin = ImageTk.PhotoImage(Image.open("img/Ysa_grin.png"))
cliff = ImageTk.PhotoImage(Image.open("img/background.jpg"))
dark_cliff = ImageTk.PhotoImage(Image.open("img/dark_cliff.jpg"))
night_beach_with_moon = ImageTk.PhotoImage(Image.open("img/night_beach_with_moon.jpg"))
night_beach = ImageTk.PhotoImage(Image.open("img/night_beach.jpg"))
dialoguebox = ImageTk.PhotoImage(Image.open("gui/textbox.png"))
choice = ImageTk.PhotoImage(Image.open("gui/button/choice_idle_background.png"))
hoverchoice = ImageTk.PhotoImage(Image.open("gui/button/choice_hover_background.png"))

SceneBg = scene1.create_image(0, 0, anchor=NW, image= night_beach)
character = scene1.create_image(180, 50, anchor=NW, image=ysa_smile, tags="character")
scene1.create_image(0, 510, anchor=NW, image= dialoguebox, tags='NextBtn')

ImgChoiceA = scene1.create_image(250, 430, anchor=NW, image=choice, tags='ImgChoiceA')
ImgChoiceB = scene1.create_image(250, 470, anchor=NW, image=choice, tags='ImgChoiceB')
textChoiceA = scene1.create_text(632, 448, anchor=CENTER, text="", fill="#F5F5F5", font=("Arial", 14), tags="ChoiceA")
textChoiceB = scene1.create_text(632, 488, anchor=CENTER, text="", fill="#F5F5F5", font=("Arial", 14), tags="ChoiceB")

HideCharacter()
HideChoice()

scene1.tag_bind('ChoiceA','<Enter>', ChoiceHover)
scene1.tag_bind('ImgChoiceA','<Enter>', ChoiceHover)
scene1.tag_bind('ChoiceA','<ButtonPress-1>', PressChoiceA)
scene1.tag_bind('ImgChoiceA','<ButtonPress-1>', PressChoiceA)
scene1.tag_bind('ImgChoiceA','<Leave>', ChoiceLeave)

scene1.tag_bind('ChoiceB','<Enter>', ChoiceHover)
scene1.tag_bind('ImgChoiceB','<Enter>', ChoiceHover)
scene1.tag_bind('ChoiceB','<ButtonPress-1>', PressChoiceB)
scene1.tag_bind('ImgChoiceB','<ButtonPress-1>', PressChoiceB)
scene1.tag_bind('ImgChoiceB','<Leave>', ChoiceLeave)

root.mainloop()