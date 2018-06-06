'''
This is an python testing tutorials package that was created for learning purposes
'''
import unittest
from packaging import version

class TestFloatStrings(unittest.TestCase):
    '''This is a float string testing testcase'''

    def test_equal(self):
        '''This is used for testing equal string floats'''
        self.assertEqual('0.1', '0.1')

    def test_greater(self):
        '''This is used for testing greater string floats'''
        self.assertGreater('0.2', '0.1')

    def test_lesser(self):
        '''This is used for testing lesser string floats'''
        self.assertLess('0.1', '0.2')

class TestVersionStrings(unittest.TestCase):
    '''This is a version string testing testcase'''

    def test_equal_versions(self):
        '''This is used for testing equal string versions'''
        v_1 = version.parse("0.1")
        v_2 = version.parse("0.1")
        self.assertEqual(v_1, v_2)

    def test_greater_versions(self):
        '''This is used for testing greater string versions'''
        v_1 = version.parse("0.2")
        v_2 = version.parse("0.1")
        self.assertGreater(v_1, v_2)

    def test_lesser_versions(self):
        '''This is used for testing lesser string versions'''
        v_1 = version.parse("0.2")
        v_2 = version.parse("0.10")
        self.assertLess(v_1, v_2)
