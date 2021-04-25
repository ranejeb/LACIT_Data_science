def fn(string):
    sum = 0
    for i in range(0,len(string)):
        sum += ord(string[i])
    print(sum)
fn(str(input("Input line, ")))