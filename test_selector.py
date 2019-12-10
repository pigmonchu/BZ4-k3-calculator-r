from unittest import TestCase, main

from tkinter import *
from tkinter import ttk
from calculator import Calculator, Selector, Display

class SelectorTests(TestCase):
    def setUp(self):
        self.root = Tk()
        self.sel = Selector(self.root)
        self.sel.grid(column=0, row=0)
        self.sel.wait_visibility()

    def test_selectorOptionR(self):
        optionR = self.sel.children['optR']
        self.assertIsInstance(optionR, ttk.Radiobutton)
        self.assertEqual(optionR.config('text')[4], 'R')


    def tearDown(self):
        self.root.update()
        self.root.destroy()


if __name__ == '__main__':
    main()