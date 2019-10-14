from xpinyin import Pinyin
from db.book import db_book
import qrcode
import os


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
        self.bookname = data["bookname"]
        self.auther = data["auther"]

    #生成二维码
    def generate_QR_code(self):
        try:
            py = ChineseToPinyin(self.bookname,self.auther)
            bookname = py.bookname_to_py()
            auther = py.auther_to_py()
            QR_path = 'C:/Users/zpg/Desktop/QR'
            if not os.path.exists(QR_path):
                os.makedirs(QR_path)
            self.QR_path =QR_path +'/{}-{}.png'.format(bookname,auther)
            # 实例化QRCode生成qr对象
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
            )
            qr.add_data(self.data)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(self.QR_path)
            return [True]
        except:
            return [False]


    #数据入库
    def data_access_to_database(self):
        auther = self.auther
        bookname = self.bookname
        QR_path = self.QR_path
        result = db_book.insertnewbook(auther,bookname,QR_path)
        return result







