import unittest
from DecimalGenerator import DecimalGenerator



class TestCSVWriter(unittest.TestCase):
    
    def test_Dotdelimiter(self):
        gen = DecimalGenerator()
        self.assertNotEqual(gen.setDotDelimiter("12,5"), "12.5")
    def test_CommaDelimiter(self):
        gen = DecimalGenerator
        self.assertNotEqual(gen.setCommaDelimiter(self, "3232.123"), "3232,123")
    #def test_getDelimiter(self):
        #gen = DecimalGenerator
        #self.assertEqual(gen.getDelimiter(self, "23,23"), "23.23")
    

if __name__ == '__main__':
    unittest.main()
