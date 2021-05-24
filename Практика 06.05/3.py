import numpy

class matriza:
    __slots__=('matriza','stroks','stolbs')
    def __init__(self,stroks=2,stolbs=2,*matriza):
        self.stroks=stroks
        self.stolbs=stolbs
        if len(matriza)>=stolbs*2:
            self.matriza=numpy.array([[matriza[i] for i in range(stolbs) ],[matriza[i] for i in range(stolbs,stolbs*2)]],  dtype=float)
        else:
            self.matriza=numpy.empty(2,2)
    def add(self,other):
        array=numpy.zeros((2,self.stolbs))

        if self.stolbs==other.stolbs:
            for i in range(self.stroks):
                for j in range(self.stolbs):
                    array[i][j]=self.matriza[i][j]+other.matriza[i][j]
        print(array)
    def mul(self,other):
        array=numpy.zeros((2,self.stolbs))
        for i in range(self.stroks):
            for j in range(self.stolbs):
                array[i][j] = self.matriza[i][j] * other
        print(array)
    def print(self):
        print(self.matriza)
m1=matriza(2,2,1,1,1,1)
print(m1.matriza)
m2=matriza(2,2,2,2,2,2)
print(m2.matriza)
m1.add(m2)
m1.mul(5)
m1.print()