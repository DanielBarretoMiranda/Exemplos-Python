def fib(n,m):
    def fib2(m):
        if m == 1 or m == 2:
            return 1
        else:
            return fib2(m-1) + fib2(m-2)
    if n==m:
         print(fib2(m), end=' ')
    else:
         print(fib2(m), end=' ')
         fib(n,m+1)

n= int(input('digite um numero: '))
m= 1
fib(n,m)