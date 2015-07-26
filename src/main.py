__author__ = 'iamhssingh'
"""
Main file that runs everything
"""

# Import classes
from Compo.preset import *

# Import file that runs cmd commands
import Compo.cmdset as cmd

# Import messagebox widget
from tkinter import messagebox

# Import partial to send functions with argument as command
from functools import partial


# Create a main window
a = Form(475, 300, "HotSpot Management by Himanshu Shankar")
# Create some variables for future purpose
data = StringVar()
status = IntVar()


allowerror = "Error! Couldn't set HOSTEDNETWORK to ALLOW! Please contact creator!\n " \
                  "MAKE SURE YOU ARE RUNNING PROGRAM AS ADMINISTRATOR!"
ssiderror = "Error! Couldn't change SSID! Please check SSID NAME RULES or contact Creator!\n" \
            "MAKE SURE YOU ARE RUNNING PROGRAM AS ADMINISTRATOR!"
pwderror = "Error! Couldn't change PASSWORD!\n1. IS PASSWORD 8 digit long?\n" \
           "2. ARE YOU FOLLOWING PASSWORD RULES AS PER YOUR AUTHENTICATION SYSTEM?\n" \
           "PLEASE GOOGLE \"Can't change wifi password hostednetwork\" or contact CREATOR!"
success = "SSID and PASSWORD of WiFi HotSpot Changed successfully!"


def refresh_more():
    """
    This function fetches info of all the network connectivity and displays IP address with MAC Address
    and their Status(Dyanamic/Static) in a tkinter Messagebox of type Info!
    :return:
    """
    x = cmd.getmoreinfo()
    messagebox.showinfo(title="HotSpot More Details", message=x)


def help_me():
    """
    This fucntion generates a Info Messagebox which displays some info and help on how to use this software.
    :return:
    """
    help_me_text = "This application is created by Himanshu Shankar." \
                   "\n---------------------------------------------------------------------\n" \
                   "Please make sure following points are positive: \n" \
                   "1. Program is running as administrator.\n" \
                   "2. You have a WiFi Card installed on your laptop that can be used to create hotspot.\n" \
                   "3. You are using Windows Vista/+" \
                   "\n---------------------------------------------------------------------\n" \
                   "Now about how this works:-\n" \
                   "I have simply harvested some built in commands of Microsoft Windows 7. " \
                   "These commands are used to manage Microsoft VIRTUAL WiFi MiniPort Adapter" \
                   "This adapter allows you to create a hotspot at the same time when you're already using your" \
                   "WiFi card. Connectify and all other software use this same adapter and same commands!" \
                   "They, maybe, even use some command prompt commands that I have used." \
                   "\n---------------------------------------------------------------------\n" \
                   "Now, how to share your internet connection? \n" \
                   "1. Go to Control Panel\\Network and Internet\\Network Connections by doing either of:- \n" \
                   "      Right Click on Network Icon on taskbar OPEN NETWORK and SHARING CENTER" \
                   "OR Control Panel -> NETWORK and SHARING CENTER" \
                   " and then -> CHANGE ADAPTER SETTING (check on left side)\n" \
                   "2. Now you will see all your network adapters. You can also see MiniPort Adapter (remember" \
                   " its name for later use)\n" \
                   "3. Carefully select the adapter through which you're connected to internet and access its" \
                   "properties by clicking right mouse button! Then go to SHARING TAB \n" \
                   "4. Check Allow Other Netowrk users to connect.... \n" \
                   "5. Now, from list carefully select name of your MiniPort adapter!\n" \
                   "Bingo! YOU're DONE! Enjoy sharing your internet " \
                   "\n---------------------------------------------------------------------\n" \
                   "Please share this Application and if you face any error, contact me :-\n" \
                   "1. Facebook:- https://www.facebook.com/iamhssingh\n" \
                   "2. EMail:- imhs5496@gmail.com\n" \
                   "3. Twitter:- https://www.twitter.com/iamhssingh\n" \
                   "Thanks for using this!\n Please report bugs asap, if any!"
    messagebox.showinfo(title="Help Me ^.^", message=help_me_text)


def refresh():
    """
    This function changes the status of Buttons: Start HotSpot, Stop HotSpot and Setting and also changes
    the content of variable 'data' which in turn changes the label that displays detail of hotspot.
    :return:
    """
    x = cmd.getinfo()
    data.set(x[1])
    status.set(x[0])
    if status.get() == 0:
        start['state'] = NORMAL
        start['bg'] = "red"
        stop['bg'] = "yellow"
        set_button['state'] = NORMAL
        stop['state'] = DISABLED
    if status.get() == 1:
        start['state'] = DISABLED
        start['bg'] = "yellow"
        stop['bg'] = "red"
        set_button['state'] = DISABLED
        stop['state'] = NORMAL


def cntrl_hotspot(val=0):
    """
    This fucntions "Starts" and "Stops" the hotspot!
    :return:
    """
    x = 0
    if val == 1:
        x = cmd.start()
    elif val == 2:
        x = cmd.stop()
    if x == 2:
        messagebox.showwarning(title="Admin right not found", message="Start program as an Administrator!")
    elif x == 1:
        if val == 1:
            messagebox.showinfo(title="Success", message="HotSpot Started Successfully!")
        elif val == 2:
            messagebox.showinfo(title="Success", message="HotSpot Stoped Successfully!")
    else:
        messagebox.showwarning(title="Error", message=x[1])
    refresh()


