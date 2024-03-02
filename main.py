from tkinter import *

class Frame(Tk):
    def __init__(self):
        super().__init__()
        self.title('Coloring')
        self.geometry("189x222")
        self.lbl = Label(text="", width=230)
        self.e1 = Entry(width=230, justify=CENTER)
        dct = {'#ff0000': 'Red',              '#ff7d00': 'Orange',
               '#ffff00': 'Yellow',               '#00ff00': 'Green',
               '#007dff': 'Blue',               '#0000ff': 'Dark Blue',
               '#7d00ff': 'Violett'}
        for colour in dct.keys():
            func = lambda c=colour, ruc=dct[colour]:\
                self.onclick(c, ruc)
            b = Button(text='',command=func, bg=colour, width=50, height=1)
            self.lbl.pack()
            self.e1.pack()
            b.pack()
    def onclick(self, colour, ru_colour):
        self.e1.delete(0, END)
        self.e1.insert(0, colour)
        self.lbl['text'] = ru_colour
if __name__ == '__main__':
    root = Frame()
    root.mainloop()
