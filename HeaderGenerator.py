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
        headerKValues = []
        headerSValues = []

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

        #headerLines += generateCommonSection(headerDict)

        # generate K section
        if keys[idx] == 'K01':
            dataKIdx = 32
            lastIdxK = 0
        while keys[idx] != "S0":
            headerK.append(keys[idx])
            headerKValues.append(values[idx])
            idx += 1
        while len(headerK) >= dataKIdx:
            headerLines.append(headerK[lastIdxK:dataKIdx])
            headerLines.append(headerKValues[lastIdxK:dataKIdx])
            dataKIdx += 32
            lastIdxK += 32

        #headerLines += generateKArraySection(headerDict)

        # generate S section
        hh = []
        i = 0
        p = 0
        l = []
        if keys[idx] == "S0":
            dataSIdx = 32
            lastIdxS = 0
            inputIdx = 0
        while len(keys) >= idx:
            headerS.append(keys[idx])
            headerSValues.append(values[idx])
            idx += 1
            if idx == 520:
                break
        while len(headerS) >= dataSIdx:
            hh.append(headerS[lastIdxS:dataSIdx])
            l.append(headerSValues[lastIdxS:dataSIdx])
            for e in hh[inputIdx]:
                headerLines.append(hh[inputIdx][i])
                i += 1
            
            for q in l[inputIdx]:
                headerLines.append(l[inputIdx][p])
                p += 1
            inputIdx += 1
            lastIdxK += 32
            dataSIdx += 32
        print(headerLines)   

            
            
            #hh.append(headerSValues[lastIdxS:dataSIdx])
            #for e in hh[inputIdx]:
                #headerLines.append(hh[inputIdx])
                #inputIdx += 1
            #inputIdx = 0
            #dataSIdx += 1
            #if dataSIdx == lastIdxS():
                #dataSIdx += 32
                #lastIdxS += 32
        #headerLines += generateSArraySection(headerDict)
        #print(headerLines)
        
        return headerLines
#class FooterGenerator:



    
def FooterGenerator(footerDict, FooterStart, FooterDataK, FooterDataS):
    keys = []
    idx = 0
    values = []
    FooterStartData = []
    FooterK = []
    FooterS = []
    FooterStartValues = []
    FooterKValues = []
    FooterSValues = []

    for i in footerDict.keys():
        keys.append(i)
    
    for e in footerDict.values():
        values.append(e)
    
    while keys[idx] != 'K01':
        startIdx = 1
        FooterStartData.append(keys[idx])
        FooterStartValues.append(values[idx])
        idx += 1

    while len(FooterStartData) != startIdx:
        FooterStart.append(FooterStartData[startIdx])
        FooterStart.append(FooterStartValues[startIdx])
        startIdx += 1

    if keys[idx] == 'K01':
        dataKIdx = 0
        while keys[idx] != "S0":
            FooterDataK.append(keys[idx] + values[idx])
            idx += 1
        while len(FooterK) >= dataKIdx:
            FooterDataK.append(FooterK[:dataKIdx])
            FooterDataK.append(FooterKValues[:dataKIdx])
            dataKIdx += 32
        

    if keys[idx] == "S0":
        dataSIdx = 0
        while len(keys) >= idx:
            FooterDataS.append(keys[idx] + str(values[idx]))
            idx += 1
            if idx == 520:
                break
        while len(FooterS) >= dataKIdx:
            FooterDataS.append(FooterS[:dataSIdx])
            FooterDataS.append(FooterSValues[:dataSIdx])
            dataSIdx += 32
        
    return footerDict, FooterStart, FooterDataK, FooterDataS