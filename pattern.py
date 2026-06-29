"""
n = 4 
*
**
***
****
"""
n = 4
for i in range(0,n+1) :
    print(i*"*")

number = input("Give some numbers: ")
list = number.split()
sum = 0 
for num in list :
    sum = sum + int(num)
print(sum)
print(max(list))
