import unittest

from unittest.mock import patch
from main import evaluator as eval


class Test_Eval(unittest.TestCase):
    def test_evals(self):
        # self.assertEqual(eval('hi'),'hi')
        # self.assertEqual(eval("'10"),"10")
        
        self.assertEqual(eval("(cons 'eyes '(ears nose))"),['eyes', 'ears'])

    def maths(self):
        self.assertEqual(eval("(+ 5 17 33)"),"55")
        self.assertEqual(eval("(* 2 4)"),"8")
        self.assertEqual(eval("(- 10 5)"),"5")
        self.assertEqual(eval("(/ 20 10)"),"2")
        self.assertEqual(eval("(* (+ 3 2) (- 10 (/ 6 3)))"),"40")
        

        

if __name__ == "__main__":
    unittest.main()
