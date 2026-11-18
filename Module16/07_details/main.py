shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]


part_name = input("Название детали: ")

count = 0
total_cost = 0

for part, price in shop:
    if part == part_name:
        count += 1
        total_cost += price

print(f"Количество деталей: {count}")
print(f"Общая стоимость: {total_cost}")

