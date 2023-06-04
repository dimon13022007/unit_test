import unittest
from main import *


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.aut = Auto('Audi', 2021, 'Q7', 30000)
        self.emplo = Employee('Vlad', 'Kuriluk', 'Antonovich', '+380236844', 'sdggghc213@gmail.com')
        self.sale = Sales('Vlad', 'Kuriluk', 'Antonovich', '+380236844', 'sdggghc213@gmail.com', 'Audi', 2021, 'Q7',
                          30000, '13.1', 90000)

    def test_showInfo(self):
        expected_output = ('Car name - Audi'
                           'Car release - 2021'
                           'Car model - Q7'
                           'Sale price - 30000'
                           )
        self.assertEqual(self.aut.showInfo1(), expected_output)

    def test_showInfo2(self):
        excepted_output2 = ('Employee first name - Vlad'
                            'Employee last name - Kuriluk'
                            'Employee patronymic - Antonovich'
                            'Employee phone - +380236844'
                            'Employee gmail - sdggghc213@gmail.com'
                            )
        self.assertEqual(self.emplo.showInfo(), excepted_output2)

    def test_showInfo3(self):
        excepted_output3 = (f'Employee first name - Vlad '
                            'Employee last name - Kuriluk '
                            'Employee patronymic - Antonovich '
                            'Employee phone - +380236844 '
                            'Employee gmail - sdggghc213@gmail.com '
                            'Car name - Audi'
                            'Car release - 2021'
                            'Car model - Q7'
                            'Sale price - 30000'
                            'Date of sale - 13.1'
                            'Actual selling price - 90000'
                           )
        self.assertEqual(self.sale.showInfo2(), excepted_output3)


if __name__ == '__main__':
    unittest.main()
