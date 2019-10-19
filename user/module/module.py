import random,string,os

from xpinyin import Pinyin


def ChineseToPinyin(str):
        p = Pinyin()
        str = p.get_pinyin(str,"")
        return str


def save_feedbacks(feedbaccks,reader):
    while True:
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 5))
        reader = ChineseToPinyin(reader)
        path = "C:/Users/zpg/Desktop/date/feedbacks/{}{}.txt".format(reader,ran_str)
        if not os.path.isfile(path):
            file_handle = open(path, mode='w')
            file_handle.write(feedbaccks)
            file_handle.close()
            return path
