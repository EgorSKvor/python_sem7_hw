from tkinter import *
from tkinter import ttk
import funcs
import controller as c


def menu(window: Tk):
    button_add_contact = Button(window, text="Добавить", font=(
        "Courier New", 14, "bold"), width=10, bg="blue", fg="white", command=lambda: new_data(window))
    button_edit_contact = Button(window, text="Редактировать", font=(
        "Courier New", 14, "bold"), width=14, bg="blue", fg="white")
    button_delete_contact = Button(window, text="Удалить", font=(
        "Courier New", 14, "bold"), width=9, bg="blue", fg="white")
    button_find_contact = Button(window, text="Поиск", font=(
        "Courier New", 14, "bold"), width=7, bg="blue", fg="white")
    button_add_contact.grid(column=0, row=0)
    button_edit_contact.grid(column=1, row=0)
    button_delete_contact.grid(column=2, row=0)
    button_find_contact.grid(column=3, row=0)


def input_choice():
    choice = int(input('Choose option (1-6) '))
    return choice


def init_window() -> Tk:
    window = Tk()
    window.title("Телефонный справочник")
    window.geometry("800x300+600+200")
    window.configure(bg="#00FA9A")
    window.resizable(True, True)
    show_list(funcs.show_list())
    return window


def show_list(contacts_list: list) -> ttk.Treeview:
    columns = ["name", "surname", "number", "comment"]
    attributes = {
        "Имя": ("#1", NO, 100),
        "Фамилия": ("#2", NO, 100),
        "Номер телефона": ("#3", NO, 125),
        "Комментарий": ("#4", NO, 150)}
    table = ttk.Treeview(columns=columns, show="headings", height=11)
    table.grid(column=0, row=1, columnspan=4, rowspan=4)
    headings = list(attributes.keys())
    for i in range(len(headings)):
        table.heading(columns[i], text=headings[i])
        params = attributes.get(headings[i])
        table.column(params[0], stretch=params[1],
                     width=params[2], anchor=CENTER)
    for item in contacts_list:
        table.insert("", END, values=item)
    scrollbar = ttk.Scrollbar(orient="vertical", command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.grid(column=4, row=1, rowspan=4, ipady=96)
    return table


def change_visibility(labels: list, entries: list, button_ok: Button, state: bool):
    for i in range(len(labels)):
        if (state):
            labels[i].grid(column=5, row=i+1)
            entries[i].grid(column=6, row=i+1)
        else:
            labels[i].grid_remove()
            entries[i].grid_remove()
    if state:
        button_ok.grid(column=5, row=5, columnspan=2)
    else:
        button_ok.grid_remove()


def new_data(window):
    labels_text = ["Имя", "Фамилия", "Номер телефона", "Комментарий"]
    labels = []
    entries = []
    for i in range(len(labels_text)):
        labels.append(Label(window, text=labels_text[i], font=(
            "Courier New", 10, "bold"), bg="#00FA9A", fg="black"))
        labels[i].grid(column=5, row=1+i)
        entries.append(Entry(window))
        entries[i].grid(column=6, row=1+i)
    button_ok = Button(window, text="ОК", font=(
        "Courier New", 14, "bold"), width=7, bg="blue", fg="white", command=lambda: c.add(labels, entries, button_ok))
    button_ok.grid(column=5, row=5, columnspan=2)
    # change_visibility(labels, entries, False)
