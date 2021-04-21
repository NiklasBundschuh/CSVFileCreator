from DataChannel import DataChannel

class DataParser:


    def __init__(self):

        # constructor
        self.__title = ""
        self.__unitValue = 1
        self.__unit = "s"

    def title(self):
        return self.__title

    def unit(self):
        return self.__unit

    def unitValue(self):
        return self.__unitValue


    # Split the unit
    def unitsplitter(self, fileline):

        # find the indexes
        semicolonIndex = fileline.find(';')
        openBracketIndex = fileline.find("[")
        closeBracketIndex = fileline.find("]")
    	
        currIntIdx = 0
        lastIntIdx = 0

        while currIntIdx < len(fileline):
            item = fileline[currIntIdx]
            if item.isdigit():
                lastIntIdx = currIntIdx
                currIntIdx += 1
                break
            currIntIdx += 1
        
        while currIntIdx < len(fileline):
            item = fileline[currIntIdx]
            if item.isdigit():
                currIntIdx += 1
            else:
                break

        if semicolonIndex == -1:
            return      



        self.__unit = fileline[openBracketIndex +1:closeBracketIndex]
        self.__unitValue = int(fileline[lastIntIdx:currIntIdx])
        print(self.__unitValue)




    # parse the Data Line
    def parseDataLine(self, fileline, dataList):
        #check if we can set the unit
        if fileline == "[ms];1000":
            self.unitsplitter(fileline)
            return
      
        # check if we are really in data lines
        elif fileline[0:1].isdigit() == False:
            return
        
        #
        valueList = self.splitLineToValueList(fileline, ";")
        
        #
        self.appendToDataChannel(valueList, dataList)

    def splitLineToValueList(self, fileline, separator):
        #parse data in line
        valueList = []
        currIdx = 0
        lastIdx = 0
        while currIdx < len(fileline):
            item = fileline[currIdx]
            if item == separator:
                # add value to 
                valueList.append(fileline[lastIdx:currIdx])
                lastIdx = currIdx + 1

            currIdx += 1

        return valueList

    def appendToDataChannel(self, valueList, dataList):
        # data are in list
        # append them to data-channels
        dataIdx = 0
        addDataChannels = False
        if len(dataList) == 0:
            addDataChannels = True
        

        for valueText in valueList:
            # exist the datachannel? 
            if addDataChannels:
                # add data-channel instance to data-list
                dataChannel = DataChannel()
                dataChannel.setTitle("Channel " + str(len(dataList)+1))
                dataList.append(dataChannel)
            
            valueText = self.checkAndReplaceComma(valueText)
            value = float(valueText)

            # add value to data-channel
            dataList[dataIdx].append(value)
            dataIdx += 1


    def checkAndReplaceComma(self, valueText):
        # convert string to value
        commaIdx = valueText.find(',')

        if commaIdx != -1:
            # replace comma with dot
            valueText = valueText[0:commaIdx] + "." + valueText[commaIdx+1:]

        return valueText        


        