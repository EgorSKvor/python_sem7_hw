from funcs import *
from view import *


def button():
    window = init_window()
    menu(window)
    window.mainloop()


def add(labels, entries, buttons):
    add_contact(entries)
    change_visibility(labels, entries, buttons, False)
    show_list(funcs.show_list())


def edit(labels, entries, buttons):
    table = show_list(funcs.show_list())
    data = table.focus()
    item = table.item(data)
    contact = item["values"]
    contact = [str(i) for i in contact]
    index = funcs.find_contact(contact)
    funcs.edit_contact(index, entries)
    change_visibility(labels, entries, buttons, False)
    show_list(funcs.show_list())


def delete(contact: list):
    contact = [str(i) for i in contact]
    index = funcs.find_contact(contact)
    funcs.delete_contact(index)
    show_list(funcs.show_list())


def search(text: str):
    if text != '':
        show_list(funcs.search_contact(text))
    else:
        show_list(funcs.show_list())
