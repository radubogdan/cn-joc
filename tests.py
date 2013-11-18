"""
Desciption: Test file for main
Name: tests.py
"""

import unittest
from main import *

class TestSuiteHelperFunctions(unittest.TestCase):
    def setUp(self):
        pass

    def test1_hasUniqueDigits(self):
        self.assertEqual(hasUniqueDigits('1234'), 1234)
    def test2_hasUniqueDigits(self):
        self.assertEqual(hasUniqueDigits('2234'), None)

    def test1_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 5678), '0 [C]  |  0 [N]')
    def test2_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 2678), '0 [C]  |  1 [N]')
    def test3_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 2186), '0 [C]  |  2 [N]')
    def test4_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 2146), '0 [C]  |  3 [N]')
    def test5_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 4321), '0 [C]  |  4 [N]')
    def test6_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 1678), '1 [C]  |  0 [N]')
    def test7_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 5246), '1 [C]  |  1 [N]')
    def test8_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 5241), '1 [C]  |  2 [N]')
    def test9_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 4213), '1 [C]  |  3 [N]')
    def test10_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 1784), '2 [C]  |  0 [N]')
    def test11_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 1384), '2 [C]  |  1 [N]')
    def test12_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 1324), '2 [C]  |  2 [N]')
    def test13_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 1284), '3 [C]  |  0 [N]')
    def test14_outputStatusOfGame(self):
        self.assertEqual(outputStatusOfGame(1234, 1234), '4 [C]  |  0 [N]')

if __name__ == '__main__':
    unittest.main()
