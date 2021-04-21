class DataChannel:


    def __init__(self):
        self.reset()


    def reset(self):
        self.__title = ""
        self.__unit = ""
        self.__unitValue = 0
        self.__data = []
   


     # append value to data-channel   
    def append(self, value):
        self.__data.append(value)


    def data(self):
        return self.__data


    def setTitle(self, text):
        # set channel title
        self.__title = text


    def title(self):
        return self.__title


    def setUnit(self, text):
        # set channel title

        self.__unit = text


    def unit(self):
        return self.__unit


    def setUnitValue(self, value):
        self.__unitValue = value

    
    def unitValue(self):
        return self.__unitValue





 
    