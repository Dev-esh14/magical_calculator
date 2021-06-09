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