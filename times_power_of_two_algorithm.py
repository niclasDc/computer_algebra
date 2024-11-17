import time

def pot(n):

    if n == 1:
        return 2

    if n % 2 == 0:
        result = pot(n/2)
        return result * result
    else:
        result = pot((n-1)/2)
        result = result * result
        return 2 * result


def pot_karatsuba(n):

    if n == 1:
        return 2

    if n % 2 == 0:
        result = pot_karatsuba(n/2)
        return karatsuba(result, result)
    else:
        result = pot_karatsuba((n-1)/2)
        result = karatsuba(result, result)
        return karatsuba(2, result)


def karatsuba(x, y):
    # Base case for recursion: if the numbers are small enough, multiply them directly.
    if x < 10 or y < 10:
        return x * y

    # Determine the size of the numbers.
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split x and y.
    # For example, if x = 1234 and m = 2, then a = 12 and b = 34
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    # Recursively calculate the three products
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine the results using the Karatsuba formula:
    # (10^(2*m) * ac) + (10^m * (ad + bc)) + bd
    result = ac * 10**(2 * m) + ad_plus_bc * 10**m + bd

    return result


n = 25
start_time = time.time()
result_standard = pot(n)
end_time = time.time()
time_standard = end_time - start_time
print(f"Standard recursive method: 2^{n} = {result_standard}")
print(f"Time taken by standard method: {time_standard:.6f} seconds\n")

start_time = time.time()
result_karatsuba = pot_karatsuba(n)
end_time = time.time()
time_karatsuba = end_time - start_time
print(f"Karatsuba recursive method: 2^{n} = {result_karatsuba}")
print(f"Time taken by Karatsuba method: {time_karatsuba:.6f} seconds\n")

print(f"Time difference: {abs(time_standard - time_karatsuba):.6f} seconds")
print(f"Karatsuba method is {time_standard / time_karatsuba:.2f} times faster" if time_karatsuba != 0 else "Karatsuba method didn't take measurable time")
