""" this is entity WeeklyPay"""
from Pay import Pay


class WeeklyPay(Pay):

    def __init__(self):
        super().__init__()
        self.__hourly = 15.0  # default hourly wage for all advisors

    def set_hourly(self, hourly):
        self.__hourly = hourly

    def get_hourly(self):
        return self.__hourly

    def compute_wage(self, hours):
        weekly_pay = hours * self.get_hourly()
        return weekly_pay
