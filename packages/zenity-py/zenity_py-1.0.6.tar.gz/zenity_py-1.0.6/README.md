# zenity-py - Zenity for Python
Exactly what it says it is.

# How to install
Just type ```python3 -m pip install zenity-py``` and it should install just fine.

BUT, you need to also check if Zenity is installed.
Type in the Command Prompt/Terminal: ```zenity```.
If this is the output you get:
```
You must specify a dialog type. See 'zenity --help' for details
```
then you're good to go and you can get to using zenity-py.

If it says something like ```zsh: command not found: zenity``` or ```'zenity' is not recognized as an internal or external command, operable program or batch file.```, then you don't have it installed.

## How to install Zenity - Linux/Mac
On Linux, use your system's package manager or Homebrew to install it.
Example: ```sudo apt install zenity```

On Mac, use Homebrew to install it.
Example: ```brew install zenity```

## How to install Zenity - Windows
Install MinGW then search for Zenity in it. I don't use Windows anymore and I never really used MinGW for any other stuff other then make, so that's all i'm saying.

# How to use
In a python file, type
```python
from zenity import Zenity

# Zenity syntax - title, body, type, options[]
# the ! in !timeout means it is an option, not a value
z = Zenity("Title", "Body", "info", ["!timeout", 5])
```

This should create a new Zenity instance. Of course, this is an example, so you can change anything.
After that, add
```python
z.Open()
```

This should start up Zenity with the parameters you specified.
If a zenity window doesn't appear, something went wrong.
You can always print() the z variable, as the Zenity class returns both the status code and output.

If you want to know what arguments you can use, go over to the [Zenity Manual](https://help.gnome.org/users/zenity/stable/).
Do not add an option like !calendar or !password onto the options. Just change the type to "calendar" or "password".
