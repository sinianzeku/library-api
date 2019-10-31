import datetime

class set_time():

    def today(self):
        today_time = datetime.date.today()
        self.today_time = today_time
        return today_time

    def next_month(self):
        self.next_month_time = self.today_time + datetime.timedelta(days=30)
        return self.next_month_time

    def time_frame(self,days):
        if days[0] == "past":
            the_time = self.today_time - datetime.timedelta(days=days[1])
            return the_time
        if days[0] == "future":
            the_time = self.today_time + datetime.timedelta(days=days[1])
            return the_time







