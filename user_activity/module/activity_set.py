

def read_synopsis(path):
    with open(path, "r") as f:
        str = f.read()
        return str

def processing_data(data):
    data[1][0]["synopsis"] = read_synopsis(data[1][0]["book_synopsis_path"])
    data[1][0].pop("book_synopsis_path")
    return data