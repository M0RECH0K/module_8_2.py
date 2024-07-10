def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_of_numbers = personal_sum(numbers)
        average = sum_of_numbers[0]
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    try:
        calculate_ = average / (len(numbers)-sum_of_numbers[1])
    except ZeroDivisionError:
        return 0

    return calculate_


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')