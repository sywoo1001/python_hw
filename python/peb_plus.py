def fibo(n):
    a = 0
    b = 1
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    elif(n>1):
        return fibo(n-1) + fibo(n-2)
print(fibo(3))