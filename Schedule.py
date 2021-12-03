class Schedule:
    def __init__(self):
        self.__advisorName = ""
        self.__hours_per_week = ""
        self.__monday = ""
        self.__tuesday = ""
        self.__wednesday = ""
        self.__thursday = ""
        self.__friday = ""

    def get_advisor_name(self):
        return self.__advisorName

    def set_advisor_name(self, advisor_name):
        self.__advisorName = advisor_name

    def get_hours_per_week(self):
        return self.__hours_per_week

    def set_hours_per_week(self, hours_per_week):
        self.__hours_per_week = hours_per_week

    def get_monday(self):
        return self.__monday

    def set_monday(self, monday):
        self.__monday = monday

    def get_tuesday(self):
        return self.__tuesday

    def set_tuesday(self, tuesday):
        self.__tuesday = tuesday

    def get_wednesday(self):
        return self.__wednesday

    def set_wednesday(self, wednesday):
        self.__wednesday = wednesday

    def get_thursday(self):
        return self.__thursday

    def set_thursday(self, thursday):
        self.__thursday = thursday

    def get_friday(self):
        return self.__friday

    def set_friday(self, friday):
        self.__friday = friday
