import datetime


class set_time():

    def today(self):
        today_time = datetime.date.today()
        return today_time

    def next_month(self):
        today_time = datetime.date.today()
        next_month_time = today_time + datetime.timedelta(days=30)
        return next_month_time

    def time_frame(self, days):
        today_time = datetime.date.today()
        if days[0] == "past":
            the_time = today_time - datetime.timedelta(days=days[1])
            return the_time
        if days[0] == "future":
            the_time = today_time + datetime.timedelta(days=days[1])
            return the_time

    def first_half_year(self):
        time_dict = {}
        today_time = datetime.date.today()
        time_dict[int(today_time.strftime("%m"))] = today_time.strftime("%Y-%m")

        last_one_month = today_time.replace(day=1) - datetime.timedelta(days=1)
        time_dict[int(last_one_month.strftime("%m"))] = last_one_month.strftime("%Y-%m")

        last_tow_month = last_one_month.replace(day=1) - datetime.timedelta(days=1)
        time_dict[int(last_tow_month.strftime("%m"))] = last_tow_month.strftime("%Y-%m")

        last_three_month = last_tow_month.replace(day=1) - datetime.timedelta(days=1)
        time_dict[int(last_three_month.strftime("%m"))] = last_three_month.strftime("%Y-%m")

        last_four_month = last_three_month.replace(day=1) - datetime.timedelta(days=1)
        time_dict[int(last_four_month.strftime("%m"))] = last_four_month.strftime("%Y-%m")

        last_five_month = last_four_month.replace(day=1) - datetime.timedelta(days=1)
        time_dict[int(last_five_month.strftime("%m"))] = last_five_month.strftime("%Y-%m")
        return time_dict
