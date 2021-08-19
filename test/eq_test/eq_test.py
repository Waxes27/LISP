import unittest
from functions import eq


class TestCase(unittest.TestCase):

    def TestEqual(self):

        eq.Eq(self, '(eq 10 10)')
        self.assertEqual(eq.Eq(self,'(eq 10 10)'), ['True'])
        self.assertEqual(eq.Eq(self,'(eq a 10)'), ['()'])
        self.assertEqual(eq.Eq(self,'(eq 5 4)'), ['False'])



if __name__ == "__main__":
    unittest.main()
