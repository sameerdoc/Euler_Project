# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

a = 0
b = 1
count = 1
lst = []

while count:
    # print(a)
    c = a + b
    a = b
    b = c
    count += 1
    lst.append(a) # put the numbers into a list to track its index later

    if len(str(a)) == 1000:  # convert that number to string to get its length for comparison
        print(a)  # number at the 1000th location
        print("length of a is :", len(str(a)))
        print("Index at which number is of size 1000 is:",lst.index(a) + 1) # use 'index' method on list and supply it the value of the number at 1000th location .i.e. current value of a , and "+ 1 coz index starts at 0"
        break # break out of while loop
