class Condition:
    def where_time(self,time):
        time = {
            "week": ["past", 7],
            "month": ["past", 30],
            "season": ["past", 90],
            "half_a_year": ["past", 180],
            "year": ["past", 365]
        }
        return time[time]

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



