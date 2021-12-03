import unittest

from MonthlyPay import MonthlyPay


class TestMonthlyPay(unittest.TestCase):
    def setUp(self):
        self.__monthly_pay = MonthlyPay()
        self.__monthly_pay.set_hourly(20)

    def test_compute_wage(self):
        self.assertEqual(self.__monthly_pay.compute_wage(24), 1920)


if __name__ == '__main__':
    unittest.main()
