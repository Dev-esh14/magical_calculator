"""
 You are going to design a magical calculator with the following functions.
• Function that takes input and calculates it’s factorial. (A)
• Function that takes input and calculate it’s sum of digits. (B)
• Function that takes input and find’s the largest digit in the input. (C)
- Implement all the above functions.
- Get input and pass the input to factorial function (A), get the output from
factorial function and pass it as input to sum of digits function (B). Get the output
from sum of digits function, add the output with random 5 digit number and pass
the outcome to largest digit function (C) and print the output that you receive from
function C.
"""
def fact(n):
    if(n==1):
        return n
    else:
        return n*fact(n-1)

def sum_up(a):
    sum=0
    while (a!= 0):        
        sum = sum + (a % 10)
        a=a //10       
    return sum
    
def largest_digit(b):
    c=b+10000
    return max(str(c))
        
n=int(input("Enter the number:"))
a=fact(n)
b=sum_up(a)
print("output is:"+largest_digit(b))

"""
OUTPUT:
input=5
output is: 3
"""