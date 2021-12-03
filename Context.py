""" This is  Context"""


#  GoF strategy pattern  -------------------


class Context:

    def __init__(self, pay):
        self.__compute = pay

    def wage_computation(self, schedule):
        hour = int(schedule.get_hours_per_week())

        return self.__compute.compute_wage(hour)
