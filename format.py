FILE_TXT = "python_sem7_hw\data_base.txt"
FILE_CSV = "python_sem7_hw\data_base.csv"


def get_file_name(format: str) -> str:
    match format:
        case "txt":
            return FILE_TXT
        case "csv":
            return FILE_CSV


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


def from_csv(data: str) -> list:
    data_list = data.split("\n")
    result_list = []
    for item in data_list:
        info = item.split(';')
        result_list.append(tuple(info))
    return result_list


def to_csv(data: list) -> str:
    result = ""
    for item in data:
        for i in range(len(item)-1):
            result += item[i] + ';'
        result += item[len(item)-1]+'\n'
    return result
