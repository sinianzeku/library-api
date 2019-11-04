from administrators.book import db_book
from config.defaulttime import set_time

class NewBookEntry():
    def __init__(self,data):
        self.book_synopsis = data["book_synopsis"]
        self.book_name = data["book_name"]
        self.book_auther = data["book_auther"]
        self.book_publisher = data["book_publisher"]
        self.book_room = data["book_room"]
        self.book_bookshelf = data["book_bookshelf"]
        self.book_publication_date = data["book_publication_date"]
        self.book_code = data["book_code"]
        self.category1 = data["category1"]
        self.category2 = data["category2"]
        self.book_language = data["book_language"]

    def verify_book_code(self):
        result = db_book.sql_verify_book_code(self.book_code)
        return result


    def query_book_category(self):
        result = db_book.sql_query_book_category(self.category1,self.category2)
        if not result[0]:
            return [False,result[1]]
        self.book_category = result[1]
        return [True]

    def language(self):
        book_language = {
        "中文图书":0,
        "西文图书":1
    }
        self.book_language = book_language[self.book_language]


    #数据入库
    def data_access_to_database(self):
        st = set_time()
        result = db_book.insertnewbook(
            book_code=self.book_code,
            book_name = self.book_name,
            book_auther = self.book_auther,
            book_category = self.book_category,
            book_publisher = self.book_publisher,
            book_room = self.book_room,
            book_bookshelf = self.book_bookshelf,
            book_synopsis = self.book_synopsis,
            book_publication_date = self.book_publication_date,
            books_add_time = st.today(),
            book_language = self.book_language
        )
        if not result[0]:
            return result
        return [True]








