def intsqrt(N):
    n = N
    while n**2 > N:
        n = (n + N // n) // 2
    return n

def issquare(N):
    n = intsqrt(N)
    return n**2 == N
    
N = int(input("Enter a number: "))
print(f"Integer square root of {N} is {intsqrt(N)}")

if issquare(N):
	print(f"{N} is a perfect square of {intsqrt(N)}")
else:
	print(f"{N} is not a perfect square of {intsqrt(N)}")