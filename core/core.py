from tkinter import *
from tkinter import messagebox

about = '''Trail 0.0.0 Unreleased Canary Python 3 Tkinter 8.5
(trail-0.0.0-unreleased-canary-py.3.x.x-tk.8.5.x)

Trail is a simple game where you take over territory squares and compete with bots.

Credits----------------------------------------------------------------------

Ideas
Inspired by: John Doe

Programming
Main Programmer: Ken Shibata
Main Designer: Ken Shibata
Main Reviewer: Ken Shibata

License----------------------------------------------------------------------

This work is licensed under the Creative Commons Attribution-NoDerivatives-NonCommercial 4.0 International license.

Special Thanks---------------------------------------------------------------

Ken Shibata

John Doe

The Supporters of Trail

GitHub

Python Software Foundation

The Users of Trail'''

class app():
    def __init__(self, master):
        self.master = master
        self.root = Toplevel(self.master)
        self.root.title('Trail - Play')
        # self.root.geometry('960x540+100+100')
        self.bg = '#0f0'
        self.borderw = 5
        self.zonexy = 15
        self.zonesize = 30
        self.zones = []
        self.dotsize = 20
        self.dotnum = 1
        self.dotmargin = (self.zonesize - self.dotsize) / 2
        self.dots = []
        self.dotsCoords = {}
        self.cnvs = Canvas(self.root,
                           bg=self.bg, width=(self.zonesize + self.borderw) * self.zonexy + self.borderw,
                           height=(self.zonesize + self.borderw) * self.zonexy + self.borderw)
        print('a')
        for i in range(self.zonexy):
            print('aa')
            for j in range(self.zonexy):
                print('ab')
                self.zones.append(
                    self.cnvs.create_rectangle(self.borderw + i * (self.borderw + self.zonesize),
                                               self.borderw + j * (self.borderw + self.zonesize),
                                               self.borderw + i * (self.borderw + self.zonesize) + self.zonesize,
                                               self.borderw + j * (self.borderw + self.zonesize) + self.zonesize,
                                               fill='#fff',
                                               outline=self.bg))
        print('b')
        for i in range(self.dotnum):
            print('ba')
            self.dots.append(self.cnvs.create_oval(0, 0, self.dotsize, self.dotsize, fill='#f00', outline='#fff'))
            print('bb')
            self.move(self.dots[-1], i, 0)
        print('c')
        self.cnvs.pack(fill=BOTH)

    def move(self, obj, x, y):
        print(x, y)
        if x >= self.zonexy or y >= self.zonexy or x < 0 or y < 0:
            print('pass')
        else:
            self.cnvs.coords(obj,
                             self.cnvs.coords(self.zones[x * self.zonexy + y])[0] + self.dotmargin,
                             self.cnvs.coords(self.zones[x * self.zonexy + y])[1] + self.dotmargin,
                             self.cnvs.coords(self.zones[x * self.zonexy + y])[2] - self.dotmargin,
                             self.cnvs.coords(self.zones[x * self.zonexy + y])[3] - self.dotmargin)
            self.dotsCoords[obj] = [x, y]

    def moveUp(self, event=None):
        self.move(self.dots[0], self.dotsCoords[self.dots[0]][0], self.dotsCoords[self.dots[0]][1] - 1)

    def moveDown(self, event=None):
        self.move(self.dots[0], self.dotsCoords[self.dots[0]][0], self.dotsCoords[self.dots[0]][1] + 1)

    def moveLeft(self, event=None):
        self.move(self.dots[0], self.dotsCoords[self.dots[0]][0] - 1, self.dotsCoords[self.dots[0]][1])

    def moveRight(self, event=None):
        self.move(self.dots[0], self.dotsCoords[self.dots[0]][0] + 1, self.dotsCoords[self.dots[0]][1])

    def engine(self):
        print(self.dots, self.dotsCoords)
        self.root.bind('<Up>', self.moveUp)
        self.root.bind('<Down>', self.moveDown)
        self.root.bind('<Left>', self.moveLeft)
        self.root.bind('<Right>', self.moveRight)
        self.__init__(self.master)
        self.root.mainloop()


master = Tk()
master.title('Trail')
def showAbout(event=None):
    messagebox.showinfo('Trail - About',about)
def showExit(event=None):
    if messagebox.askquestion('Trail - Exit','Really exit Trail?',icon=messagebox.WARNING,type=messagebox.YESNO,parent=master) == messagebox.YES:
        exit()
x = app(master)
Button(master,text='NEW',font='sans 35',bg='#0f0',fg='#fff',command=x.engine,bd=0).pack(side=TOP,fill=BOTH)
Button(master,text='EXIT',font='sans 35',bg='#f00',fg='#fff',command=showExit,bd=0).pack(side=TOP,fill=BOTH)
Button(master,text='ABOUT',font='sans 35',bg='#00f',fg='#fff',command=showAbout,bd=0).pack(side=TOP,fill=BOTH)
master.mainloop()
