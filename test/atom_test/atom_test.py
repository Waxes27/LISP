import unittest
from functions import atom


class TestCase(unittest.TestCase):

    def TestAtom(self):

       
        self.assertEqual(atom.Atom(self,'(atom 10)'), ['T'])
        self.assertEqual(atom.Atom(self,'(atom a)', )['T'])
        self.assertEqual(atom.Atom(self,'(eq !)'), ['T'])



if __name__ == "__main__":
    unittest.main()
