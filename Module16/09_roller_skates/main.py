num_rollers = int(input("Количество роликов: "))
rollers = []
for i in range(num_rollers):
    size = int(input(f"Размер пары {i + 1}: "))
    rollers.append(size)

num_people = int(input("\nКоличество людей: "))
feet_sizes = []
for i in range(num_people):
    size = int(input(f"Размер ноги человека {i + 1}: "))
    feet_sizes.append(size)


count = 0
for foot_size in feet_sizes:
    if foot_size in rollers:
        count += 1
        rollers.remove(foot_size)

print(f"Наибольшее количество людей, которые могут взять ролики: {count}")