def quitx(h=None):
    """
    This function facilitate Quiting of GUI Shells.
    :return:
    """
    cnfrm = messagebox.askyesno(title="Quit?", message="Are you sure you want to quit?")
    if cnfrm > 0:
        if h is not None:
            data.set(cmd.getinfo()[1])
            set_button['state'] = NORMAL
            h.destroy()
        elif h is None:
            a.destroy()


def settings():
    """
    This function is setting window function that is used to configure hotspot!
    :return:
    """
    set_button['state'] = DISABLED
    setwin = TL(235, 120, "Setting for HotSpot Management")
    ssid_name = StringVar(master=setwin)
    ssid_pwd = StringVar(master=setwin)
    setfrm = setwin.addFrame(padx=20, pady=20)
    addLabel(setfrm, 0, 0, "SSID: ")
    addLabel(setfrm, 1, 0, "PassWord: ")
    addEntry(setfrm, 0, 1, ssid_name)
    addEntry(setfrm, 1, 1, ssid_pwd)

    def change(name, pwd):
        """
        Changes Name and Password of hotspot.
        :param name: Name of HotSpot
        :param pwd: Password of HotSpot
        :return:
        """
        cmd.stop()
        z = cmd.changehotspot(name, pwd)
        if z[0] == 0:
            messagebox.showerror(master=setwin, title="Error!", message=allowerror)
            setwin.destroy()
            refresh()
        if z[1] == 0:
            messagebox.showerror(master=setwin, title="Error!", message=ssiderror)
            setwin.destroy()
            refresh()
        if z[2] == 0:
            messagebox.showerror(master=setwin, title="Error!", message=pwderror)
            setwin.destroy()
            refresh()
        else:
            messagebox.showinfo(master=setwin, title="Succes", message=success)
            setwin.destroy()
            refresh()

    addButton(setfrm, 2, 1, "Confirm", command=lambda: change(ssid_name.get(), ssid_pwd.get()))
    addButton(setfrm, 2, 0, "Cancel", command=partial(quitx, setwin))
    setwin.protocol("WM_DELETE_WINDOW", partial(quitx, setwin))

# Background colors to be used in frames. bgcolor: frame1, bgcolor1: frame2
bgcolor = 'darkorchid4'
bgcolor1 = "white"

# Frame1: Contains a Scroll Window b
frame1 = a.addFrame(width=195, fill=BOTH)
frame1.propagate(0)

# B: Scroll Window that contains control buttons
b = a.addscroll(master=frame1)

# Frame2: Contains Scroll Window c
frame2 = a.addFrame(fill=BOTH)

# c: Scroll Window that contains HotSpot Status and Setting button!
c = a.addscroll(master=frame2)

# Sets bgcolor of b and c.
b['bg'] = bgcolor
c['bg'] = bgcolor1

# Contents of b and c
addLabel(b, 0, 1, "Controls of HotSpot", bg=bgcolor, fg="white", font=("Times New Roman", 12, "bold underline italic"))
addLabel(b, 1, 1, "            ", bg=bgcolor, fg="white")
addLabel(b, 0, 0, "     ", bg=bgcolor, fg="white")

start = addButton(b, 2, 1, "Start HotSpot", command=partial(cntrl_hotspot, 1), fg="white", font=("Times New Roman", 9, "bold"))
addLabel(b, 3, 1, "                        ", bg=bgcolor, fg="white")

stop = addButton(b, 4, 1, "Stop HotSpot", command=partial(cntrl_hotspot, 2), fg="white", font=("Times New Roman", 9, "bold"))
addLabel(b, 5, 1, "                        ", bg=bgcolor, fg="white")

addButton(b, 6, 1, "Refresh HotSpot Details", command=refresh, bg="blue", fg="white", font=("Times New Roman", 10, "italic"))
addLabel(b, 7, 1, "                        ", bg=bgcolor, fg="white")

addButton(b, 8, 1, "More Detail on HotSpot", command=refresh_more, bg="blue", fg="white", font=("Times New Roman", 10, "italic"))
addLabel(b, 9, 1, "                        ", bg=bgcolor, fg="white")

addButton(b, 10, 1, "Help", command=help_me, bg="black", fg="white")

addLabel(c, 1, 0, "     ", bg=bgcolor1)
addLabel(c, 1, 1, "HotSpot Details", bg=bgcolor1, fg="black", font=("Times New Roman", 12, "bold underline italic"))
set_button = addButton(c, 3, 1, "Settings", command=settings, bg="red", fg="white", font=("Times New Roman", 11, "bold"))

info_label = addLabel(c, 2, 1, data.get(), bg=bgcolor1, fg='blue', font=("Times New Roman", 9, "bold"))
info_label['textvariable'] = data

# Event binding upon initiating close of window
a.protocol("WM_DELETE_WINDOW", quitx)

# Refresh to get content of HotSpot detial variable: 'data' and change status of buttons
refresh()

# Runs main window
a.mainloop()
