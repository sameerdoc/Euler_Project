# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Solution Below


a = 1
b = 2
count = 1
lst = []

while count:
    # print(a)
    c = a + b
    #update values, dont change below sequence
    a = b
    b = c
    count += 1
    # move even numbers to a list and find the sum
    if a % 2 == 0:
        lst.append(a)
        total = sum(lst)

    #if the term exceeds value of 4 million, print sum and break from while loop
    if a >= 4000000:
        count = 0
        print("limit reached!")
        print("sum of even numbers:",total)
        break
