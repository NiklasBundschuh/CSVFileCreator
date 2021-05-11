from HeaderParser import HeaderParser

class HeaderGenerator:

    #def __init__(self):
        # constructor
        #self.reset(self)

    #def reset():
        # reset internal state
        #return

    def generate(self, headerDict, headerLines):
        keys = []
        values = []
        idx = 0
        headerStartData = []
        headerK = []
        headerS = []
        headerStartValues = []
        headerValuesK = []
        headerValuesS = []

        for i in headerDict.values():
            values.append(i)
        for e in headerDict.keys():
            keys.append(e)
        # generate common sedction




        while keys[idx] != 'K01':
            startIdx = 1
            headerStartData.append(keys[idx])
            headerStartValues.append(values[idx])
            idx += 1

        while len(headerStartData) != startIdx:
            headerLines.append(headerStartData[startIdx])
            headerLines.append(headerStartValues[startIdx])
            startIdx += 1

       

        # generate K section
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
        print(headerLines)
        #headerLines += generateKArraySection(headerDict)

        # generate S section
        keyCacheS = []
        valuesChacheS = []
        dataIdxS = 32
        lastIdxS = 0
        inputIdxS = 0

        if keys[idx] == "S0":
            while len(keys) == 520:
                headerS.append(keys[idx])
                headerValuesS.append(values[idx])
                idx += 1
                if idx == 520:
                    break

            while len(headerS) >= dataIdxS:
                keyCacheS.append(headerS[lastIdxS:dataIdxS])
                valuesChacheS.append(headerValuesS[lastIdxS:dataIdxS])
                lastIdxS += 33
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

        return headerLines


class FooterGenerator:
  
    def generate(self, footerDict, footerLines):
        keys = []
        idx = 0
        values = []
        footerStartData = []
        footerK = []
        footerS = []
        footerStartValues = []
        footerValuesK = []
        footerValuesS = []

        for i in footerDict.keys():
            keys.append(i)
        
        for e in footerDict.values():
            values.append(e)
        
        while keys[idx] != 'K01':
            startIdx = 1
            footerStartData.append(keys[idx])
            footerStartValues.append(values[idx])
            idx += 1

        while len(footerStartData) != startIdx:
            footerLines.append(footerStartData[startIdx])
            footerLines.append(footerStartValues[startIdx])
            startIdx += 1

        # generate K section

        keyCacheK = []
        valueCacheK = []
        lastIdxK = 0
        dataIdxK = 32
        inputIdxK = 0
        if keys[idx] == 'K01':
            while keys[idx] != "S0":
                footerK.append(keys[idx])
                footerValuesK.append(values[idx])
                idx += 1
            while len(footerK) >= dataIdxK:
                keyCacheK.append(footerK[lastIdxK:dataIdxK])
                valueCacheK.append(footerValuesK[lastIdxK:dataIdxK])
                dataIdxK += 32
                lastIdxK += 32
            while inputIdxK != 2:
                i = 0
                p = 0
                for e in keyCacheK[inputIdxK]:
                    footerLines.append(keyCacheK[inputIdxK][i]) 
                    i += 1
                for q in valueCacheK[inputIdxK]:
                    footerLines.append(valueCacheK[inputIdxK][p])
                    p += 1
                inputIdxK += 1
            
        # generate S section
        keyCacheS = []
        valuesChacheS = []
        dataIdxS = 32
        lastIdxS = 0
        inputIdxS = 0

        if keys[idx] == "S0":
            while len(keys) == 520:
                footerS.append(keys[idx])
                footerValuesS.append(values[idx])
                idx += 1
                if idx == 520:
                    break

            while len(footerS) >= dataIdxS:
                keyCacheS.append(footerS[lastIdxS:dataIdxS])
                valuesChacheS.append(footerValuesS[lastIdxS:dataIdxS])
                lastIdxS += 33
                dataIdxS += 32

            while inputIdxS != 14:
                i = 0
                p = 0
                for e in keyCacheS[inputIdxS]:
                    footerLines.append(keyCacheS[inputIdxS][i]) 
                    i += 1
                for q in valuesChacheS[inputIdxS]:
                    footerLines.append(valuesChacheS[inputIdxS][p])
                    p += 1
                inputIdxS += 1
            print(footerLines)

            return footerLines