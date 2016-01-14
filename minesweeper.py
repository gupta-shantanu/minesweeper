from tkinter import *
from random import randint


class App:
    def __init__(self, a, b, c):
        self.master = Tk()
        self.ngame(self.master, a, b, c)
        self.master.title("MineSweeper  shantanu@programmer.net")
        self.master.mainloop()

    def ngame(self, master, a, b, c):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame,
                             text="QUIT", fg="darkred",
                             command=self.end)
        self.button.pack(side=LEFT)
        st = game(a, b, c)
        st.newgame()
        self.button = Button(frame,
                             text="NEW", fg="blue",
                             command=self.destr)
        self.button.pack(side=RIGHT)
        frame2 = st.drawframe(master)
        self.button = Button(frame,
                             text="FLAG", fg="darkgreen",
                             command=st.flag)
        self.button.pack(side=LEFT)
        self.L1 = Label(frame, text="Height")
        self.L1.pack(side=LEFT)
        self.E1 = Entry(frame, bd=1, width=2)

        self.E1.pack(side=LEFT)
        self.L1 = Label(frame, text="Width")
        self.L1.pack(side=LEFT)
        self.E2 = Entry(frame, bd=1, width=2)

        self.E2.pack(side=LEFT)
        self.L1 = Label(frame, text="Mines")
        self.L1.pack(side=LEFT)
        self.E3 = Entry(frame, bd=1, width=2)
        self.E3.pack(side=RIGHT)
        self.E1.insert(0, a)
        self.E2.insert(0, b)
        self.E3.insert(0, c)

        frame2.pack()

    def destr(self):
        a = int(self.E1.get())
        b = int(self.E2.get())
        c = int(self.E3.get())
        self.master.destroy()
        self.__init__(a, b, c)

    def end(self):
        quit()


class cell:
    def __init__(self):
        self.value = 0
        self.visible = 0


class game:
    def __init__(self, width, height, mines):
        self._difw_ = width
        self._difh_ = height
        self._mine_ = mines
        self.cells = [[cell() for j in range(0, self._difw_)] for i in range(0, self._difh_)]
        self.m1 = []
        self.flagster = 0

    def newgame(self):
        copy = self._mine_
        total = self._difw_ * self._difh_
        i = -1
        while copy:
            i = (i + 1) % (total)
            t = randint(0, total - 1)
            if self.cells[t // self._difw_][t % self._difw_].value == 0:
                self.cells[t // self._difw_][t % self._difw_].value = -100
                copy -= 1
        for i in range(0, self._difh_):
            for j in range(0, self._difw_):
                if self.cells[i][j].value < 0:
                    self.update(i, j, self.cells)


    def update(self, x, y, new):
        r = [-1, 0, 1]
        for i in r:
            for j in r:
                self.setcell(x + i, y + j, new)

    def setcell(self, x, y, new):
        try:
            if x >= 0 and y >= 0:
                new[x][y].value += 1
        except:
            pass

    def final(self):
        master = Tk()
        T = Text(master, height=2, width=30, fg="red")
        T.pack()
        T.insert(END, "YOU LOSE !!!")
        for i in self.m1:
            i["state"]="disabled"

    def press(self, x, y):
        if self.flagster != 1:
            self.m1[self._difw_ * x + y]["state"] = "disabled"
            self.m1[self._difw_ * x + y]["bg"] = "white"

            if (self.cells[x][y].value > 0):
                self.m1[self._difw_ * x + y]["text"] = self.cells[x][y].value
            elif (self.cells[x][y].value == 0):
                self.m1[self._difw_ * x + y]["text"] = " "
                self.chain(x, y)
            else:
                self.m1[self._difw_ * x + y]["text"] = "*"
                self.m1[self._difw_ * x + y]["bg"] = "darkred"
                self.final()
        else:
            self.flagster = 0
            if self.m1[self._difw_ * x + y]["bg"] != "yellow":
                self.m1[self._difw_ * x + y]["bg"] = "yellow"
                self.m1[self._difw_ * x + y]["fg"] = "red"
                self.m1[self._difw_ * x + y]["text"] = "F"
            else:
                self.m1[self._difw_ * x + y]["bg"] = "grey"
                self.m1[self._difw_ * x + y]["text"] = " "

    def altchain(self, x, y):
        try:
            if self.m1[self._difw_ * x + y]["state"] != "disabled" and x >= 0 and y >= 0 and \
                            self.m1[self._difw_ * x + y]["bg"] != "yellow":
                if self.cells[x][y].value == 0:
                    self.chain(x, y)
                elif self.m1[self._difw_ * x + y]["bg"] != "yellow":
                    self.press(x, y)
        except:
            pass

    def chain(self, x, y):
        self.m1[self._difw_ * x + y]["text"] = " "
        self.m1[self._difw_ * x + y]["state"] = "disabled"
        self.m1[self._difw_ * x + y]["bg"] = "white"
        r = [-1, 0, 1]
        for i in r:
            for j in r:
                self.altchain(x + i, y + j)

    def flag(self):
        if self.flagster == 0:
            self.flagster = 1
        else:
            self.flagster = 0


    def drawframe(self, master):
        frame = Frame(master)

        for i in range(0, self._difh_):
            for j in range(0, self._difw_):
                self.m1.append(Button(frame, text=" ", font="Verdana 15 bold", bg="grey", width=2,
                                      command=lambda a=i, b=j: self.press(a, b)))
                self.m1[self._difw_ * i + j].grid(row=i, column=j)
        return frame


app = App(10, 10, 10)


            
            
        

