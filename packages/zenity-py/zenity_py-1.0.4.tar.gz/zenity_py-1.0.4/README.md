# zenity-py - Zenity for Python
Exactly what it says it is.

# How to install
Just type ```python3 -m pip install zenity-py``` and it should install just fine.

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
