
from flask.globals import request
import json
from HeaderParser import HeaderParser
from DataParser import DataParser


class CSVFileSeparatorKeys:

    HEADER_START = "Kopfzeilen START"
    HEADER_END   = "Kopfzeilen ENDE"
    FOOTER_START = "Fusszeilen START"
    FOOTER_END   = "Fusszeilen ENDE"
    DATA_START   = "Zeittakt"

# decides wether a footer/header section starts/ends

def checkSectionTrigger(fileLine, headerState, footerState, dataState):
   




    # check the Header Start
    if fileLine[0:len(CSVFileSeparatorKeys.HEADER_START)] == CSVFileSeparatorKeys.HEADER_START:
        headerState = True
        fileLine = fileLine[len(CSVFileSeparatorKeys.HEADER_START):]
        
        

    # check the Header End
    elif fileLine[0:len(CSVFileSeparatorKeys.HEADER_END)] == CSVFileSeparatorKeys.HEADER_END:

        headerState = False
        fileLine = fileLine[len(CSVFileSeparatorKeys.HEADER_END):]
            
            
    # check the Footer Start
    elif fileLine[0:len(CSVFileSeparatorKeys.FOOTER_START)] == CSVFileSeparatorKeys.FOOTER_START:
        footerState = True
        fileLine = fileLine[len(CSVFileSeparatorKeys.FOOTER_START):]
    
        
    # check the Footer End
    elif fileLine[0:len(CSVFileSeparatorKeys.FOOTER_END)] == CSVFileSeparatorKeys.FOOTER_END:
        footerState = False
        fileLine = fileLine[len(CSVFileSeparatorKeys.FOOTER_END):]
        

    elif fileLine[0:len(CSVFileSeparatorKeys.DATA_START)] == CSVFileSeparatorKeys.DATA_START:
        dataState = True
        # don't remove trigger info    
    
    return fileLine, headerState, footerState, dataState,


def parseKeyValueFile(path):

        # create the variables
        headerSection = False
        footerSection = False
        dataSection = False
        head = HeaderParser()
        foot = HeaderParser()
        data = DataParser()
        headerDict = {}
        footerDict = {}
        dataList = []


        # open file and
        file = open(path, 'r')


        # go through all lines
        for line in file:


            # remove CR/LF
            line = line[:-1]
            
            

            # Check for Header Section
            line, headerSection, footerSection, dataSection = checkSectionTrigger(line, headerSection, footerSection, dataSection)
            
            if headerSection == True:
                head.parseHeaderLine(line, headerDict)

            # Check for Footer Section
            elif footerSection == True:
                foot.parseHeaderLine(line, footerDict)

            elif dataSection == True:
                data.parseDataLine(line, dataList)
                
        
        return headerDict, footerDict, dataList








