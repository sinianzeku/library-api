from xpinyin import Pinyin
from administrators.book import db_book



#将中文转成拼音
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

#新书入库
class NewBookEntry():
    def __init__(self,data):
        self.data = data
        self.synopsis = data["synopsis"]
        py = ChineseToPinyin(data["book_name"], data["book_auther"])
        self.bookname = py.bookname_to_py()
        self.auther = py.auther_to_py()

    #保存简介
    def save_synopsis(self):
        try:
            synopsis_path = 'C:/Users/zpg/Desktop/synopsis'
            self.data["book_synopsis_path"] = synopsis_path + '/{}-{}.txt'.format(self.bookname, self.auther)
            file_handle = open(self.data["book_synopsis_path"], mode='w')
            file_handle.write(self.synopsis)
            file_handle.close()
            return True
        except:
            return False

    #数据入库
    def data_access_to_database(self):
        self.data.pop("synopsis")
        keys = ",".join(list(self.data.keys()))
        values = '","'.join(list(self.data.values()))
        result = db_book.insertnewbook(keys, values, )
        self.book_id = result
        return True








