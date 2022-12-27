
def get_data(filename: str) -> str:
    with open(filename, "r") as fin:
        return fin.read()


def append_data(filename: str, data: str):
    with open(filename, "a") as fout:
        fout.write(data)


def set_data(filename: str, data: str):
    with open(filename, "w") as fout:
        fout.write(data)
