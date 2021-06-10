import unittest
from HeaderParser import HeaderParser

class TestHeaderparser(unittest.TestCase):

    def test_headerKeyValueLineINTComma(self):
        gen = HeaderParser()
        key = "Vordruck"
        value = "97,33849"
        info = key + ";" + value
        hDict = {}
        gen.parseHeaderLine(info, hDict)
        self.assertEqual(list(hDict.keys())[0], key)
        self.assertEqual(hDict[key], 97.33849)

    def test_headerKeyValueLineINTDot(self):
        gen = HeaderParser()
        key = "AuftragSoll"
        value = "60.00"
        info = key + ";" + value
        hDict = {}
        gen.parseHeaderLine(info, hDict)
        self.assertEqual(list(hDict.keys())[0], key)
        self.assertEqual(hDict[key], 60.00)
       

    def test_headerKeyValueLineINT(self):
        gen = HeaderParser()
        key = "Gewicht"
        value = "53"
        info = key + ";" + value
        hDict = {}
        gen.parseHeaderLine(info, hDict)
        self.assertEqual(list(hDict.keys())[0], key)
        self.assertEqual(hDict[key], 53)
       
    
    def test_headerKeyValueLineTXT(self):
        gen = HeaderParser()
        key = "Begin"
        value = "23.07.2019 19:55:19;2019;07;23;19;55"
        info = key + ";" + value
        hDict = {}
        gen.parseHeaderLine(info, hDict)
        self.assertEqual(list(hDict.keys())[0], key)
        self.assertEqual(hDict[key], value)



if __name__ == '__main__':
    unittest.main()