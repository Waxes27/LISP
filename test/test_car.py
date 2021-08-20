import unittest

class TestSuite(unittest.TestCase):

    def test_car(self):

        print("Tests Running   .....")

        testList = [1, 2, 3, 4, 5]
        self.assertEqual(testList[0], 1)


    def test_failling(self):
        testList = [1, 2, 3, 4, 5]
        self.assertNotEqual(testList[0], 3)


    def test_list_inside_list(self):
        testList = ([("kas","jga;s", 25), "khdjlgdadkha", 23, " "])
        self.assertEqual(testList[0], ("kas","jga;s", 25))



if __name__=="main":
    unittest.TestCase()
