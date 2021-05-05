from DataParser import DataParser

def DataGenerator(dataList, DataCSV):
    cache = []
    rowIdx = 0
    itemIdx = 0
    while len(dataList) >= itemIdx:
        if rowIdx == 128:
            itemIdx += 1
            rowIdx = 0
        cache.append(dataList[rowIdx].data())
        DataCSV.append(cache[0][itemIdx])
        cache = []
        rowIdx += 1
    return DataCSV, dataList
    
   
    
    