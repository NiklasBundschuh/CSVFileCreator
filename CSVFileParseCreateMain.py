from CSVFileGenerator import createCSVFile
from DataGenerator import DataGenerator
from HeaderGenerator import  HeaderGenerator
from CSVFileParser import parseKeyValueFile

def main():
    headerDict = {}
    footerDict = {}
    dataList = []

    
   
    headerDict, footerDict, dataList = parseKeyValueFile('text_2DateiÖffnen.csv')
    createCSVFile(headerDict, footerDict, dataList)

if __name__ == '__main__':
    main()