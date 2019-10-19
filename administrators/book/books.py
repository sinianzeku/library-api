from xpinyin import Pinyin
from administrators.book import db_book
import os
import random
import string




class ChineseToPinyin():
    def __init__(self,bookname,auther):
        self.bookname = bookname
        self.auther = auther

    def bookname_to_py(self):
        p = Pinyin()
        bookname = p.get_pinyin(self.bookname,"")
        return bookname
    def auther_to_py(self):
        p = Pinyin()
        auther = p.get_pinyin(self.auther,"")
        return auther


class NewBookEntry():
    def __init__(self,data):
        self.data = data
        self.synopsis = data["synopsis"]
        py = ChineseToPinyin(data["book_name"], data["book_auther"])
        self.bookname = py.bookname_to_py()
        self.auther = py.auther_to_py()


    def save_synopsis(self):
        try:
            synopsis_path = 'C:/Users/zpg/Desktop/date/synopsis'
            file_exists = True
            while file_exists:
                ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 5))
                self.data["book_synopsis_path"] = synopsis_path + '/{}{}{}.txt'.format(self.bookname, self.auther,ran_str)
                if not os.path.isfile(self.data["book_synopsis_path"]):
                    file_exists = False
            file_handle = open(self.data["book_synopsis_path"], mode='w')
            file_handle.write(self.synopsis)
            file_handle.close()
            return [True]
        except:
            return False

    #数据入库
    def data_access_to_database(self):
        self.data.pop("synopsis")
        keys = ",".join(list(self.data.keys()))
        values = '","'.join(list(self.data.values()))
        result = db_book.insertnewbook(keys, values, )
        if not result[0]:
            return result
        self.book_id = result
        return [True]








