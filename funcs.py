from view import menu


def show_list():
    with open('data_base.txt', 'r') as data:
        full_list = data.read()
    print(full_list)


def find_contact():
    finder = input('Enter first name of person u want to find ')
    with open('data_base.txt', 'r') as data:
        full_list = data.read()
    tolist = full_list.split('\n')
    list_from = tolist.index(finder)
    for i in range(list_from, list_from + 3):
        print(str(tolist[i]))

    print('Found succesful! ')


def add_contact():
    enter = input('Enter new contact ').split()
    for i in range(len(enter)):
        write_data = f'\n{enter[i]}'
        with open('data_base.txt', 'a') as data:
            data.write(write_data)
    print('Added succesful! ')


def edit_contact():
    with open('data_base.txt', 'r') as data:
        dataa = data.read().split('\n')
    todict = dict(zip([i for i in range(1, len(dataa))], dataa))
    for k, v in todict.items():
        s = str(k) + ' -> ' + str(v)
        print(s)
    input_key = int(input('Enter key of position u want to change '))
    new_value = input('Enter new value ')
    todict[input_key] = new_value
    new_list = list(todict.values())
    with open('data_base.txt', 'w') as data:
        data.write('')
    for i in range(len(new_list)):
        write_data = f'\n{new_list[i]}'
        with open('data_base.txt', 'a') as data:
            data.write(write_data)
    print('Edited succesful! ')


def delete_contact():
    name = input('Enter name of conact u want to delete ')

    with open('data_base.txt', 'r') as data:
        lst = data.read().split('\n')
    finder = lst.index(name)
    new_lst = []
    for i in range(finder, finder + 3):
        new_lst.append(lst[i])

    with open('data_base.txt', 'r'), open('data_base.txt', 'w') as outfile:

        for line in lst:
            if str(line) not in new_lst:
                outfile.write(f'\n{line}')
    print('Deleted succesful! ')
