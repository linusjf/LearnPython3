#!/usr/bin/env python
"""
That sounds like a classic problem in algorithm design, specifically a variation of the Longest Increasing Subsequence (LIS) problem.

Here's a possible solution in Python:

```
def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] == arr[j] + 1:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

Example usage:
arr = [1, 2, 3, 5, 6, 7, 9, 10]
print(longest_increasing_subsequence(arr))  # Output: 5
```

This solution uses dynamic programming to build up a table `dp` where `dp[i]` represents the length of the longest increasing subsequence ending at index `i`. The final answer is the maximum value in the `dp` table.

The time complexity of this solution is O(n^2), where n is the length of the input array. This is because we have two nested loops that iterate over the array.

"""

def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    dp = [1] * len(arr)

    for i in range(1, len(arr)):
        j = i - 1
        if arr[i] == arr[j] + 1:
            dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)

arr = [1, 2, 3, 5, 6, 7, 9, 10]
print(longest_increasing_subsequence(arr))  # Output: 3
