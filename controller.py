from funcs import *
from view import *


def button():
    window = init_window()
    menu(window)
    window.mainloop()


def add(labels, entries, button_ok):
    add_contact(entries)
    change_visibility(labels, entries, button_ok, False)
