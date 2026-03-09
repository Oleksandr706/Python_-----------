
C = ["Хліб", "Молоко", "Сир"]
A = [100, 50, 30]             
B = [25.5, 38.0, 120.0]       

total_cost = 0
for i in range(len(A)):
    total_cost += A[i] * B[i]

average_price = sum(B) / len(B)

# Знаходимо товар, якого найбільше
max_qty = max(A) 
index_max = A.index(max_qty)

print("Загальна вартість:", total_cost)
print("Середня ціна:", average_price)
print("Товару якого найбільше:", C[index_max])