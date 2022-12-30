from funcs import *
from view import *


def button():
    window = init_window()
    menu(window)
    window.mainloop()


def add(labels, entries, buttons):
    format = get_format()
    add_contact(entries, format)
    change_visibility(labels, entries, buttons, False)
    show_list(funcs.show_list(format))


def edit(labels, entries, buttons):
    format = get_format()
    table = show_list(funcs.show_list(format))
    data = table.focus()
    item = table.item(data)
    contact = item["values"]
    contact = [str(i) for i in contact]
    index = funcs.find_contact(contact, format)
    funcs.edit_contact(index, entries, format)
    change_visibility(labels, entries, buttons, False)
    show_list(funcs.show_list(format))


def delete(contact: list):
    format = get_format()
    contact = [str(i) for i in contact]
    index = funcs.find_contact(contact, format)
    funcs.delete_contact(index, format)
    show_list(funcs.show_list(format))


def search(text: str):
    format = get_format()
    print(format)
    if text != '':
        show_list(funcs.search_contact(text, format))
    else:
        show_list(funcs.show_list(format))
