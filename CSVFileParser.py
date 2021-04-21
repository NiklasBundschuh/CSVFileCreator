from flask.globals import request
import json
from HeaderParser import HeaderParser
from DataParser import DataParser
from DataChannel import DataChannel


# decides wether a footer/header section starts/ends

def checkSectionTrigger(fileLine, headerState, footerState, dataState):
    HEADER_START = "Kopfzeilen START"
    HEADER_END   = "Kopfzeilen ENDE"
    FOOTER_START = "Fusszeilen START"
    FOOTER_END   = "Fusszeilen ENDE"
    Data_Start = "Zeittakt"




    # check the Header Start
    if fileLine[0:len(HEADER_START)] == HEADER_START:
        headerState = True
        fileLine = fileLine[len(HEADER_START):]
        
           

    # check the Header End
    elif fileLine[0:len(HEADER_END)] == HEADER_END:

        headerState = False
        fileLine = fileLine[len(HEADER_END):]
               
            
    # check the Footer Start
    elif fileLine[0:len(FOOTER_START)] == FOOTER_START:
        footerState = True
        fileLine = fileLine[len(FOOTER_START):]
       
           
     # check the Footer End
    elif fileLine[0:len(FOOTER_END)] == FOOTER_END:
        footerState = False
        fileLine = fileLine[len(FOOTER_END):]
        

    elif fileLine[0:len(Data_Start)] == Data_Start:
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
            
    print("HeaderStart----------------------------------------------------------------------------")
    print(headerDict)
    print("HeaderEnd---------------------------------------------------------------------------------------")
    print("FooterStart---------------------------------------------------------------------------------------")
    print(footerDict)
    print("FooterEnd---------------------------------------------------------------------------------------")
    print("DataStart---------------------------------------------------------------------------------------")
    print(dataList[127].data())
    print("DataEnd---------------------------------------------------------------------------------------")
    return headerDict, footerDict, dataList









