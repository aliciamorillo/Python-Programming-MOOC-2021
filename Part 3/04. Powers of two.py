limit = int(input("Upper limit:"))
result = [limit + 1]
power = 1

while power <= limit:
    result.append(power)
    power *= 2

result.pop(0)

for x in result:
  print(x)