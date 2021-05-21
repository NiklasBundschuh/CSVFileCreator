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
 

#-------------------------------------------
#    i = []
#    idx = 1
#    firstidx = 1
#    lastidx = 0
#    
#    with open ('CopiedCSV.csv', 'w', newline='') as copy:
#        writer = csv.writer(copy)
#
#        while headerLines[firstidx] and headerLines[lastidx] != 'K01':
#            i.append(str(headerLines[lastidx])  + ";" + str(headerLines[firstidx]))
#            writer.writerows([i])
#            i = []
#            idx += 1
#            lastidx += 2
#            firstidx += 2
#        firstidx -= 1
#
#        while headerLines[firstidx] != 'S0':
#            while len(i) != 32:
#                i.append(headerLines[firstidx])
#                firstidx += 1
#            writer.writerows([i])
#            i = []
#        
#        while firstidx != 1038:
#            while len(i) != 32:
#                i.append(headerLines[firstidx])
#                firstidx += 1
#            writer.writerows([i])
#            i = []
#
#        firstidx = 1
#        lastidx = 0
#
#        while footerLines[firstidx] and footerLines[lastidx] != 'K01':
#            i.append(str(footerLines[lastidx]) + ";" + str(footerLines[firstidx]))
#            writer.writerows([i])
#            i = []
#            idx += 1
#            lastidx += 2
#            firstidx += 2
#        firstidx -= 1
#
#        while footerLines[firstidx] != 'S0':
#            while len(i) != 32:
#                i.append(footerLines[firstidx])
#                firstidx += 1
#            writer.writerows([i])
#            i = []
#        
#        while firstidx != 822:
#            while len(i) != 32:
#                i.append(footerLines[firstidx])
#                firstidx += 1 
#            writer.writerows([i]) 
#            i = []
#-------------------------------------------
               
        
        
        #copy.close
    #return