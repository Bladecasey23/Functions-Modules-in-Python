import math

num = float(input("Enter a positive number: "))

if num <= 0:
    print("Please enter a number greater than 0 for square root and logarithm.")
else:
    sqrt_val = math.sqrt(num)
    log_val = math.log(num)
    sine_val = math.sin(num)  

print(f"Square root of {num}: {sqrt_val}")
print(f"Natural logarithm (ln) of {num}: {log_val}")
print(f"Sine of {num} radians: {sine_val}")
