import unittest

from Samples import Palindrome


class unitTest(unittest.TestCase):

    def test_palindrome(self):

        #test = "malayalam"
        result = Palindrome.panlindrome("malayalam")

        self.assertEqual(result, True)


    def testFailCase_palindrome(self):

        #test = "malayalam"
        result = Palindrome.panlindrome("test")

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()