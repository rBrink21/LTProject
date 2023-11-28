import unittest
from BillCalculator import BillCalculator


class TestBillCalculator(unittest.TestCase):
    def test_bill_calculator(self):
        b = BillCalculator(0)
        self.assertEqual(b.calculate_bill_amount(100, 10), 10)
        self.assertEqual(b.calculate_bill_amount(250, 50), 5)
        self.assertEqual(b.calculate_bill_amount(465, 25), 18)

    def test_create_bill_list(self):
        b = BillCalculator(123)
        #               100,50,20,10,5,1,.25,.1,.05,0.01
        expected_list = [1,0,1,0,0,3,0,0,0,0]
        actual_list = b.create_bill_list()
        self.assertEqual(expected_list, actual_list)

        b = BillCalculator(352.22)
        expected_list = [3,1,0,0,0,2,0,2,0,2]
        actual_list = b.create_bill_list()
        self.assertEqual(expected_list,actual_list)

    def test_denomination_to_string(self):
        b = BillCalculator(0)
        self.assertEqual(b.denomination_to_string(100),"$100 bill")
        self.assertEqual(b.denomination_to_string(1),"$1 bill")
        self.assertEqual(b.denomination_to_string(0.25),"quarter")
        self.assertEqual(b.denomination_to_string(0.1),"dime")
        self.assertEqual(b.denomination_to_string(0.01),"penny")

    def test_print_out(self):
        b = BillCalculator(19.99)
        self.assertEqual(b.get_bill_list(),[
                                            "1 - $10 bill",
                                            "1 - $5 bill",
                                            "4 - $1 bills",
                                            "3 - quarters",
                                            "2 - dimes",
                                            "4 - pennies"
        ])


if __name__ == '__main__':
    unittest.main()
