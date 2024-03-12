start = 1
end = 101

result = 0

for x in range(start, end):  
    if x % 2 == 1:
        result = result + x

print("Sum of odd numbers is", result)
