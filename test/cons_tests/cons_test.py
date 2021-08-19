import unittest
from functions import cons


class ConsTests(unittest.TestCase):
    def testSimpleCons(self):
        cons.Cons.counter(self, '(cons 3)')

        self.assertEqual(cons.Cons.counter(self, '(cons 3)'), ['3'])
        self.assertEqual(cons.Cons.counter(self, '(cons 3 (cons 4))'), ['3', '4'])
        self.assertEqual(cons.Cons.counter(self, "(cons 'eyes '(ears nose))	"), ['eyes', 'ears', 'nose'])
        self.assertEqual(cons.Cons.counter(self, "(cons '1 (cons '2 (cons '3 '()))) "), ['1', '2', '3'])
        self.assertEqual(cons.Cons.counter(self, '(cons 3 (cons eyes crossed (cons the road))'),
                         ['3', 'eyes', 'crossed', 'the', 'road'])


if __name__ == "__main__":
    unittest.main()
