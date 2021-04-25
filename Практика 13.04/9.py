def fn(string):
    for i in range(0,len(string)):
        print(string[i],'-',ord(string[i]))
fn(str(input("введите , ")))