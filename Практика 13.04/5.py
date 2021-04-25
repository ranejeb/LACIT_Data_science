def romb2(num):
    for i in range(1, num+1):
        string = ""
        for j in range(1, num-i+1):
            string += "  "
        for k in reversed(range(num-i+2, num+1)):
            string += str(k) + " "
        string +=  str(num-i+1) + " "
        for l in reversed(range(num-i+2, num+1)):
            string += str(l) + " "
        print(string)


    for i in reversed(range(1, num)):
        string = ""
        for j in range(1, num-i+1):
            string += "  "
        for k in reversed(range(num-i+2, num+1)):
            string += str(k) + " "
        string +=  str(num-i+1) + " "
        for l in range(num-i+2, num+1):
            string += str(l) + " "
        print(string)
romb2(int(input("введите число , " ))) 