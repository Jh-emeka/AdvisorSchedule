""" this is entity MonthlyPay"""

from Pay import Pay


class MonthlyPay(Pay):

    def __init__(self):
        super().__init__()
        self.__hourly = 15.0  # default hourly wage for all advisors
        self.__total_hours = 0

    def get_hourly(self):
        return self.__hourly

    def set_hourly(self, hour):
        self.__hourly = hour

    def set_total_hours(self, hour):
        self.__total_hours = hour

    def get_total_hours(self):
        return self.__total_hours

    def compute_wage(self, hours):
        monthly_pay = (hours * self.get_hourly()) * 4

        return monthly_pay
