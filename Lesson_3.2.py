# def fibo(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a

def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
print(fibo(6))