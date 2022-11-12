import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslatorMethods(unittest.TestCase):

    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(''), '')


    def test_e2f(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(''), '')

if __name__ == '__main__':
    unittest.main()