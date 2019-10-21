import datetime

class set_time():
    def today(self):
        self.today_time = datetime.date.today()
        return self.today_time

    def next_month(self):
        self.next_month_time = self.today_time + datetime.timedelta(days=30)
        return self.next_month_time






