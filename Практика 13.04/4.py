def romb(num):
    for i in range(1, num+1):
        string = ""
        for j in range(1, num-i+1):
            string += "  "
        for k in range(1, i):
            string += str(k) + " "
        string +=  str(i) + " "
        for l in reversed(range(1, i)):
            string += str(l) + " "
        print(string)

    for i in reversed(range(1, num)):
        string = ""
        for j in range(1, num-i+1):
            string += "  "
        for k in range(1, i):
            string += str(k) + " "
        string +=  str(i) + " "
        for l in reversed(range(1, i)):
            string += str(l) + " "
        print(string)
romb(int(input("input number, " )))