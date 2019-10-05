import tkinter as tk
from tkinter import ttk
import sys
import urllib
import json
import base64
from pygame import*


Large_Font = ("Verdana", 40)
from PIL import Image, ImageTk

def PlaytargetSound():
        mixer.init()
        mixer.music.load("sound_effects/Metal_Gong-Dianakc-109711828.wav")
        mixer.music.play()

def PlaytargetSound2():
    mixer.init()
    mixer.music.load("sound_effects/slot-machine-daniel_simon.wav")
    mixer.music.play()


class mainTkinter(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "That Program")
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree, PageFour):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")
            self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
        global username_variable
        
        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)
            load = Image.open("visuals/water_globe.jpg")
            render = ImageTk.PhotoImage(load)
            
            img = tk.Label(self, image=render)
            img.image = render
            img.place(x= 0, y=0)
            label = tk.Label(self, text= "Start Page", font=Large_Font)
            label.pack(pady=10, padx=10)
            button = ttk.Button(self, text="Visit Page 1",command = lambda: controller.show_frame(PageOne))
            button.pack()
            button2 = ttk.Button(self, text="Page 2",command = lambda: controller.show_frame(PageTwo))
            button2.pack()
            button4 = ttk.Button(self, text="Page 3",command = lambda: controller.show_frame(PageThree))
            button4.pack()
            
        
        
class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,)
        label1 = tk.Label(self, text= "Page 1", font=Large_Font)
        label1.pack(pady=10, padx=10)
        button1 = ttk.Button(self, text="Back to Home",command = lambda: [controller.show_frame(StartPage), PlaytargetSound()])
        button1.pack()
        button2 = ttk.Button(self, text="Page 2",command = lambda: controller.show_frame(PageTwo))
        button2.pack()
        button4 = ttk.Button(self, text="Page 3",command = lambda: controller.show_frame(PageThree))
        button4.pack()
        button5 = ttk.Button(self, text="slot machine",command = (PlaytargetSound2))
        button5.pack()
        

class PageTwo(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,)
        label2 = tk.Label(self, text= "Page 2", font=Large_Font)
        label2.pack(pady=10, padx=10)
        button2 = ttk.Button(self, text="Page 1",command = lambda: controller.show_frame(PageOne))
        button2.pack()
        button3 = ttk.Button(self, text="Back to Home",command = lambda: [controller.show_frame(StartPage), PlaytargetSound()])
        button3.pack()
        button4 = ttk.Button(self, text="Page 3",command = lambda: controller.show_frame(PageThree))
        button4.pack()

class PageThree(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,)
        label2 = tk.Label(self, text= "Page 3", font=Large_Font)
        label2.pack(pady=10, padx=10)
        button2 = ttk.Button(self, text="Page 1",command = lambda: controller.show_frame(PageOne))
        button2.pack()
        button3 = ttk.Button(self, text="Page 2",command = lambda: controller.show_frame(PageTwo))
        button3.pack()
        button4 = ttk.Button(self, text="Back to Home",command = lambda: [controller.show_frame(StartPage), PlaytargetSound()])
        button4.pack()
        button5 = ttk.Button(self, text ="Show Image", command = lambda: controller.show_frame(PageFour))
        button5.pack()
class PageFour(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,)
        load = Image.open("visuals/water_globe.jpg")
        render = ImageTk.PhotoImage(load)
        
        img = tk.Label(self, image=render)
        img.image = render
        img.pack()

        
app = mainTkinter()
app.mainloop()

