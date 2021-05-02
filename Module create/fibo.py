def find_fibo(n):
    if n <= 2:
        return 1
    fibo_x, fibo_next = 1, 1
    i = 3
    while i <= n:
        i += 1
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
    return fibo_next

def list_fibo(n):
    fibo_list = [1,1]
    if n<=2:
        return fibo_list[:n]
    fibo_x, fibo_next = 1, 1
    i = 3
    while i <= n:
        i += 1
        fibo_x, fibo_next = fibo_next, fibo_x + fibo_next
        fibo_list.append(fibo_next)
    return fibo_list

if __name__ == "__main__":  #import file a jeno nichergulo print nahoy sejonno ai global name function
    for j in range(1,11):
        print(find_fibo(j))
        
    print(list_fibo(1))
    print(list_fibo(2))
    print(list_fibo(10))
