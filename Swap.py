def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return "values after swaping are {} and {}".format(a,b)

num1=int(input('enter first number : '))
num2=int(input('enter second number : '))

print('values before swaping are {} and {}'.format(num1,num2))
print(swap(num1,num2))