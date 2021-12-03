import unittest

from WeeklyPay import WeeklyPay


class TestWeeklyPay(unittest.TestCase):

    def setUp(self):
        self.__weekly_pay = WeeklyPay()
        self.__weekly_pay.set_hourly(20)

    def test_compute_wage(self):
        self.assertEqual(self.__weekly_pay.compute_wage(24), 480)


if __name__ == '__main__':
    unittest.main()
