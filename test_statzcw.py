import unittest
import statzcw


class StatzcwTest(unittest.TestCase):

    def test_zcount(self):
        list_in = [0, 1, 2, 3, 4, 5]
        expected_out = 6
        actual_out = statzcw.zcount(list_in)
        self.assertEqual(expected_out, actual_out)

    def test_zmean(self):
        list_in = [0, 1, 2, 3, 4, 5]
        expected_out = 2.5
        actual_out = statzcw.zmean(list_in)
        self.assertEqual(expected_out, actual_out)

    def test_zmode(self):
        list_in = [0, 1, 2, 2, 5, 5]
        expected_out = {2, 5}
        actual_out = statzcw.zmode(list_in)
        self.assertEqual(expected_out, actual_out)

    def test_zmode1(self):
        list_in = [0, 1, 2, 3, 4, 5]
        expected_out = set()
        actual_out = statzcw.zmode(list_in)
        self.assertEqual(expected_out, actual_out)

    def test_zmedian(self):
        list_in = [5, 4, 4, 1, 3]
        expected_out = 4
        actual_out = statzcw.zmedian(list_in)
        self.assertEqual(expected_out, actual_out)

    def test_zmedian1(self):
        list_in = [5, 4, 4, 1, 3, 2]
        expected_out = 3.5
        actual_out = statzcw.zmedian(list_in)
        self.assertEqual(expected_out, actual_out)
