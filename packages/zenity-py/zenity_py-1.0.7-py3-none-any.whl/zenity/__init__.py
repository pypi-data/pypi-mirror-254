# Zenity_py by Marko2155
# Please do not remove these comments, modify any code or reupload this to PyPI without crediting the owner first.
import tkinter.messagebox as tkm
import subprocess
from shutil import which


class Zenity:
    def __init__(self, title="Attention", text="This text box will close after 5 seconds.", type="info",
                 options=None):
        if options is None:
            options = ["!timeout", 5]
        self.text = text
        self.title = title
        self.type = type
        self.options = options
        self.command = ""
        args = ""
        for option in self.options:
            if str(option).startswith("!"):
                opt = str(option).replace("!", "")
                args += " --" + opt
            else:
                args += " " + str(option)
        self.command = "zenity --" + self.type + " --title " + self.title + " --text '" + self.text + "'" + args
        pass

    def Command(self):
        return self.command

    def Open(self):
        if which("zenity"):
            status, output = subprocess.getstatusoutput(self.command)
            return status, output
        else:
            tkm.showerror("Error", "Zenity was not found on your system. Please install it and then run this program again.")
