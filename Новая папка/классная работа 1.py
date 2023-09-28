def sum_elements(numbers):
    return sum(numbers)

def find_max_element(numbers):
    if len(numbers) == 0:
        return None
    max_element = numbers[0]
    for num in numbers:
        if num > max_element:
            max_element = num
    return max_element

def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

menu = """
Меню:
1. Подсчитать сумму элементов списка
2. Найти наибольший элемент списка
3. Удалить дубликаты из списка
4. Объединить два списка
0. Выйти из программы
"""

while True:
    print(menu)
    choice = int(input("Выберите действие: "))

    if choice == 0:
        print("Программа завершена.")
        break
    elif choice == 1:
        input_str = input("Введите список чисел через пробел: ")
        my_list = list(map(int, input_str.split()))
        result = sum_elements(my_list)
        print("Сумма элементов списка равна:", result)
    elif choice == 2:
        input_str = input("Введите список чисел через пробел: ")
        my_list = list(map(int, input_str.split()))
        result = find_max_element(my_list)
        if result is not None:
            print("Наибольший элемент в списке:", result)
        else:
            print("Список пуст.")
    elif choice == 3:
        input_str = input("Введите список чисел через пробел: ")
        my_list = list(map(int, input_str.split()))
        result = remove_duplicates(my_list)
        print("Список без дубликатов:", result)
    elif choice == 4:
        input_str1 = input("Введите первый список чисел через пробел: ")
        list1 = list(map(int, input_str1.split()))
        input_str2 = input("Введите второй список чисел через пробел: ")
        list2 = list(map(int, input_str2.split()))
        result = merge_tuples(list1, list2)
        print("Объединенный список:", result)
    else:
        print("Некорректный выбор действия. Попробуйте еще раз.")