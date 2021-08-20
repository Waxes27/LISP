import unittest
from unittest.main import main
from functions import quote

class QouteExpressiontTest(unittest.TestCase):
    
    def test_quoteWord(self):
        qoute = quote.Quote('`10')
        self.assertEqual(qoute.IsQoute('`10'),True)
        self.assertEqual(qoute.IsQoute('(quote 10)'),True)
        self.assertEqual(qoute.IsQoute('(quote Testing)'),True)
        self.assertEqual(qoute.IsQoute('`lwanele'),True)

        self.assertEqual(qoute.IsQoute('"10'),False)
        self.assertEqual(qoute.IsQoute('(10 quote)'),False)
        self.assertEqual(qoute.IsQoute('(quo Testing)'),False)
        self.assertEqual(qoute.IsQoute('lwanele'),False)


      
    if __name__ == "___main__":
        unittest.main()


    