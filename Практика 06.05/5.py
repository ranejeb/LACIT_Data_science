import random

class project:
    __slots__=('name','cost','strings_need','strings_ready')
    def __init__(self,name,cost,strings_need):
        self.name=name
        self.cost=cost
        self.strings_need=strings_need
        self.strings_ready=0
    def getcost(self):
        return self.cost
    def getstringsneed(self):
        return self.strings_need
    def getstringsready(self):
        return self.strings_ready
    def setstringsready(self,string):
        self.strings_ready=string
    def getname(self):
        return self.name
class programmer:
    __slots__=('fullname','level',)
    def __init__(self,name,level):
        self.fullname=name
        self.level=level
    def getlevel(self):
        return self.level

class manager :
    __slots__=('fullname','programmers','project')
    def __init__(self,name,programmers,project):
        self.fullname = name
        self.programmers=programmers
        self.project=project
    def getproject(self):
        return self.project
    def setproject(self,project):
        self.project=project
    def getprogrammers(self):
        return self.programmers
    def getfullname(self):
        return self.fullname

manag=manager('A'  ,  [ programmer('B',random.randrange(1,4,1)) , programmer('C',random.randrange(1,4,1)) , programmer('D',random.randrange(1,4,1)) ]  ,  project('1' , random.randrange(1,10000,1000) , random.randrange(1,10000,1000)) )
capital=10000
mount=0
while capital>0:
    print(f'Месяц №{mount} \nКапитал {capital}')
    if(manag.getproject().getstringsneed()<=manag.getproject().getstringsready()) :
        capital +=manag.getproject().getcost()
        print(f'Проект {manag.getproject().getname()} закончен')
        manag.setproject(  project('1' , random.randrange(1,10000,1000) , random.randrange(1,10000,1000)) )
        print(f'Начат проект {manag.getproject().getname()}')
    for _ in manag.getprogrammers():
        if _.getlevel()==1:
            manag.getproject().setstringsready(manag.getproject().getstringsready()+100)
            capital-=100
        elif _.getlevel() == 2:
            manag.getproject().setstringsready(manag.getproject().getstringsready() + 200)
            capital -= 200
        elif _.getlevel() == 3:
            manag.getproject().setstringsready(manag.getproject().getstringsready() + 300)
            capital -= 300
    mount += 1
else:
    print('Вы проиграли')
