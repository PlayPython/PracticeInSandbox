import unittest
import requests
from aDong import count_words_in_a_file as COUNT


class MyTestCase(unittest.TestCase):
    def Test_count_words(self):
        with open('test.txt', 'w+') as f:
            f.write("How to write a pythonic program\nI don't know")
        test_obj = COUNT.CountWord('test.txt')
        self.assertEqual(test_obj.count_words_sum(), 9)

        test_obj = COUNT.CountWord('test2.txt')
        self.assertTrue(isinstance(test_obj.count_words_sum(), int))

        # self.assertEqual(True, False)





if __name__ == '__main__':
    unittest.main()
