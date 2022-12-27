import view as v
import database as d
import format as f


def show_list(_format: str = "txt") -> list:
    data = d.get_data(f.get_file_name(_format))
    return f.from_txt(data)


def find_contact():
    # запрос на ввод делается во view, из спец. поля считываем текст
    finder = input('Enter first name of person u want to find ')
    # вызвать функцию форматтера и сфррмировать список
    with open('data_base.txt', 'r') as data:
        full_list = data.read()
    # пробежать по списку и найти список совпадений (ну или если не заморачиваться, то одно совпадение)
    tolist = full_list.split('\n')
    list_from = tolist.index(finder)
    for i in range(list_from, list_from + 3):
        print(str(tolist[i]))
    # обновить view согласно тексту
    print('Found succesful! ')


def add_contact(entries: list):
    data = [item.get() for item in entries]
    data_list = [data]
    d.append_data(f.get_file_name("txt"), f.to_txt(data_list))
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
