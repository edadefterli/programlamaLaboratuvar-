def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(5))

def fastFib(n,memo={}):     #memo'da daha önceden hesaplanmış fibonacci değerlerini tutar.
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result=fastFib(n-1,memo)+fastFib(n-2,memo)
        return result

print(fib(5))