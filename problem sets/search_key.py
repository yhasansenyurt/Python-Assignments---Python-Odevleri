from tkinter import *
import random
import tkinter.messagebox
class MainGUI:
    def __init__(self):
        window = Tk()
        window.geometry("415x300")
        self.canvas = Canvas(window,width=500,height=250,bg="white")
        self.entry = StringVar()
        self.canvas.pack()
        window.title("Linear Search Animation")
        Label(window,text="Enter a key (in float):").place(x=100,y=265)
        self.ent = Entry(window,width=5,textvariable=self.entry)
        self.ent.place(x=215,y=267)
        self.ent.configure(state=DISABLED)
        self.stepb = Button(window,width=5,text="step",command=self.step)
        self.stepb.place(x=255,y=263)
        self.stepb.configure(state=DISABLED)
        self.button = Button(window,width=5,text="start",command=self.createRectangle)
        self.button.place(x=50,y=263)
        self.reset =Button(window, width=5,text="reset",command=self.resetButton)
        self.reset.place(x=300, y=263)
        self.reset.configure(state=DISABLED)

        window.mainloop()



    def createRectangle(self):
        self.button.configure(state=DISABLED)
        self.stepb.configure(state=ACTIVE)
        self.reset.configure(state=ACTIVE)
        self.ent.configure(state=NORMAL)
        self.a = [x for x in range(1,20)]
        random.shuffle(self.a)
        self.x1 = 0
        self.x2 = 20
        self.y2 = 250
        self.i = 0
        while True:
            if self.i == 19:
                break
            self.canvas.create_rectangle(self.x1,250 - self.a[self.i]*12,self.x2,self.y2)
            self.canvas.create_text(self.x1+10,240-self.a[self.i]*12,text=self.a[self.i])
            self.x1 += 20
            self.i += 1
            self.x2 += 20
    c = False
    def resetButton(self):
        global a1
        global a2
        global j
        global c
        global k
        self.c = True
        self.canvas.delete("all")
        self.a = [x for x in range(1, 20)]
        random.shuffle(self.a)
        self.x1 = 0
        self.x2 = 20
        self.y2 = 250
        self.i = 0
        while True:
            if self.i == 19:
                break
            self.canvas.create_rectangle(self.x1, 250 - self.a[self.i] * 12, self.x2, self.y2)
            self.canvas.create_text(self.x1 + 10, 240 - self.a[self.i] * 12, text=self.a[self.i])
            self.x1 += 20
            self.i += 1
            self.x2 += 20
        self.a1 =-20
        self.a2 =0
        self.j =0
        self.k =-1
    a1=-20
    a2=0
    j = 0
    k = -1
    def step(self):
        global a1
        global a2
        global j
        global c
        global k
        self.a1 += 20
        self.a2 += 20
        self.k += 1
        self.canvas.create_rectangle(self.a1, 250 - self.a[self.j] * 12, self.a2, self.y2,fill="red")
        self.j +=1
        self.canvas.create_rectangle(self.a1-20, 250 - self.a[self.j-2] * 12, self.a2-20, self.y2, fill="white")
        if int(self.entry.get()) == self.a[self.k]:
            tkinter.messagebox.showinfo("Message","You found it!")
            self.resetButton()



MainGUI()