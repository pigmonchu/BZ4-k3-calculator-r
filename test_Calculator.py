from unittest import TestCase, main
from calculator import openParenthesis

class TestFunctionsCalc(TestCase):

    def test_contar_parentesis(self):
        self.assertEqual(openParenthesis('()'), 0)
        self.assertEqual(openParenthesis('(((VI))'), 1)
        self.assertEqual(openParenthesis('((VI))(('),2)

if __name__ == '__main__':
    main()