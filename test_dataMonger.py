import datamunger
import unittest
import io 
import sys 

class TestDataMonger(unittest.TestCase):

    def test_calc_total(self):
        #Basic Test
        current=[0,1,2,3,4,5,6,7,8]
        self.assertEqual(datamunger.calc_total(current),36)

        #Test inluding extra digits after the 9th Position 
        current=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28]
        self.assertEqual(datamunger.calc_total(current),72)

        #Test including digit in the first position 
        current=[36,1,2,3,4,5,6,7,8]
        self.assertEqual(datamunger.calc_total(current),36)

        #Test Larger Numbers
        current=[0,1458,2738,3875,4983,5674,6785,7654,8763]
        self.assertEqual(datamunger.calc_total(current),41930)

        #Test Negative Numbers
        current=[0,-1,2,-3,4,-5,6,-7,8]
        self.assertEqual(datamunger.calc_total(current),4)

        #Combination Test 
        current=[45,76,89,-473,9876,432,-987,4532,94,5431,68,-432]
        self.assertEqual(datamunger.calc_total(current),13639)


    def test_calc_monotonic(self):

        #Test with no errors
        output = io.StringIO()
        sys.stdout = output
        previous = [0,1,2,3,4,5,6,7,8]
        current =  [1,2,3,4,5,6,7,8,9]
        line = 10
        datamunger.check_monotonic(line,previous,current)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "")


        #Test with one error 
        output = io.StringIO()
        sys.stdout = output
        previous = [0,1,2,3,4,5,6,7,8]
        current =  [1,2,3,4,3,6,7,8,9]
        line = 10
        datamunger.check_monotonic(line,previous,current)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Monotonic error at column 4 comparing lines 9 and 10  values 3 and 4 \n")

        #Test with two errors 
        output = io.StringIO()
        sys.stdout = output
        previous = [0,1,2,3,4,5,6,7,8]
        current =  [1,2,3,4,3,6,7,5,9]
        line = 28
        datamunger.check_monotonic(line,previous,current)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Monotonic error at column 4 comparing lines 27 and 28  values 3 and 4 \nMonotonic error at column 7 comparing lines 27 and 28  values 5 and 7 \n")

        #Test with negatve number 
        output = io.StringIO()
        sys.stdout = output
        previous = [0,1,2,3,4,5,6,-5,8]
        current =  [1,2,3,4,5,6,7,-10,9]
        line = 35
        datamunger.check_monotonic(line,previous,current)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Monotonic error at column 7 comparing lines 34 and 35  values -10 and -5 \n")

        #Test with two errors 
        output = io.StringIO()
        sys.stdout = output
        previous = [0,244,2,3,4,5,783,7,8]
        current =  [1,-34,3,4,5,6,345,8,9]
        line = 53
        datamunger.check_monotonic(line,previous,current)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Monotonic error at column 1 comparing lines 52 and 53  values -34 and 244 \nMonotonic error at column 6 comparing lines 52 and 53  values 345 and 783 \n")


    def test_check_row(self):

        #Basic Test
        previous = [36,1,2,3,4,5,6,7,8]
        current = [44,2,3,4,5,6,7,8,9]
        line =1 
        self.assertEqual(datamunger.check_row(line,previous,current),True)


        #Test With Incorrect Sum
        output = io.StringIO()
        sys.stdout = output
        previous = [36,1,2,3,4,5,6,7,8]
        current = [42,2,3,4,5,6,7,8,9]
        line = 1
        datamunger.check_row(line,previous,current)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(),"Sum error at line  1 [42, 2, 3, 4, 5, 6, 7, 8, 9] computed 44 and expected 42\n")





if __name__ == '__main__':
    unittest.main()
