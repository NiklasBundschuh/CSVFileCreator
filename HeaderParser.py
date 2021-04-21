
class HeaderParser:

    def __init__(self):
                                 
        # constructor
        
        # constants
        self.__CONST_HEADER_STATE_KEY_VALUE = 0
        self.__CONST_HEADER_STATE_TABLE_KEY = 1
        self.__CONST_HEADER_STATE_TABLE_VALUE = 2
        
        # properties
        self.reset()

    def reset(self):
        self.__tableState = self.__CONST_HEADER_STATE_KEY_VALUE
        self.__lastKeys = []


    def parseHeaderLine(self, fileLine, headDict):
        #print("Header parser modul")
        
        prevState = self.__tableState
        self.__checkHeaderLineState(fileLine)
        
        # handle error in format:
        # two key-lines consecutive --> add value-line with zeros
        if self.__tableState == prevState and prevState == self.__CONST_HEADER_STATE_TABLE_KEY:
            values = [0] * 32
            self.__addTableKeyValues(headDict, values)


        # key-value part
        if self.__tableState == self.__CONST_HEADER_STATE_KEY_VALUE:      
            self.__parseHeaderKeyValueLine(fileLine, headDict)

        elif self.__tableState == self.__CONST_HEADER_STATE_TABLE_KEY:
            self.__lastKeys = self.__parseHeaderTableKeyLine(fileLine)

        elif self.__tableState == self.__CONST_HEADER_STATE_TABLE_VALUE:
            values = self.__parseHeaderTableValueLine(fileLine)

            # added lastKeys and values to dictionary
            self.__addTableKeyValues(headDict, values)


        

    # --------------------------------------------------------------------------------

                                # Pivate methods



     # check Values and Keys
    def __checkHeaderLineState(self, fileLine):


        # check Keys
        if fileLine[0:3] == "K01":
            self.__tableState = self.__CONST_HEADER_STATE_TABLE_KEY

        elif fileLine[0:3] == "K33":
            self.__tableState = self.__CONST_HEADER_STATE_TABLE_KEY

        elif fileLine[0:1] == "S":
           self.__tableState = self.__CONST_HEADER_STATE_TABLE_KEY


        # check Values
        elif self.__tableState == self.__CONST_HEADER_STATE_TABLE_KEY:
            self.__tableState = self.__CONST_HEADER_STATE_TABLE_VALUE


        # check Values and Keys (path)
        else:
            self.__tableState = self.__CONST_HEADER_STATE_KEY_VALUE
        
        


    # split function from path
    def __parseHeaderKeyValueLine(self, fileLine, dict):
        key = ""
        value = ""
        lastIdx = 0
        currIdx = 0
        while currIdx < len(fileLine):
            item = fileLine[currIdx]
            if item == ";":
                if lastIdx < currIdx:
                    key = fileLine[lastIdx:currIdx]
                    lastIdx = currIdx +1
                    break

            currIdx += 1

        if lastIdx > currIdx:
            value=fileLine[lastIdx:]

        dict[key] = value




    # split function from Keys
    def __parseHeaderTableKeyLine(self, fileLine):
        keys = []
        lastIdx = 0
        currIdx = 0
        while currIdx < len(fileLine):
            item = fileLine[currIdx]
            if item == ";":
                if lastIdx < currIdx:
                    keys.append(fileLine[lastIdx:currIdx])
                    
                lastIdx = currIdx +1
            currIdx += 1
                    

        if lastIdx < currIdx:
            keys.append(fileLine[lastIdx:currIdx])
        return keys




    # split function from Values
    def __parseHeaderTableValueLine(self, fileLine):
        values = []
        lastIdx = 0
        currIdx = 0
        while currIdx < len(fileLine):
            item = fileLine[currIdx]
            if item == ";":
                if lastIdx < currIdx:
                    values.append(fileLine[lastIdx:currIdx])

                lastIdx = currIdx +1
            currIdx += 1
                    

        if lastIdx < currIdx:
            values.append(fileLine[lastIdx:currIdx])
        return values




    # Get the next Key index
    def __getNextSKeyIndex(self, keys):
        maxIdx = -1
        for item in keys:
            if len(item) > 0 and item[0] ==  "S":
                sIdx = int(item[1:])
                maxIdx = max(maxIdx, sIdx)
        return maxIdx + 1




    # Change the Key indecies
    def __adaptSKeyIndicies(self, sIdx):
        idx = 0
        while idx < len(self.__lastKeys):
            self.__lastKeys[idx] = "S" + str(sIdx)
            sIdx += 1
            idx += 1




    # add the Key and Values to the Dict
    def __addTableKeyValues(self, headDict, values):
        # if SXX already exists, find next free index
        if self.__lastKeys[0][0] == "S":
            sIdx = self.__getNextSKeyIndex(headDict.keys())
            self.__adaptSKeyIndicies(sIdx)

        keyValCount = min(len(self.__lastKeys), len(values))
        idx = 0
        while idx < keyValCount:
            headDict[self.__lastKeys[idx]] = values[idx]
            idx += 1





            




