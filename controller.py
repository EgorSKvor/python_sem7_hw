from funcs import show_list, edit_contact, delete_contact, find_contact, add_contact
from view import menu, input_choice


def button():
    menu()
    value = input_choice()
    if value == 1:
        show_list()
    elif value == 2:
        find_contact()
    elif value == 3:
        add_contact()
    elif value == 4:
        edit_contact()
    elif value == 5:
        delete_contact()
    elif value == 6:
        pass
