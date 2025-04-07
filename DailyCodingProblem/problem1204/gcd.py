#!/usr/bin/env python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_gcd(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

# Example
nums = [42, 56, 14]
print(find_gcd(nums))  # Output: 14
