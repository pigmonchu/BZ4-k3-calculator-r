from unittest import TestCase, main

from tkinter import *
from tkinter import ttk
from calculator import Calculator, Selector, Display

class CalculatorTests(TestCase):
    def setUp(self):
        self.root = Tk()
        self.calc = Calculator(self.root)
        self.calc.grid(column=0, row=0)
        self.calc.wait_visibility()

    def tearDown(self):
        self.root.update()
        self.root.destroy()

    def testCalcHaveSelectorTipus(self):
        self.assertIsInstance(self.calc.children['sel'], Selector)

    def testCalcHaveDisplay(self):
        self.assertIsInstance(self.calc.children['disp'], Display)

    def testInitCalcIsRoman(self):
        self.assertEqual(self.calc.children['sel'].value.get(), 'R')
        self.assertEqual(self.calc.children['layoutRoman'].winfo_manager(), 'grid')
        self.assertEqual(self.calc.children['layoutArabic'].winfo_manager(), '')
        self.calc.children['sel'].value.set('A')
        self.assertEqual(self.calc.children['layoutRoman'].winfo_manager(), '')
        self.assertEqual(self.calc.children['layoutArabic'].winfo_manager(), 'grid')
        
    



if __name__ == '__main__':
    main()