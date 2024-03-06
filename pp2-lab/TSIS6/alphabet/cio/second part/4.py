# Write a Python program that invoke square root function after specific milliseconds​

import time, math

num = int(input())
ms = int(input())

time.sleep(ms / 1000)
root = math.sqrt(num)
print(f"Square root of {num} after {ms} milliseconds is {root}")