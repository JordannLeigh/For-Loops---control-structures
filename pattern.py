# Write code that outputs a half diamond shape
# Use an if-else statment and a single for loop
for i in range(1, 10):
    if i <= 5:
        print("*" * i)
    else:
        print("*" * (10 - i))
        