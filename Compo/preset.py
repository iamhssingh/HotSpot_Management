__author__ = 'iamhssingh'
"""
Contains classes that I used in main.py to facilitate my working
Any advice is accepted. Creating classes for first time.
"""

from tkinter.tix import *


def addButton(master, row, column, text, imagez=None, command=None, **kwargs):
    """
    Creates a button and "GRIDS" it to master.
    :param master: MASTER WINDOW
    :param row: ROW
    :param column: COLUMN
    :param text: TEXT
    :param imagez: IMAGE, if any
    :param command: COMMAND, if any
    :param kwargs: any other parameter
    :return: button
    """
    button = Button(master=master, text=text, **kwargs)
    if imagez is not None:
        button['image'] = imagez
        if command is not None:
            button['command'] = command
        else:
            button['state'] = DISABLED
        button.image = imagez

    elif imagez is None:
        if command is not None:
            button['command'] = command
        else:
            button['state'] = DISABLED

    button.grid(row=row, column=column)
    return button


def addLabel(master, row, column, text, **kwargs):
    """
    Creates a label and grids it to master.
    :param master: MASTER
    :param row: ROW
    :param column: COLUMN
    :param text: TEXT
    :param kwargs: any other parameter
    :return: label
    """
    label = Label(master=master, text=text, **kwargs)
    label.grid(row=row, column=column)
    return label


def addEntry(master, row, column, variable, **kwargs):
    """
    Creates an Entry and grids it to master.
    :param master: MASTER
    :param row: ROW
    :param column: COLUMN
    :param variable: VAR() contains data that is entered
    :param kwargs: any other parameter
    :return: Entry
    """
    entry = Entry(master=master, textvariable=variable, **kwargs)
    entry.grid(row=row, column=column)
    return entry


class Form(Tk):
    """
    Creates a Tk Window.
    """

    def __init__(self, size_x, size_y, title, **kwargs):
        """
        Creates a Tk Window
        :param size_x: Horizontal Size
        :param size_y: Vertical Size
        :param title: Title
        :param kwargs: any other parameter
        :return:
        """
        super().__init__()
        self.update_idletasks()
        self.w = int(self.winfo_screenwidth()/2 - size_x/2)
        self.h = int(self.winfo_screenheight()/2 - size_y/2)
        self.geometry('{}x{}+{}+{}'.format(size_x, size_y, self.w, self.h))
        self.title("{}".format(title))

    def addFrame(self, border=4, relief=RIDGE, height=None, width=200, padx=4, pady=4, expand=1, fill=BOTH, side=LEFT, **kwargs):
        """
        Adds a frame to object.
        :param border: Border width
        :param relief: Style of border
        :param height: Height
        :param width: Width
        :param padx: Marginal gap horizontally
        :param pady: Marginal gap vertically
        :param expand: Will it expand as per content?
        :param fill: Will it fill X and Y?
        :param side: Will it orient to a side?
        :param kwargs: any other parameter
        :return: frame
        """
        frame = Frame(master=self, border=border, relief=relief, padx=padx, pady=pady, height=height, width=width, **kwargs)
        frame.pack(expand=expand, fill=fill, side=side)
        return frame

    def addscroll(self, master=None, width=None, height=None, **kwargs):
        """
        Adds a Scroll Window
        :param master: Master
        :param width: Width
        :param height: Height
        :param kwargs: any other argument
        :return: scroll window
        """
        if width is None:
            width = self.winfo_screenwidth()
        if height is None:
            height = self.winfo_screenheight()
        if master is None:
            master = self
        swin = ScrolledWindow(master=master, width=width, height=height, **kwargs)
        swin.pack(fill=Y, expand=1)
        x = swin.window
        return x


class TL(Toplevel):
    """
    Creates a top level
    """

    def __init__(self, size_x, size_y, title, **kwargs):
        """
        Creates a TopLevel Widget
        :param size_x: Horizontal Size
        :param size_y: Vertical Size
        :param title: Title
        :param kwargs: any other parameter
        :return:
        """
        super().__init__()
        self.update_idletasks()
        self.w = int(self.winfo_screenwidth()/2 - size_x/2)
        self.h = int(self.winfo_screenheight()/2 - size_y/2)
        self.geometry('{}x{}+{}+{}'.format(size_x, size_y, self.w, self.h))
        self.title("{}".format(title))

    def addFrame(self, border=4, relief=RIDGE, padx=4, pady=4, expand=1, fill=BOTH, side=LEFT, **kwargs):
        """
        Adds a frame to object.
        :param border: Border width
        :param relief: Style of border
        :param padx: Marginal gap horizontally
        :param pady: Marginal gap vertically
        :param expand: Will it expand as per content?
        :param fill: Will it fill X and Y?
        :param side: Will it orient to a side?
        :param kwargs: any other parameter
        :return: frame
        """
        frame = Frame(master=self, border=border, relief=relief, padx=padx, pady=pady, **kwargs)
        frame.pack(expand=expand, fill=fill, side=side)
        return frame
