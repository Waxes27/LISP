import unittest
from functions import cdr


class CdrTests(unittest.TestCase):
    def testSimpleCdr(self):
        self.assertEqual(cdr.Cdr.do(self,
        "(cdr '(3 5 6 8))"),['5','6','8'])

    def testSimpleCdrWithList(self):
        self.assertEqual(cdr.Cdr.do(self,
        "(cdr ((6 9)(5 4)(7 9))"),['(5 4)','(7 9)'])
    
    def testComplexCdr(self):
        self.assertEqual(cdr.Cdr.do(self,
        "(cdr (cdr '(1 2 3 4 5 6)))"),['3','4','5','6'])
    
    def testComplexCdrList(self):
        self.assertEqual(cdr.Cdr.do(self,
        "(cdr (cdr '((1 2) (3 4) (5 6) (7 8) (9 10))))"),['(5 6)','(7 8)','(9 10)'])


