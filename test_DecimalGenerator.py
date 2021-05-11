import unittest
from DecimalGenerator import DecimalGenerator



class TestCSVWriter(unittest.TestCase):
    #def __init__(self):
        #self.dot = 0 
        #self.comma = 1
        

    def test_Constructor(self):
        gen = DecimalGenerator()
        self.assertEqual(gen.getDelimiter(), 0)
    
        # number with Comma
    def test_Dotdelimiter(self):
        gen = DecimalGenerator()
        gen.setDotDelimiter()
        self.assertEqual(gen.getDelimiter(), 0)

        # number with Dot
    def test_CommaDelimiter(self):
        gen = DecimalGenerator()
        gen.setCommaDelimiter()
        self.assertEqual(gen.getDelimiter(), 1)


    def test_generatePositiveDotDelimiter(self):
        gen = DecimalGenerator()
        self.assertEqual(gen.getDelimiter(), 0)

        number = 2.3
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "2.3")




    def test_generateNegativeDotDelimiter(self):
        gen = DecimalGenerator()
        self.assertEqual(gen.getDelimiter(), 0)

        number = -2.3
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "-2.3")

  
######

    def test_generateIntegerDotDelimiter(self):
        gen = DecimalGenerator()
        self.assertEqual(gen.getDelimiter(), 0)

        number = 2.0
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "2.0")


        number = -2.0
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "-2.0")

 
#####

    def test_generateZeroDotDelimiter(self):
        gen = DecimalGenerator()
        self.assertEqual(gen.getDelimiter(), 0)

        number = 4.7
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "4.7")








    def test_generatePositiveCommaDelimiter(self):
        gen = DecimalGenerator()
        gen.setCommaDelimiter()
        self.assertEqual(gen.getDelimiter(), 1)

        number = 2.3
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "2,3")

 
########

    def test_generateNegativeCommaDelimiter(self):
        gen = DecimalGenerator()
        gen.setCommaDelimiter()

        number = -2.3
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "-2,3")


######

    def test_generateIntegerCommaDelimiter(self):
        gen = DecimalGenerator()
        gen.setCommaDelimiter()

        number = 2.0
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "2,0")



        number = -2.0
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "-2,0")


####

    def test_generateZeroCommaDelimiter(self):
        gen = DecimalGenerator()
        gen.setCommaDelimiter()

        number = 4.7
        text = gen.generate(number)
        self.assertEqual(gen.generate(number), "4,7")


#####

if __name__ == '__main__':
    unittest.main()
