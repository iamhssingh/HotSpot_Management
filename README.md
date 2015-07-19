# HotSpot_Management
I have created a GUI interface for managing HotSpot.


Files:-
  1. bin/HotSpotManagement_v5_64bit.exe :- This program will extract a folder to your specified location which contails EXECUTABLE FILES of this project that can be run on Windows 64 bit.
  2. bin/HotSpotManagement_v5_32bit.exe :- This program will extract a folder to your specified location which contails EXECUTABLE FILES of this project that can be run on Windows 32 bit. (COMMING SOON.. LIKE IN FEW HOURS)
  3. src :- Contains source code (.py)
  4. src/setup.py :- This can be used to create a "Executable" by running setup.py py2exe in cmd!

Requirements:-

  1. OS :- Windows Vista/+
  2. WiFi Card (Works on every laptop)
  3. Python (for .py files) - If you are dowloading compiled version then no need of this
  4. msvcr100.dll loaded in system. This is needed to run .exe compiled version.
  5. Run Program as Administrator

For msvcr100.dll:-
  Follow this link and guides here:- 
  http://www.dll-files.com/dllindex/dll-files.shtml?msvcr100

Language:-
  I have used Python 3.4 64 bit. It'll run on both 64 bit and 32 bit.

Libraries:-
  1. Tkinter for GUI
  2. subprocess for executing command prompt
  3. py2exe for compiling

Working:-
  Tkinter:-
    It creates a GUI interface that's it. I am not so good at graphics so please don't look at it. You can make contribution in that area if you want to.
  
  subprocess:-
    This part was tricky a bit keeping in mind I am first time using this utility. Anyway it executes some basic commands:-
      1. netsh wlan show hostednetwork :- It shows info of HotSpot Adabpter
      2. netsh wlan set hostednetwork mode=Allow ssid=SSID key=password :- It changed properties of hotspot
      3. netsh wlan start hostednetwork :- It starts the hotspot.
      4. netsh wlan stop hostednetwork :- It stops the hotspot.

That's it for now!
Please advice me on how to write this in better way. Not only code, but repository also. Share if you like it. Contribute if you want to! 

Thanks to FREENODE IRC WEB CHAT #PYTHON room that provided me hepl at times!
