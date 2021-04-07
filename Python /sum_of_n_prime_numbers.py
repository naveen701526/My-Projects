MAX = 105000
print("Input a number (n≤10000) to compute the sum:(0 to exit)")
is_prime = [True for _ in range(MAX)]
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** (1 / 2)) + 1):
    if is_prime[i]:
        for j in range(i ** 2, MAX, i):
            is_prime[j] = False
primes = [i for i in range(MAX) if is_prime[i]]
while True:
    n = int(input())
    if not n:
        break
    print("Sum of first", n, "prime numbers:")
    print(sum(primes[:n]))
