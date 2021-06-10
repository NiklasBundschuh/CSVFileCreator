from DataGenerator import DataGenerator
from HeaderGenerator import HeaderGenerator
from CSVFileParser import CSVFileSeparatorKeys
import csv


def createCSVFile(headerDict, footerDict, dataList): 
    head = HeaderGenerator()
    data = DataGenerator()
    
    headerLines = head.generate(headerDict) 
    footerLines = head.generate(footerDict)
    dataLines = data.generate(dataList)

    writer = open("CopiedCSVa.csv", "w")
    try:
        writeLine(writer, CSVFileSeparatorKeys.HEADER_START)
        writeLines(writer, headerLines)
        writeLine(writer, CSVFileSeparatorKeys.HEADER_END)
        writer.flush()
        writeLine(writer, CSVFileSeparatorKeys.FOOTER_START)
        writeLines(writer, footerLines)
        writeLine(writer, CSVFileSeparatorKeys.FOOTER_END)

        writeLines(writer, dataLines)

        writer.close()
    except:
        writer.close()


def writeLine(writer, line):
    writer.write(line + "\n")

def writeLines(writer, lineList):
    for line in lineList:
        writeLine(writer, line)
 
