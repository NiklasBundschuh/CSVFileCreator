from DataParser import DataParser


class DataGenerator:
    def generate(self, dataList):
        dataLines = []
        cache = []
        rowIdx = 0
        itemIdx = 0
        while len(dataList) >= itemIdx:
            if rowIdx == 128:
                itemIdx += 1
                rowIdx = 0
            cache.append(dataList[rowIdx].data())
            dataLines.append(cache[0][itemIdx])
            cache = []
            rowIdx += 1
        print(dataLines)
        return dataLines
        
   
    
    