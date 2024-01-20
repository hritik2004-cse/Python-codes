def factorial(n):
    if (n<0):
        return 'enter a positive number'
    elif (n==0):
        return 'factorial of 0 is 1'    
    else:
        fact=1
        for i in range(1,n+1):
            fact*= i
        return "factorial of {} is {} ".format(num,fact)
                
                
num=int(input('enter a number :'))
print(factorial(num))                