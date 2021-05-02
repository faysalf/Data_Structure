def find_fibo(n):
    if n <= 2:
        return 1
    fibo_x, fibo_next = 1, 1
    i = 3
    while i <= n:
        i += 1
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
    return fibo_next

for j in range(1,11):
    print(find_fibo(j))
