import win32com.client as comclt
from pynput.keyboard import Key, Listener
import winsound
from random import randint
wsh = comclt.Dispatch("WScript.Shell")
COMPLIMENT_LIST = [
    "Thx",
    "ty",
    "thx",
    "Thank you",
    "love you",
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
DURATION = 200
severity = 0


def beeping(pitch: int) -> None:
    """Makes noise 

    Args:
        noise (int): the input decides the pitch
    """
    winsound.Beep(pitch*1000+1000, DURATION)


def writer(key: str) -> None:
    """ It will make the other functions run their code and change the severity.

    Args:
        key (str): Its reads the key you are pressing and checks for \
        certain keys inputs. Its not really a string\
        but a input created from a class that was imported but it \
        behaves like a string

    Returns:
        _type_: it return "False" when the program is supposed to end
    """
    global severity
    if key == Key.right:
        if severity < len(WORD_LIST)-1:
            severity += 1
            beeping(severity)
    if key == Key.left:
        if severity > 0:
            severity -= 1
            beeping(severity)
    if key == Key.up or Key.down:
        beeping(severity)
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


if __name__ == "__main__":
    with Listener(on_release=writer) as listener:
        listener.join()
