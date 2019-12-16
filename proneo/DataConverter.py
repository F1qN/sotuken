import csv


class data:
    path = None
    tables = []
    def __init__(self):
        self.path = "./data/table.csv"
        with open(self.path) as f:
            reader = csv.reader(f)
            for row in reader:
                cell = (row[0],row[1])
                self.tables.append(cell)

    def getX(self,order):
        return int(self.tables[order][0])

    def getY(self,order):
        return int(self.tables[order][1])

    def getLength(self):
        return len(self.tables)



        
