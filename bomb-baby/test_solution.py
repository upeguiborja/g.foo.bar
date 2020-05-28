import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def testSolution1(self):
        self.assertEqual("1", solution("2", "1"))
    
    def testSolution2(self):
        self.assertEqual("4", solution("4", "7"))

    def testSolution3(self):
        self.assertEqual("impossible", solution("2", "4"))

    def testSolution4(self):
        self.assertEqual("impossible", solution("4", "2"))

    def testSolution5(self):
        self.assertEqual("impossible", solution("10", "10"))

if __name__ == "__main__":
    unittest.main()
