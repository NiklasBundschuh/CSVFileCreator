from CSVFileParser import parseKeyValueFile

def main():
    headerDict = {}
    footerDict = {}
    dataList = []

    headerDict, footerDict, dataList = parseKeyValueFile('text_2DateiÖffnen.csv')
    

if __name__ == '__main__':
    main()