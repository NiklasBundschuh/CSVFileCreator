from DataParser import DataParser
from DecimalGenerator import DecimalGenerator



class DataGenerator:

    def __init__(self):
        self.__decimator = DecimalGenerator()
        self.__decimator.setCommaDelimiter()

    def generate(self, myData):
        # generate first line
        dataLines  = self.generateSamplerateSection(myData)
        dataLines += self.generateDataSection(myData)
        return dataLines

    def generateSamplerateSection(self, myData):
        dataLines = ["Zeittakt"]
        if len(myData) > 0:
            dataLines.append("[" + myData[0].unit() + "];{:d}".format(myData[0].unitValue()))
        else:
            dataLines.append("[ms];1000")
        return dataLines

    def generateDataSection(self, myData):
        if len(myData) == 0:
            return [""]

        dataLines = []
        lineIdx = 0
        lineMax = myData[0].dataLength()
        while lineIdx < lineMax:
            dataLines.append(self.generateDataLine(myData, lineIdx))
            lineIdx += 1
        return dataLines

    def generateDataLine(self, myData, lineIdx):
        dataLine = ""
        for dataChannel in myData:
            dataLine += self.__decimator.generate(dataChannel.data()[lineIdx]) + ";"
        return dataLine

    
   
    
    