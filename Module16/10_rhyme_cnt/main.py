n = int(input("Количество человек: "))
k = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {k}-й человек")

people = list(range(1, n + 1))
current_index = 0

while len(people) > 1:
    print(f"\nТекущий круг людей: {people}")
    start_person = people[current_index]
    print(f"Начало счёта с номера {start_person}")

    out_index = (current_index + k - 1) % len(people)
    removed_person = people.pop(out_index)
    print(f"Выбывает человек под номером {removed_person}")

    if people:
        current_index = out_index % len(people)

print(f"\nОстался человек под номером {people[0]}")

