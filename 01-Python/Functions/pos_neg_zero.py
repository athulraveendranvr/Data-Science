"""define a function to return positive negative or zero for a given number"""

result = lambda num:"positive" if num > 0 else("negative"if num < 0 else "zero")

print(result(-5))