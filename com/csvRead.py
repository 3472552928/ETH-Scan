import csv
import os


class ReadCsv():
    def __init__(self,filename):
        self.filename=filename
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.file = os.path.join(path, "conf", filename)

    def readALL(self,end,start):
        res =[]
        with open(self.file,"r") as f:
            self.data = csv.reader(f)
            for i in self.data:
                res.append(i)
        # print(res[start:end+1])
        return res[start:end+1]

    '''按行提取'''
    def readRow(self,i):
        with open(self.file,"r") as f:
            data = csv.reader(f)
            res = list(data)
            print(res[i])
        return res

    '''按列提取'''
    def readLine(self,i=1):
        with open(self.file,'r') as f:
            data = csv.reader(f)
            for line in data:
                print(line[0])

# if __name__ == '__main__':
#     cs = ReadCsv("export-0x5026f006b85729a8b14553fae6af249ad16c9aab_withnotes---wojak.csv")
#     data = cs.readALL(end=5002,start=1)
#     # print(data)
#     # cs.readRow(i=2)
#     # cs.readLine()


