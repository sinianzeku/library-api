class Condition():
    def where_time(self,times):
        time = {
            "最近一周": ["past", 7],
            "近一个月": ["past", 30],
            "近三个月": ["past", 90],
            "近半年": ["past", 180],
            "近一年": ["past", 365]
        }
        return time[times]

    def language(self,languages):
        language = {
            "中文图书": 0,
            "西文图书": 1,
            "0": "中文图书",
            "1": "西文图书"
        }
        return language[languages]


    def books(self,books):
        book = {
            "书名": "book_name",
            "作者": "book_auther"
        }
        return book[books]

    def state(self,states):
        state = {
            "0": "在馆",
            "1": "已借出",
            "在馆": "0",
            "已借出": "1"
        }
        return state[states]

    def sex(self,sexs):
        sex = {
            '0': '女',
            '1': '男',
            '女': '0',
            '男': '1',
            None: '',
            '':''
        }
        return sex[sexs]



