# Zenity_py by Marko2155
# Please do not remove these comments, modify any code or reupload this to PyPI without crediting the owner first.
import tkinter.messagebox as tkm
import subprocess
from shutil import which


class Zenity:
    def __init__(self, title="Attention", text="This text box will close after 5 seconds.", type="info",
                 options=["!timeout", 5]):
        self.text = text
        self.title = title
        self.type = type
        self.options = options
        pass

    def Open(self):
        if which("zenity"):
            args = ""
            for option in self.options:
                if str(option).startswith("!"):
                    opt = str(option).replace("!", "")
                    args += " --" + opt
                else:
                    args += " " + str(option)
            status, output = subprocess.getstatusoutput("zenity --" + self.type + " --title " + self.title + " --text '" + self.text + "'" + args)
            return status, output
        else:
            tkm.showerror("Zenity was not found on your system. Please install zenity and try again")
