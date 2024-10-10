import win32com.client as comclt
from pynput.keyboard import Key, Listener
import time
from random import randint
wsh = comclt.Dispatch("WScript.Shell")
COMPLIMENT_LIST = [
    "Thx",
    "ty",
    "thx",
    "Thank you",
    "love you (no homo)",
    "you are amazing",
    "well done",
]
NEUTRAL_LIST = [
    "meh",
    "whatever",
    "Trust",
]
INSULT_LIST = [
    "Your two brain cells are fighting for third place",
    "You are adopted", "Don't know, don't care",
    "Didn't ask", "I despise you",
    "There is no way you just did that",
]
WORD_LIST = [COMPLIMENT_LIST, NEUTRAL_LIST, INSULT_LIST]
severity = 0


def writer(key: str) -> None:
    global severity
    if key == Key.right:
        if severity < len(WORD_LIST)-1:
            severity += 1
        print(severity, "r")
    if key == Key.left:
        if severity > 0:
            severity -= 1
        print(severity, "l")
    if key == Key.ctrl_r:
        wsh.SendKeys(chr(13))
        try:
            wsh.SendKeys(WORD_LIST[severity]
                         [randint(0, len(WORD_LIST[severity])-1)])
        except Exception:
            severity = severity
        wsh.SendKeys(chr(13))
    if key == Key.delete:
        return False


with Listener(on_release=writer) as listener:
    listener.join()
