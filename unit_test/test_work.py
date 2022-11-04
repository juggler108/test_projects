from work import *
import unittest

data = {'Smartphone': -251, 'Computer': 340, 'Tablet': 50, 'TV': 10}
lst = [1, 22, 333, 4444, 55555]


class TestWork(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_test_arr(self):
        self.assertEqual(type(test_arr(data)), tuple)

    def test_percent1(self):
        self.assertEqual(type(percent(lst)), list)

    def test_percent2(self):
        for i in percent(lst):
            with self.subTest(i=i):
                self.assertGreaterEqual(100, i)


if __name__ == '__main__':
    unittest.main()