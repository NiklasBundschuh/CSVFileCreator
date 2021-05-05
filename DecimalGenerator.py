
import re
class DecimalGenerator:
    def __init__(self, ):
        # constants
        self.__CONST_DECIMAL_DELIMTER_DOT = 0
        self.__CONST_DECIMAL_DELIMTER_COMMA = 1
       
        

    def setCommaDelimiter(self, number):
        i = (number)
        comma = i.replace(".", ",")
        return

        

    def setDotDelimiter(self, number):
        e = (number)
        dotted = e.replace(",", ".")
        return 


    def getDelimiter(self, number):
        idx = 0
        innerIdx = 0
        list = []
        list.append(str(number))
        while len(list) >= idx:
            finder = list[idx][innerIdx]
            if finder == ",":

                self.__delimiter = self.__CONST_DECIMAL_DELIMTER_DOT
                idx += 1
            elif finder == ".":
                self.__delimiter = self.__CONST_DECIMAL_DELIMTER_COMMA
                idx += 1
            else:
                innerIdx +=1
                
            
        if self.__delimiter == self.__CONST_DECIMAL_DELIMTER_COMMA:
            self.setCommaDelimiter(self, number)

        elif self.__delimiter == self.__CONST_DECIMAL_DELIMTER_DOT:
            self.setDotDelimiter(self, number)

        return self.__delimiter, number



    def generate(number):
        text = str(number)
        
        return text
def main():
    number = 234.3
    number = DecimalGenerator.getDelimiter(number)

        

if __name__ == '__main__':
    main()