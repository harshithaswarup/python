import unittest
from task_2_temp import *

class TestString(unittest.TestCase):
    def test_check(self):
        t=Temperature()
        self.date=t.get_date()
        self.assertEqual(self.date,'12/11/18')

    def test_date(self):
        t=Temperature()
        self.date=t.get_date()
        self.assertNotEqual(self.date,'13/11/18')

    def test_date1(self):
        t=Temperature()
        self.date=t.get_date()
        self.assertTrue(self.date,'12/11/18')

    def test_temp(self):
        t=Temperature()
        self.fin_dict=t.get_temprtr(date)
        fin_dict_1={'12/11/2018':[['234C',500,'500C']]}
        self.assertNotEqual(self.fin_dict,fin_dict_1)
        
        
if __name__=='__main__':
    unittest.main()

    
