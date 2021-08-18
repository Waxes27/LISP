import unittest
from validation.validations import Validations

class ValidationTests(unittest.TestCase):
    def test_brackets_always_evaluated_properly(self):
        valid_exp_2 = "()"
        valid_exp_6 = "((()))"
        valid_exp_8 = "(()(()))"
        invalid_exp_3 = "())"
        invalid_exp_4 = "(((("
        invalid_exp_5 = "(+ (5 (+ 14 1))"

        self.assertTrue(Validations.isValidExpressionBrackets(valid_exp_2))
        self.assertTrue(Validations.isValidExpressionBrackets(valid_exp_6))
        self.assertTrue(Validations.isValidExpressionBrackets(valid_exp_8))
        self.assertFalse(Validations.isValidExpressionBrackets(invalid_exp_3))
        self.assertFalse(Validations.isValidExpressionBrackets(invalid_exp_4))
        self.assertFalse(Validations.isValidExpressionBrackets(invalid_exp_5))
        self.assertFalse(Validations.isValidExpressionBrackets("("))

    def test_quote_detected_properly(self):
        """Check if quote-only commands are consistently detected"""
        valid_quote_1 = "'1"
        valid_quote_brackets = "(quote wtc)"
        invalid_quote_1 = "1"
        invalid_quote_brackets = "(quot wtc)"

        self.assertTrue(Validations.isValidQuote(valid_quote_1))
        self.assertTrue(Validations.isValidQuote(valid_quote_brackets))
        self.assertFalse(Validations.isValidQuote(invalid_quote_1))
        self.assertFalse(Validations.isValidQuote(invalid_quote_brackets))


if __name__ == "__main__":
    unittest.main()
