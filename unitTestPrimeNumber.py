import unittest

from Samples import primeNumber


class unitTest(unittest.TestCase):

    def test_prime(self):
        """test positive prime number """
        result = primeNumber.Prime(3)
        self.assertEqual(result, True)

    def test_nonprime(self):
        """test non prime number """
        result = primeNumber.Prime(4)
        self.assertEqual(result, False)

    def test_fraction_value(self):
        """test fractional value """
        result = primeNumber.Prime(3/4)
        self.assertEqual(result, False)

    def test_negative_integer(self):
        """test negative value """
        result = primeNumber.Prime(-4)
        self.assertEqual(result, False)

    def test_decimal_value(self):
        """test decimal value """
        result = primeNumber.Prime(3.75)
        self.assertEqual(result, False)

    def test_zero_value(self):
        """test zero value """
        result = primeNumber.Prime(0)
        self.assertEqual(result, False)

    def test_empty_string(self):
        """test empty string"""
        result = primeNumber.Prime("")
        self.assertEqual(result, False)

    def test_special_char(self):
        """test special characters"""
        result = primeNumber.Prime("#$%^&")
        self.assertEqual(result, False)

    def test_number_as_string(self):
        """test string input"""
        result = primeNumber.Prime("123")
        self.assertEqual(result, False)

    def test_noneinput(self):
        """test none input """
        result = primeNumber.Prime(None)
        self.assertEqual(result, False)



if __name__ == '__main__':
    unittest.main()