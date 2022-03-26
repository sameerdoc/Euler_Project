# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

number = int(input("Provide Integer number to find the prime factor of:"))
lst = []
lst1 = []

# To find the factors of a number n, you dont have to check all numbers less than n. It is enough if you check upto int(sqrt(n))
# here we find all the factors of given number and creating a list of those numbers i.e. all such numbers which can be multiplies to give result as given number
# so instead of using range(2,number), where number can be huge, use int(sqrt(number)) otherwise code will be stuck in a huge loop whose loop size will size of number

for i in range(2,int(sqrt(number))):
    if number % i == 0:
        lst.append(i)

# To find the factors of a number n, you dont have to check all numbers less than n. It is enough if you check upto int(sqrt(n))
# here we checking out of above list which factors can be divided furthr into small factors(numbers) and creating its list
for k in range(2,int(sqrt(number))):
    for j in lst:
        if j%k == 0 and j != k:
            lst1.append(j)

# by finding difference of above 2 lists we ll get numbers ( factors) which cant be divided further
diff = set(lst) - set(lst1)

# sort that list to find highest number in it
diff1 = sorted(diff)
# print the last element of that sorted list which will be highest in value, that would be the largest factor
print("Largest prime factor of  given number:", number, end= '')
print(" is:",diff1[-1])
