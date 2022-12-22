def menu():
    print('*'*13 + ' Welcome to telephone list ' + '*'*13)
    print(' 1 - Show full list\n 2 - Find contact\n 3 - Add new contact\n 4 - Edit contact\n 5 - Delete contact\n 6 - Exit')


def input_choice():
    choice = int(input('Choose option (1-6) '))
    return choice
