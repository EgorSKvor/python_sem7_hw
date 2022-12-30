from tkinter import *
from tkinter import ttk
import funcs
import controller as c


def menu(window: Tk):
    button_add_contact = Button(window, text="Добавить", font=(
        "Courier New", 14, "bold"), width=10, bg="blue", fg="white", command=lambda: new_data(window, False, c.add))
    button_edit_contact = Button(window, text="Редактировать", font=(
        "Courier New", 14, "bold"), width=14, bg="blue", fg="white", command=lambda: new_data(window, True, c.edit))
    button_delete_contact = Button(window, text="Удалить", font=(
        "Courier New", 14, "bold"), width=9, bg="blue", fg="white", command=lambda: delete_acception(window))
    button_find_contact = Button(window, text="Поиск", font=(
        "Courier New", 14, "bold"), width=7, bg="blue", fg="white", command=lambda: search_pane(window))
    button_add_contact.grid(column=0, row=0)
    button_edit_contact.grid(column=1, row=0)
    button_delete_contact.grid(column=2, row=0)
    button_find_contact.grid(column=3, row=0)


def init_window() -> Tk:
    global window
    window = Tk()
    window.title("Телефонный справочник")
    window.geometry("800x300+600+200")
    window.configure(bg="#00FA9A")
    window.resizable(False, False)
    global columns
    columns = ["name", "surname", "number", "comment"]
    global table
    table = ttk.Treeview(columns=columns, show="headings", height=11)
    show_list(funcs.show_list())
    return window


def show_list(contacts_list: list) -> ttk.Treeview:
    attributes = {
        "Имя": ("#1", NO, 100),
        "Фамилия": ("#2", NO, 100),
        "Номер телефона": ("#3", NO, 125),
        "Комментарий": ("#4", NO, 150)}
    table.grid(column=0, row=1, columnspan=4, rowspan=5)
    headings = list(attributes.keys())
    for i in range(len(headings)):
        table.heading(columns[i], text=headings[i])
        params = attributes.get(headings[i])
        table.column(params[0], stretch=params[1],
                     width=params[2], anchor=CENTER)
    data = table.focus()
    items = list(table.item(data, 'values'))
    item_copy = items.copy()
    if len(table.get_children()) > 1:
        table.delete(*table.get_children())
    for item in contacts_list:
        i = table.insert("", END, values=item)
        if list(item) == item_copy:
            table.focus(i)
    scrollbar = ttk.Scrollbar(orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(column=4, row=1, rowspan=5, ipady=96)
    return table


def change_visibility(labels: list, entries: list, buttons: list, state: bool):
    for i in range(len(labels)):
        if (state):
            labels[i].grid(column=5, row=i+1)
            entries[i].grid(column=6, row=i+1)
        else:
            labels[i].grid_remove()
            entries[i].grid_remove()
    if state:
        buttons[0].grid(column=5, row=5)
        buttons[1].grid(column=6, row=5)
    else:
        buttons[0].grid_remove()
        buttons[1].grid_remove()


def new_data(window, state, l_func):
    switch_remove(window)
    labels_text = ["Имя", "Фамилия", "Номер телефона", "Комментарий"]
    labels = []
    entries = []
    contact = ['', '', '', '']
    if state:
        data = table.focus()
        if data == '':
            data = table.get_children()[0]
        item = table.item(data)
        contact = item["values"]
        contact = [str(i) for i in contact]
    for i in range(len(labels_text)):
        labels.append(Label(window, text=labels_text[i], font=(
            "Courier New", 10, "bold"), bg="#00FA9A", fg="black"))
        labels[i].grid(column=5, row=1+i)
        entries.append(Entry(window))
        entries[i].insert(0, contact[i])
        entries[i].insert
        entries[i].grid(column=6, row=1+i)
    button_ok = Button(window, text="ОК", font=(
        "Courier New", 14, "bold"), width=7, bg="blue", fg="white", command=lambda: l_func(labels, entries, [button_ok, button_back]))
    button_ok.grid(column=5, row=5)
    button_back = Button(window, text="Назад", font=(
        "Courier New", 14, "bold"), width=7, bg="blue", fg="white", command=lambda: change_visibility(labels, entries, [button_ok, button_back], False))
    button_back.grid(column=6, row=5)


def delete_acception(window):
    switch_remove(window)
    data = table.focus()
    label_text = "Выберите контакт" if data == '' else "Подтвердить удаление\nвыбранного контакта?"
    label = Label(window, text=label_text, font=(
        "Courier New", 10, "bold"), bg="#00FA9A", fg="black")
    label.grid(column=5, row=1, columnspan=2, rowspan=4, padx=40)
    buttons = []
    if data != '':
        button_ok = Button(window, text="ОК", font=(
            "Courier New", 14, "bold"), width=7, bg="blue", fg="white", command=lambda: delete(label, buttons, True))
        button_ok.grid(column=5, row=5, padx=20)
        buttons.append(button_ok)
    button_back = Button(window, text="Назад", font=(
        "Courier New", 14, "bold"), width=7, bg="blue", fg="white", command=lambda: delete(label, buttons, False))
    button_back.grid(column=6, row=5, padx=40)
    buttons.append(button_back)


def delete(label, buttons, state: bool):
    label.grid_remove()
    for btn in buttons:
        btn.grid_remove()
    if state:
        data = table.focus()
        item = table.item(data)
        contact = item["values"]
        c.delete(contact)


def switch_remove(window):
    for item in window.grid_slaves():
        if 4 < int(item.grid_info()["column"]) < 7:
            item.grid_remove()


def search_pane(window):
    entry = Entry(window, font=("Courier New", 16, "bold"), width=15)
    entry.grid(column=5, row=1, columnspan=2, rowspan=4, padx=40)
    buttons = []
    button_search = Button(window, text="Найти", font=(
        "Courier New", 14, "bold"), width=7, bg="blue", fg="white", command=lambda: search(entry, buttons, True))
    button_search.grid(column=5, row=5, padx=20)
    buttons.append(button_search)
    button_back = Button(window, text="Назад", font=(
        "Courier New", 14, "bold"), width=7, bg="blue", fg="white", command=lambda: search(entry, buttons, False))
    button_back.grid(column=6, row=5, padx=40)
    buttons.append(button_back)


def search(entry, buttons, state):
    text = str(entry.get())
    if state:
        c.search(text)
    else:
        entry.grid_remove()
        for btn in buttons:
            btn.grid_remove()
        if len(table.get_children()) > 0:
            table.delete(*table.get_children())
        c.search('')
