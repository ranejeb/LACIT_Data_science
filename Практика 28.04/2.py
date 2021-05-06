import sys
"""
print("This is the name of the program:", sys.argv[0])
  
print("Argument List:", str(sys.argv))
"""

s = ''
s2 = ''
for i in range(1,len(sys.argv)):
    s = s + sys.argv[i]+' '
s2 = s
print(s2,end=' ')

#python3 2.py arg1 arg2