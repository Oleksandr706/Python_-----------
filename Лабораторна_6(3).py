import random

original = []
for i in range(25):
    original.append(random.randint(-50, 50))

A1 = [] # додатні
A2 = [] # від'ємні

for x in original:
    if x > 0:
        A1.append(x)
    elif x < 0:
        A2.append(x)

print("Список A1 (додатні):", A1)
print("Список A2 (від'ємні):", A2)