n = int(input("num:\n"))

sum = 0
num = n
count = 0

while (n != 0):
    
    remainder = n % 10
    n //= 10
    sum += remainder ** 3
    count += 1
    
print("sum : {0}".format(sum))
print("number of digits :", count)

if (num == sum):
    print("Arm Strong")


