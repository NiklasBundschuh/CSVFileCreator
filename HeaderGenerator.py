from DecimalGenerator import DecimalGenerator
from typing import Dict
from HeaderParser import HeaderParser

class HeaderGenerator:
    def __init__(self):
        self.__decimator = DecimalGenerator()
        self.__decimator.setCommaDelimiter()

    def generate(self, myDict):
        # generate common section
        headerLines  = self.generateCommonSection(myDict)
        headerLines += self.generateKSection(myDict)
        headerLines += self.generateSSection(myDict)
        return headerLines

    def generateCommonSection(self, hDict):
        sectionLines = []
        
        return sectionLines

    def generateKSection(self, hDict):
        sectionLines  = self.generateDoubleLine(hDict, "K", 1, 0)
        sectionLines += self.generateDoubleLine(hDict, "K", 33, 0)
        return sectionLines

    def generateSSection(self, hDict):
        sectionLines = []
        startIdx = 0
        idx = 0
        while idx < 14:
            sectionLines += self.generateDoubleLine(hDict, "S", startIdx, startIdx)
            idx += 1
            startIdx += 32

        return sectionLines

    def generateDoubleLine(self, hDict, prefix, startIdx, keyOffset):
        doubleLine = ["", ""]
        idx = 0
        while idx < 32:
            key = prefix + "{:02d}".format(startIdx + idx)
            doubleLine[0] += prefix + "{:02d}".format(startIdx - keyOffset + idx) + ";"
            doubleLine[1] += self.__decimator.generate(hDict[key]) + ";"
            idx += 1
            


        return doubleLine
