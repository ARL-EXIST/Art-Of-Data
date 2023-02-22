class ComplexNumber:
    
    def __init__(self, n_One, n_Two):
        self.a = n_One
        self.b = n_Two

    def string(self):
        if(self.b > 0):
            return (str(self.a) + " + " + str(self.b) + "i")
        if(self.b < 0):
            return (str(self.a) + " " + str(self.b) + "i")
        else:
            return (str(self.a))

    def addition(self, other):
        self.a = self.a + other.a
        self.b = self.b + other.b
    
    def subtraction(self, other):
        self.a = self.a - other.a
        self.b = self.b - other.b
    
    def multiplication(self, other):
        num = ComplexNumber((self.a * other.a) - (self.b * other.b), (self.a * other.b) + (self.b * other.a))
        self.a = num.a
        self.b = num.b

    def division(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        self.a = ((a*c) + (b*d))/((c*c) +(d*d))
        self.b = ((b*c) - (a*d))/((c*c) +(d*d))
    
class DataFrame:

    def __init__(self, table):
        self.tblArray = table
    
    def getIndex(self, row, col):
        return self.tblArray[row-1][col-1]
    
    def setIndexTo(self, row, col, val):
        self.tblArray[row-1][col-1] = val

    def getValIndex(self, val):
        for x in self.tblArray:
            for y in x:
                if(self.tblArray[x][y] == val):
                    return x, y
        return None
        
    def countRows(self):
        return len(self.tblArray) - 1

    def countCol(self):
        return len(self.tblArray[0]) - 1
    
    def appendRow(self, rowArr):
        self.tblArray.append(rowArr)

    def appendCol(self, colArr):
        count = 0
        for x in self.tblArray:
            self.tblArray[count].append(colArr[count])
            count += 1
    
    def insertRow(self, rowArr, index):
        self.tblArray.insert(rowArr, index)
    
    def insertCol(self, colArr, index):
        count = 0
        for x in self.tblArray:
            self.tblArray[count].insert(colArr[count], index)
            count += 1
    

x = ComplexNumber(11, 24)
y = ComplexNumber(-4, -1)
print(x.string())
x.division(y)
print(x.string())