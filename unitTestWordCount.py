import unittest
from Samples import countWordsInFile

inputfile = 'testfile.txt'
inputemptyfile = 'emptytestfile.txt'

class unitTest(unittest.TestCase):

    def test_single_occurence(self):
        """test word count frequency 1 """
        result = countWordsInFile.countCheck("Apple", inputfile)
        self.assertEqual(result, 1)

    def test_multi_occurence(self):
        """test word count frequency greater than 1 """
        result = countWordsInFile.countCheck("mango", inputfile)
        self.assertEqual(result, 2)

    def test_multiple_values(self):
        """test word count frequency for multiple words """
        result = countWordsInFile.countCheck("mango", inputfile)
        self.assertEqual(result, 2)
        result = countWordsInFile.countCheck("strawberry", inputfile)
        self.assertEqual(result, 2)
        result = countWordsInFile.countCheck("pear", inputfile)
        self.assertEqual(result, 2)

    def test_incorrect_count(self):
        """test incorrect word count frequency"""
        result = countWordsInFile.countCheck("apple", inputfile)
        self.assertNotEqual(result, 1)

    def test_case_sensitive(self):
        """test case sensitive words """
        result = countWordsInFile.countCheck("APPLE", inputfile)
        self.assertNotEqual(result, 0)

    def test_empty_input(self):
        """test empty input """
        result = countWordsInFile.countCheck("", inputfile)
        self.assertEqual(result, 0)

    def test_none_input(self):
        """test none input """
        result = countWordsInFile.countCheck(None, inputfile)
        self.assertEqual(result, 0)

    def test_empty_input_file(self):
        """test empty input file """
        result = countWordsInFile.countCheck('apple', inputemptyfile)
        self.assertEqual(result, 0)

    def test_isalpha_input(self):
        """test alphanumeric input """
        result = countWordsInFile.countCheck('1234abc', inputfile)
        self.assertEqual(result, 0)

    def test_nonexisting_file(self):
        """test non existing input file"""
        result = countWordsInFile.countCheck('apple', "nonexitingfile.txt")
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()