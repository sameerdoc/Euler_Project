#Print fibonacci sequence of given MAX number 

MAX = 10
a = 1
b = 2
count = 0

while count < MAX:
    print(a)
    c = a + b
    #update values, dont change below sequence
    a = b
    b = c
    count += 1
