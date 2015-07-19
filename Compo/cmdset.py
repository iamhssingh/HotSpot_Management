__author__ = 'iamhssingh'
"""
Contains all commands related to hotspot. Controls hotspot by executing commands in commandline.
"""

import subprocess


def getinfo():
    """
    Runs "netsh wlan show hostednetwork" in cmd.
    Puts the result in proper format in msg as string.
    Gets the status of HotSpot
    :return: Status(z), message(msg)
    """
    a = subprocess.check_output(["netsh", "wlan", "show", "hostednetwork"], shell=True)
    x = str(a)

    z = 0
    msg = ""

    if "Status                 : Not started" in x:
        z = 0
    elif "Status                 : Started" in x:
        z = 1

    for y in range(2, len(x)-1):
        if x[y] == "\\" and x[y+1] == "r" or x[y-1] == "\\" and x[y] == "r" or x[y-1] == "\\" and x[y] == "n":
            continue
        elif x[y] == "\\" and x[y+1] == "n":
            msg += '\n'
        else:
            msg += "{}".format(x[y])

    return z, msg


def getmoreinfo():
    """
    Runs "arp -a" in cmd.
    Puts the result in proper format in msg as string.
    :return: message(msg)
    """
    a = subprocess.check_output(["arp", "-a"], shell=True)
    x = str(a)

    msg = ""

    for y in range(2, len(x)-1):
        if x[y] == "\\" and x[y+1] == "r" or x[y-1] == "\\" and x[y] == "r" or x[y-1] == "\\" and x[y] == "n":
            continue
        elif x[y] == "\\" and x[y+1] == "n":
            msg += '\n'
        else:
            msg += "{}".format(x[y])

    return msg


def changehotspot(ssid, key):
    """
    Runs "netsh wlan set hostednetwork mode=allow ssid=SSID key=PASSWORD" in cmd.
    Puts the result in proper format in msg as string and checks if there is certain phrase in it.
    According to phrase sets status in list z[MODE CHANGED(0/1), SSID CHANGED(0/1), PASSWORD CHANGED(0/1)]
    :param ssid: SSID
    :param key: PASSWORD
    :return: z
    """
    p = "ssid={}".format(ssid)
    q = "key={}".format(key)
    if (len(key)<8):
        return [1, 1, 0]
    else:
        a = subprocess.check_output(["netsh", "wlan", "set", "hostednetwork", "mode=allow", p, q], shell=True)
        a = str(a)
        z = []
        if "The hosted network mode has been set to allow." in a:
            z.append(1)
        else:
            z.append(0)
        if "The SSID of the hosted network has been successfully changed." in a:
            z.append(1)
        else:
            z.append(0)
        if "The user key passphrase of the hosted network has been successfully changed." in a:
            z.append(1)
        else:
            z.append(0)
        return z


def stop():
    """
    Runs "netsh wlan stop hostednetwork" in cmd.
    Puts the result in proper format in msg as string and checks if there is certain phrase in it.
    According to phrase sets status in z.
    :return:z
    """
    cd = subprocess.check_output(["netsh", "wlan", "stop", "hostednetwork"], shell=True)
    a = str(cd)

    if "You must run this command from a command prompt with administrator privilege." in a:
        z = 2

    elif "The hosted network stopped." in a:
        z = 1

    else:
        z = [0, a]

    return z


def start():
    """
    Runs "netsh wlan stop hostednetwork" in cmd.
    Puts the result in proper format in msg as string and checks if there is certain phrase in it.
    According to phrase sets status in z.
    :return:z
    """
    cd = subprocess.check_output(["netsh", "wlan", "start", "hostednetwork"], shell=True)
    a = str(cd)

    if "You must run this command from a command prompt with administrator privilege." in a:
        z = 2

    elif "The hosted network started." in a:
        z = 1

    else:
        z = [0, a]

    return z
