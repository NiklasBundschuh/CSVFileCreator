from DataGenerator import DataGenerator
from HeaderGenerator import FooterGenerator, HeaderGenerator
import csv


def CreateCSVFile(headerDict, footerDict, dataList): 
    headerLines = []
    head = HeaderGenerator()
    #foot = FooterGenerator()
    #data = DataGenerator(dataList,)

    head.generate(headerDict, headerLines) 
    #writer.writerows([headerlines])

    #head.generate(footerDict)
    #writer.writerows([footerlines])

    #datalines =  data.generate(dataList)
    #writer.writerows([datalines])
    i = []
    for e in headerLines:
        
        i.append(str(e) +'\n')
    
    
    
    with open ('CopiedCSV.csv', 'w', newline='') as copy:
        writer = csv.writer(copy)
        writer.writerows([i])
        copy.close
    return headerDict, footerDict, dataList