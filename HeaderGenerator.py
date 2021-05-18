from typing import Dict
from HeaderParser import HeaderParser

class HeaderGenerator:
    
    def header(self, headerDict):
        Dict = headerDict
        self.generate(Dict)

        
    def footer(self, footerDict):
        Dict = footerDict
        self.generate(Dict)

    def generate(self, Dict):
        keys = []
        values = []
        headerLines = []
        idx = 0

        for i in Dict.values():
            values.append(i)
        for e in Dict.keys():
            keys.append(e)
        self.generateIsection(headerLines, idx, keys, values)

         
        # generate common sedction


    def generateIsection(self, headerLines, idx, keys, values):
        headerStartValues = []
        headerStartData = []
        while keys[idx] != 'K01':
            startIdx = 1
            headerStartData.append(keys[idx])
            headerStartValues.append(values[idx])
            idx += 1

        while len(headerStartData) != startIdx:
            headerLines.append(headerStartData[startIdx])
            headerLines.append(headerStartValues[startIdx])
            startIdx += 1
        self.generateKsection( headerLines, idx, keys, values)

      
    def generateKsection(self, headerLines, idx, keys, values):
        # generate K section
        headerValuesK = []
        headerK = []
        keyCacheK = []
        valueCacheK = []
        lastIdxK = 0
        dataIdxK = 32
        inputIdxK = 0
        if keys[idx] == 'K01':
            while keys[idx] != "S0":
                headerK.append(keys[idx])
                headerValuesK.append(values[idx])
                idx += 1
            while len(headerK) >= dataIdxK:
                keyCacheK.append(headerK[lastIdxK:dataIdxK])
                valueCacheK.append(headerValuesK[lastIdxK:dataIdxK])
                dataIdxK += 32
                lastIdxK += 32
            while inputIdxK != 2:
                i = 0
                p = 0
                for e in keyCacheK[inputIdxK]:
                    headerLines.append(keyCacheK[inputIdxK][i]) 
                    i += 1
                for q in valueCacheK[inputIdxK]:
                    headerLines.append(valueCacheK[inputIdxK][p])
                    p += 1
                inputIdxK += 1
        self.generateSsection(headerLines, idx, keys, values)
        


    def generateSsection(self, headerLines, idx, keys, values):
            # generate S section
            headerValuesS = []
            headerS = []
            keyCacheS = []
            valuesChacheS = []
            dataIdxS = 32
            lastIdxS = 0
            inputIdxS = 0
    
            if keys[idx] == "S0":
                while idx != 520:
                    headerS.append(keys[idx])
                    headerValuesS.append(values[idx])
                    idx += 1
                   
                    
                while len(headerS) >= dataIdxS:
                    keyCacheS.append(headerS[lastIdxS:dataIdxS])
                    valuesChacheS.append(headerValuesS[lastIdxS:dataIdxS])
                    lastIdxS += 32
                    dataIdxS += 32
    
                while inputIdxS != 14:
                    i = 0
                    p = 0
                    for e in keyCacheS[inputIdxS]:
                        headerLines.append(keyCacheS[inputIdxS][i]) 
                        i += 1
                    for q in valuesChacheS[inputIdxS]:
                        headerLines.append(valuesChacheS[inputIdxS][p])
                        p += 1
                    inputIdxS += 1
            print(headerLines)
            
    
    

