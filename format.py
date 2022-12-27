FILE_TXT = "python_sem7_hw\data_base.txt"


def get_file_name(format: str) -> str:
    match format:
        case "txt":
            return FILE_TXT


def from_txt(data: str) -> list:
    data_list = data.split("\n\n")
    result_list = []
    for item in data_list:
        info = item.split('\n')
        result_list.append(tuple(info))
    return result_list


def to_txt(data: list) -> str:
    result = ""
    for item in data:
        for info in item:
            result += info + '\n'
        result += '\n'
    return result
