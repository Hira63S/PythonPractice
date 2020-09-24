#Testing:
#instance of object and methods
#unittest-testing the smallest possible testing
#testing means checking situation whether your code behaves as it should
#in this case, the units are built in methods.
#Assertions make the test case!!! if there is not asseration, there is no testcase
import unittest


class TestStringMethods(unittest.TestCase):
#we are declaring methods here, each method gets the self argument.
#you never have to tell what self is equal to, it literally says it is a noun
#then we invoke a method on it.
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

#let's make another model_selection

class TestIntegers(unittest.TestCase):

    def test_adding_integers(self):
        addition = 2 + 2
        self.assertEqual(addition, 4)

    def test_div_by_zero(self):
        #we can do this another threewaysplit
        with self.assertRaises(ZeroDivisionError): #we can assert with error. when we assert the code, it raises the zero division error
            div = 1/0
#        self.assertEqual(div , 1)

#    def test_int_is_not_float(self):


if __name__ == '__main__':
    unittest.main() #it  stays if you run it directly, it will run this line.
#we are not initiating self but the functions we are using here does it itself.
