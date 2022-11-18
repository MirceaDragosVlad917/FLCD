from Model.Hashtable import HashTable


class SymbolTable:
    def __init__(self):
        self.idTable = HashTable(107)
        self.intConstTable = HashTable(107)
        self.strConstTable = HashTable(107)

    def getIdTable(self):
        return self.idTable

    def getIntConstTable(self):
        return self.intConstTable

    def getStrConstTable(self):
        return self.strConstTable

    def addToIdTable(self, token):
        return self.idTable.insert(token)

    def addToIntConstTable(self, token):
        return self.intConstTable.insert(token)

    def addToStrConstTable(self, token):
        return self.strConstTable.insert(token)

    def __str__(self):
        return "SymbolTable{" + "\n" + "idTable=" + str(self.idTable.data) + "\n" + "intConstTable=" + str(
            self.intConstTable.data) + "\n" + "strConstTable=" + str(self.strConstTable.data) + "\n" + '}'
