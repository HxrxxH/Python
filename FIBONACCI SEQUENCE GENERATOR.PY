def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

num = int(input("Enter number of terms: "))
print("Fibonacci Sequence:", fibonacci(num))
