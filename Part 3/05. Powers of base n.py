limit = int(input("Upper limit:"))
base = int(input("Base:"))
result = [limit + 1]
power = 1

while power <= limit:
    result.append(power)
    power *= base

result.pop(0)

for x in result:
  print(x)