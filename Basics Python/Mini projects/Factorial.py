# Python code​​​​​​‌‌​‌‌​‌​​​​‌‌‌‌‌​​​​​‌​‌‌ below

def factorial(num):
    # Your code goes here.
    fact = 1
    if type(num) != int:
        return None
    if num == 0:
        return 1
    if num < 0:
        return None 
    '''else:
        for i in range(1, num + 1):
            fact = fact * i
        return fact
    '''
    return num * factorial(num-1)
    
print(factorial(5))