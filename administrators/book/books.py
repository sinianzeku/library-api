import os
import random
import string

from administrators.book import db_book
from administrators.module.defaulttime import set_time

class NewBookEntry():
    def __init__(self,data):
        self.synopsis = data["book_synopsis"]
        self.book_name = data["book_name"]
        self.book_auther = data["book_auther"]
        self.book_category = data["book_category"]
        self.book_publisher = data["book_publisher"]
        self.book_room = data["book_room"]
        self.book_bookshelf = data["book_bookshelf"]
        self.book_publication_date = data["book_publication_date"]



    def save_synopsis(self):
        synopsis_path = './data/synopsis'
        file_exists = True
        while file_exists:
            ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 20))
            self.book_synopsis_path = synopsis_path + '/{}.txt'.format(ran_str)
            if not os.path.isfile(self.book_synopsis_path):
                file_exists = False
        file_handle = open(self.book_synopsis_path, 'w')
        file_handle.write(self.synopsis)
        file_handle.close()
        return [True]


    #数据入库
    def data_access_to_database(self):
        st = set_time()
        result = db_book.insertnewbook(
            book_name = self.book_name,
            book_auther = self.book_auther,
            book_category = self.book_category,
            book_publisher = self.book_publisher,
            book_room = self.book_room,
            book_bookshelf = self.book_bookshelf,
            book_synopsis_path = self.book_synopsis_path,
            book_publication_date = self.book_publication_date,
            books_add_time = st.today()
        )
        if not result[0]:
            return result
        return [True]








