import unittest
from validation import validations

class ValidationTests(unittest.TestCase):
    def test_brackets_always_evaluated_properly(self):
        valid_exp_2 = "()"
        valid_exp_6 = "((()))"
        valid_exp_8 = "(()(()))"
        invalid_exp_3 = "())"
        invalid_exp_4 = "(((("
        invalid_exp_5 = "(+ (5 (+ 14 1))"

        self.assertTrue(validations.isValidExpressionBrackets(valid_exp_2))
        self.assertTrue(validations.isValidExpressionBrackets(valid_exp_6))
        self.assertTrue(validations.isValidExpressionBrackets(valid_exp_8))
        self.assertFalse(validations.isValidExpressionBrackets(invalid_exp_3))
        self.assertFalse(validations.isValidExpressionBrackets(invalid_exp_4))
        self.assertFalse(validations.isValidExpressionBrackets(invalid_exp_5))
        self.assertFalse(validations.isValidExpressionBrackets("("))

    def test_quote_detected_properly(self):
        """Check if quote-only commands are consistently detected"""
        valid_quote_1 = "'1"
        valid_quote_brackets = "(quote wtc)"
        invalid_quote_1 = "1"
        invalid_quote_brackets = "(quot wtc)"

        self.assertTrue(validations.isValidQuote(valid_quote_1))
        self.assertTrue(validations.isValidQuote(valid_quote_brackets))
        self.assertFalse(validations.isValidQuote(invalid_quote_1))
        self.assertFalse(validations.isValidQuote(invalid_quote_brackets))


if __name__ == "__main__":
    unittest.main()
