def power(base, exponent):
    # Base case
    if exponent == 0:
        return 1
    
    # If exponent is even
    if exponent % 2 == 0:
        half = power(base, exponent // 2)
        return half * half
    
    # If exponent is odd
    else:
        return base * power(base, exponent - 1)


# Example usage
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))

print(f"{b}^{e} =", power(b, e))
