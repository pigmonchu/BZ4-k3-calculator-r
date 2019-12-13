import unittest
from romannumber import RomanNumber

class RomanNumberTest(unittest.TestCase):

    def test_symbols_romans(self):
        self.assertEqual(int(RomanNumber('I')), 1)
        self.assertEqual(int(RomanNumber('V')), 5)
        self.assertEqual(int(RomanNumber('X')), 10)
        self.assertEqual(int(RomanNumber('L')), 50)
        self.assertEqual(int(RomanNumber('C')), 100)
        self.assertEqual(int(RomanNumber('D')), 500)
        self.assertEqual(int(RomanNumber('M')), 1000)

        with self.assertRaises(ValueError) as context:
            int(RomanNumber('A'))
        
        self.assertEqual('Simbolo incorrecto', str(context.exception))

    
    def test_numeros_crecientes(self):
        self.assertEqual(int(RomanNumber('XVI')), 16)
        self.assertEqual(int(RomanNumber('III')), 3)

    def test_no_mas_de_tres_repeticiones(self):
        self.assertEqual(int(RomanNumber('LXXIII')), 73)

        with self.assertRaises(ValueError) as context:
            int(RomanNumber('IIII'))
        self.assertEqual('Más de 3 repeticiones', str(context.exception))

        with self.assertRaises(ValueError) as context:
            int(RomanNumber('VVV'))
        self.assertEqual('Más de un valor de 5 repetido', str(context.exception))

    def test_numeros_decrecientes(self):
        self.assertEqual(int(RomanNumber('IX')), 9)
        self.assertEqual(int(RomanNumber('CMXCIX')), 999)
 
    def test_restas_no_admiten_repeticiones(self):
        with self.assertRaises(ValueError) as context:
            int(RomanNumber('MIIX'))
        
        self.assertEqual('No se admiten repeticiones en restas', str(context.exception))


    def test_restas_no_admiten_derivados_del_5(self):
        with self.assertRaises(ValueError) as context:
            int(RomanNumber('VC'))
        self.assertEqual('No se pueden restar valores de 5', str(context.exception))

    def test_restas_no_admiten_mas_de_un_orden_de_diferencia(self):
        with self.assertRaises(ValueError) as context:
            int(RomanNumber('IC'))
        self.assertEqual('Distancia en resta mayor de factor 2', str(context.exception))

        with self.assertRaises(ValueError) as context:
            int(RomanNumber('IL'))
        self.assertEqual('Distancia en resta mayor de factor 2', str(context.exception))

        with self.assertRaises(ValueError) as context:
            int(RomanNumber('VL'))  
        self.assertEqual('No se pueden restar valores de 5', str(context.exception))

    def test_numeros_mayores_de_3999(self):
        self.assertEqual(int(RomanNumber('(IV)')), 4000)
        self.assertEqual(int(RomanNumber('(VII)CMXXIII')), 7923)
        self.assertEqual(int(RomanNumber('((VII))(DLIII)DCXXXVII')), 7553637)

    def test_procesar_parentesis(self):
        self.assertEqual(RomanNumber('(IV)')._RomanNumber__contarParentesis(), [(1, 'IV')])
        self.assertEqual(RomanNumber('((VII))(XL)CCCXXII')._RomanNumber__contarParentesis(), [(2, 'VII'), (1, 'XL'), (0, 'CCCXXII')])

        with self.assertRaises(ValueError) as context:
            RomanNumber('(VI)((VII))')._RomanNumber__contarParentesis()
        self.assertEqual('Número de paréntesis incorrecto', str(context.exception))        
        
        with self.assertRaises(ValueError) as context:
            RomanNumber('(VI)((VII)')._RomanNumber__contarParentesis()
        self.assertEqual('Número de paréntesis incorrecto - Faltan cierres', str(context.exception))

        with self.assertRaises(ValueError) as context:
            RomanNumber('VI)((VII)')._RomanNumber__contarParentesis()
        self.assertEqual('Número de paréntesis incorrecto - Sobran cierres', str(context.exception))

class ArabicNumberTest(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(str(RomanNumber(1)), 'I')
        self.assertEqual(str(RomanNumber(2)), 'II')
        self.assertEqual(str(RomanNumber(4)), 'IV')

    def test_arabic_a_roman(self):
        self.assertEqual(str(RomanNumber(2123)), 'MMCXXIII')
        self.assertEqual(str(RomanNumber(2444)), 'MMCDXLIV')
        self.assertEqual(str(RomanNumber(3555)), 'MMMDLV')
        self.assertEqual(str(RomanNumber(1678)), 'MDCLXXVIII')
        self.assertEqual(str(RomanNumber(2999)), 'MMCMXCIX')

    def test_arabic_a_roman_gt_3999(self):
        self.assertEqual(str(RomanNumber(4000)), '(IV)')
        self.assertEqual(str(RomanNumber(7763147686)), '(((VII)))((DCCLX))(MMMCXLVII)DCLXXXVI')

    def test_gruposDe1000(self):
        self.assertEqual(RomanNumber(7763147686)._RomanNumber__gruposDeMil(), [[3, 7], [2, 760],[1, 3147], [0, 686]])
        self.assertEqual(RomanNumber(3763142686)._RomanNumber__gruposDeMil(), [[3, 0], [2, 3760],[1, 3140], [0, 2686]])


class TestsForCalculator(unittest.TestCase):
    def test_parentesis(self):
        with self.assertRaises(ValueError) as context:
            RomanNumber('(')
        self.assertEqual('Número de paréntesis incorrecto - Faltan cierres', str(context.exception))

        with self.assertRaises(ValueError) as context:
            RomanNumber('(()')
        self.assertEqual('Número de paréntesis incorrecto - Faltan cierres', str(context.exception))

        with self.assertRaises(ValueError) as context:
            RomanNumber('((())')
        self.assertEqual('Número de paréntesis incorrecto - Faltan cierres', str(context.exception))

        with self.assertRaises(ValueError) as context:
            RomanNumber('((()')
        self.assertEqual('Número de paréntesis incorrecto - Faltan cierres', str(context.exception))

        with self.assertRaises(ValueError) as context:
            RomanNumber('(IV))')
        self.assertEqual('Número de paréntesis incorrecto - Sobran cierres', str(context.exception))

        self.assertEqual(int(RomanNumber('()')), 0)



if __name__ == '__main__':
    unittest.main()