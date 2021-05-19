class Phone:
    
    def __init__(self, n , m , w ):

        self.number = n
        self.model = m
        self.weight = w

    def receiveCall(self, name ):

        print("Звонит "+ name)

    def getNumber(self, n):
        
        return n



phone1 = Phone("+375233979349" , "nokia" , 1234  )
phone2 = Phone("+375346979349" , "lg" , 457  )
phone3 = Phone("+375233134349" , "samsung" , 567  )


print(phone1.number, phone1.model, phone1.weight )
print(phone2.number, phone2.model, phone2.weight )
print(phone3.number, phone3.model, phone3.weight )

phone1.receiveCall("Jonny")
phone2.receiveCall("Cristian")
phone3.receiveCall("Dorian")

phone3.getNumber("+375296785940")