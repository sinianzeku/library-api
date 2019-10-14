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
        self.synopsis = data["synopsis"]

        py = ChineseToPinyin(data["book_name"], data["book_auther"])
        self.bookname = py.bookname_to_py()
        self.auther = py.auther_to_py()


    #生成二维码
    def generate_QR_code(self):
        try:

            QR_path = 'C:/Users/zpg/Desktop/QR'
            if not os.path.exists(QR_path):
                os.makedirs(QR_path)
            self.data["book_QR_path"] =QR_path +'/{}-{}.png'.format(self.bookname,self.auther)

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
            )
            qr.add_data(self.data)
            qr.make(fit=True)
            img = qr.make_image()
            img.save(self.data["book_QR_path"])
            return [True]
        except:
            return [False]
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
        result = db_book.insertnewbook(keys,values,)
        return True




def sweepcode():
    import cv2
    import pyzbar.pyzbar as pyzbar

    camera = cv2.VideoCapture(0)

    barcodeData = 0
    while not barcodeData:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)  # 显示图片（摄像窗口）
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        barcodes = pyzbar.decode(image)
        for barcode in barcodes:
            # 提取条形码的边界框的位置
            # 画出图像中条形码的边界框
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # 条形码数据为字节对象，所以如果我们想在输出图像上
            # 画出来，就需要先将它转换成字符串

            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type

            # 绘出图像上条形码的数据和条形码类型
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        .5, (0, 0, 125), 2)

            # 向终端打印条形码数据和条形码类型





