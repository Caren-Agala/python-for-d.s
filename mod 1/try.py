total = 0
i = 0
while i < 5:
    age = int(input('age: '))
    i = i + 1
    if age <= 3:
        continue
    elif age > 3:
        total += 100
    
print(total)

    