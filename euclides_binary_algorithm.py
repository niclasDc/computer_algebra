def GCD_binary(a, b):

    # if a == b
    if a == b:
        return a
    
    # if a and b are even
    if a % 2 == 0 and b % 2 == 0:
        result = 2 * GCD_binary(a//2, b//2)
        print(f"2 * GCD({a//2}, {b//2})")
        return result
    
    # if a is even and b is odd
    if a % 2 == 0 and b % 2 == 1:
        result = GCD_binary(a//2, b)
        print(f"GCD({a//2}, {b})")
        return result
    
    # if a is odd and b is even
    if a % 2 == 1 and b % 2 == 0:
        result = GCD_binary(a, b//2)
        print(f"GCD({a}, {b//2})")
        return result
    
    # if a and b are odd
    if a % 2 == 1 and b % 2 == 1:
        if a > b:
            result = GCD_binary((a-b)//2, b)
            print(f"GCD({(a-b)//2}, {b})")
            return result
        else:
            result = GCD_binary(a, (b-a)//2)
            print(f"GCD({a}, {(b-a)//2})")
            return result
    

print(GCD_binary(8771, 3206))
