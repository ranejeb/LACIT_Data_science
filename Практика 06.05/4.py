import numpy


class Reader:
    __slots__=('fullname','id','facultet','date_of_birth','phone')

    def __init__(self,fullname):
        self.fullname=fullname

    def get_fullname(self):
        return self.fullname
    def set_fullname(self,fullname):
        self.fullname=fullname

    def get_id(self):
        return self.id
    def set_id(self,id):
        self.id=id

    def set_facultet(self,facultet):
        self.facultet=facultet
    def get_facultet(self):
        return self.facultet

    def set_date_of_birth(self,date_of_birth):
        self.date_of_birth=date_of_birth
    def get_date_of_birth(self):
        return self.date_of_birth

    def set_phone(self,phone):
        self.phone=phone
    def get_phone(self):
        return self.phone

    def takeBook1(self,num):
        print(f'{self.fullname} взял {num} книги')
    def takeBook2(self,*books):
        print(f'{self.fullname} взял книги:', ' '.join(books))
    def takeBook3(self,*books):
        print(f'{self.fullname} взял книги:', " ".join([i.getname() for i in books]))
    def returnBook1(self,num):
        print(f'{self.fullname} вернул {num} книги')
    def returnBook2(self,*books):
        print(f'{self.fullname} вернул книги:', ' '.join(books))
    def returnBook3(self,*books):
        print(f'{self.fullname} вернул книги:', " ".join([i.getname() for i in books]))

class book:
    __slots__=('author','name')
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
    
mas=numpy.array([Reader('Петров П.П.'),Reader('Иванов В.В.'),Reader('Антонов А.А.')])
mas[0].takeBook1(2)
mas[1].takeBook2('a','b','c')
mas[2].takeBook3(book('a'),book('b'),book('c'))
mas[0].returnBook1(2)
mas[1].returnBook2('a','b','c')
mas[2].returnBook3(book('a'),book('b'),book('c'))