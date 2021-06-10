from DataParser import DataParser
from DecimalGenerator import DecimalGenerator
class HeaderParser:
    
    # Header Information
    Head_Key_Order = "Auftrag"
    Head_Key_PrePressure = "Vordruck"
    Head_Key_Furnace_Temp = "Ofentemp"
    Head_Key_Part_Weight = "Gewicht"

    # Fotter Information
    Foot_Key_Amount = "Menge[kg]"
    Foot_Key_Order_Set = "AuftragSoll"
    Foot_Key_Order_Cnt = "AuftragIst"
    Foot_Key_Charge_Set = "ChargeSoll"
    Foot_Key_Charge_Cnt = "ChargeIst"
    Foot_Key_Cycle_Brutto = "ZyklusBrutto[sek]"
    Foot_Key_Cycle_Netto = "ZyklusNetto[sek]"

    def __init__(self):              
        # constructor
        # constants
        self.__CONST_HEADER_STATE_KEY_VALUE = 0
        self.__CONST_HEADER_STATE_TABLE_KEY = 1
        self.__CONST_HEADER_STATE_TABLE_VALUE = 2
        
        # properties
        self.reset()
        return

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
        values = []
        lastIdx = 0
        currIdx = 0
        while currIdx < len(fileLine):
            item = fileLine[currIdx]
            if item == ";":
                if lastIdx < currIdx:
                    if lastIdx == 0:
                        key = fileLine[lastIdx:currIdx]
                    else:
                        values.append(fileLine[lastIdx:currIdx])
                    lastIdx = currIdx +1
                    

            currIdx += 1

        if lastIdx < currIdx:
            values.append(fileLine[lastIdx:currIdx])
        idx = 0
        while len(values) > idx:
            if key == HeaderParser.Head_Key_Order:
                values[idx] = int(values[idx])
            elif key == HeaderParser.Head_Key_PrePressure:
                values[idx] = float(DataParser.checkAndReplaceComma(self, values[idx]))
            elif key == HeaderParser.Head_Key_Furnace_Temp:
                values[idx] = int(values[idx])
            elif key == HeaderParser.Head_Key_Part_Weight:
                values[idx] = int(values[idx])
        
            
            elif key == HeaderParser.Foot_Key_Amount:
                values[idx] = int(values[idx])
            elif key == HeaderParser.Foot_Key_Order_Set:
                values[idx] = int(values[idx])
            elif key == HeaderParser.Foot_Key_Order_Cnt:
                values[idx] = int(values[idx])
            elif key == HeaderParser.Foot_Key_Charge_Set:
                values[idx] = int(values[idx])
            #elif key == HeaderParser.Foot_Key_Charge_Cnt:
                #values[idx] = int(values[idx])
            elif key == HeaderParser.Foot_Key_Cycle_Brutto:
                values[idx] = float(DataParser.checkAndReplaceComma(self, values[idx]))
            elif key == HeaderParser.Foot_Key_Cycle_Netto:
                values[idx] = float(DataParser.checkAndReplaceComma(self, values[idx]))
               

            dict[key] = values
            idx += 1
        
        #if key in headFootInformation:
            #value = self.__convertHeaderFootertoINT(value)
        
        # case statement regarding key content
        #dict[key] = value
        #return
    
    def __convertHeaderFootertoINT(self, value):
        value = str(value)
        posComma = value.find(",")
        posDot = value.find(".")
        posSemicolon = value.find(";")

        if posSemicolon != -1:
            valueList = value.split(";")
            idx = 0
            while len(valueList) > idx:
                posComma = valueList[idx].find(",")
                posDot = valueList[idx].find(".")
                if posComma != -1:
                    self.__deci = DecimalGenerator()
                    self.__deci.setDotDelimiter()    
                    valueList[idx] = self.__deci.generate(valueList[idx])
                    valueList[idx] = float(valueList[idx])

                elif posDot != -1:
                    valueList[idx] = float(valueList[idx])

                else:
                    valueList[idx] = int(valueList[idx])
                
                value = ""
                value += valueList[idx] + ";"
                
                
                
                idx += 1
            return value
            
            



        elif posComma != -1:
            self.__deci = DecimalGenerator()
            self.__deci.setDotDelimiter()    
            value = self.__deci.generate(value)
            value = float(value)
            return value

        elif posDot != 1:
            value = float(value)
            return value

        else:
            value = int(value)
            return value
        
        



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
                    values.append(int(fileLine[lastIdx:currIdx]))

                lastIdx = currIdx +1
            currIdx += 1
                    

        if lastIdx < currIdx:
            values.append(int(fileLine[lastIdx:currIdx]))
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
            self.__lastKeys[idx] = "S{:02d}".format(sIdx)
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





            




