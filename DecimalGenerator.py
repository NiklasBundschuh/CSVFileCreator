
import re
from decimal import *

class DecimalGenerator:
    def __init__(self):
        # constants
        self.__CONST_DECIMAL_DELIMTER_DOT = 0
        self.__CONST_DECIMAL_DELIMTER_COMMA = 1

        self.__delimiter = self.__CONST_DECIMAL_DELIMTER_DOT
        return
        

    def setCommaDelimiter(self):
        self.__delimiter = self.__CONST_DECIMAL_DELIMTER_COMMA
        return

    def setDotDelimiter(self):
        self.__delimiter = self.__CONST_DECIMAL_DELIMTER_DOT
        return 


    def getDelimiter(self):
        return self.__delimiter

    def generate(self, number):
        text = str(number)
        
        if self.__delimiter == self.__CONST_DECIMAL_DELIMTER_COMMA:
            pos = text.find(".")
            if pos != -1:
                text = text[:pos] + "," + text[pos + 1:]

        return text
    
