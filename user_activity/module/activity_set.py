class Condition:
    def where_time(self,time):
        dict_time = {
            "week": ["past", 7],
            "month": ["past", 30],
            "season": ["past", 90],
            "half_a_year": ["past", 180],
            "year": ["past", 365]
        }
        self.times = dict_time[time]
        return self.times

    def language(self,languages):
        language_dict = {
            "中文图书": 0,
            "外文图书": 1
        }
        self.language = language_dict[languages]
        return self.language




