import view as v
import database as d
import format as f


def show_list(_format: str = "txt") -> list:
    data = d.get_data(f.get_file_name(_format))
    match _format:
        case "txt": return f.from_txt(data)[:-1]
        case "csv": return f.from_csv(data)[:-1]


def find_contact(info_list: list, _format: str = "txt") -> int:
    data_list = show_list(_format)
    index = 0
    for info in data_list:
        if list(info) == info_list:
            return index
        index += 1
    return -1


def add_contact(entries: list, _format: str = "txt"):
    data = [item.get() if item.get() != '' else '-' for item in entries]
    data_list = [data]
    match _format:
        case "txt": d.append_data(f.get_file_name("txt"), f.to_txt(data_list))
        case "csv": d.append_data(f.get_file_name("csv"), f.to_csv(data_list))
    print('Added succesful! ')


def edit_contact(index: int, entries: list, _format: str = "txt"):
    data_list = show_list(_format)
    if index == -1:
        print("Data wasn't selected! ")
    else:
        data_list[index] = [item.get() if item.get() !=
                            '' else '-' for item in entries]
        match _format:
            case "txt": d.set_data(f.get_file_name("txt"), f.to_txt(data_list))
            case "csv": d.set_data(f.get_file_name("csv"), f.to_csv(data_list))
        print('Edited succesful! ')


def delete_contact(index: int, _format: str = "txt"):
    data_list = show_list(_format)
    if index == -1:
        print("Data wasn't selected! ")
    else:
        data_list.pop(index)
        match _format:
            case "txt": d.set_data(f.get_file_name("txt"), f.to_txt(data_list))
            case "csv": d.set_data(f.get_file_name("csv"), f.to_csv(data_list))
    print('Deleted succesful! ')


def search_contact(text: str, _format: str = "txt") -> list:
    data_list = show_list(_format)
    return list(filter(lambda info: text in info, data_list))
