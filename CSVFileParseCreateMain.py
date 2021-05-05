from CSVFileGenerator import CreateCSVFile
from DataGenerator import DataGenerator
from HeaderGenerator import FooterGenerator, HeaderGenerator
from CSVFileParser import parseKeyValueFile

def main():
    headerDict = {}
    footerDict = {}
    dataList = []

    
   
    headerDict, footerDict, dataList = parseKeyValueFile('text_2DateiÖffnen.csv')
    headerDict, footerDict, dataList= CreateCSVFile(headerDict, footerDict, dataList)

if __name__ == '__main__':
    main()