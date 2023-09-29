# Задача 6
# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана). 
# Функция формирует словарь с информацией о результатах отгадывания. 
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде. 
# Для формирования результатов используйте генераторное выражение.


_results_dict = {}


def record_result(quiz_text, attempt_number):
    global _results_dict
    if quiz_text not in _results_dict:
        _results_dict[quiz_text] = []
    if attempt_number is not None:
        _results_dict[quiz_text].append(attempt_number)


def display_results():
    global _results_dict
    sorted_results = list(_results_dict.items())
    for quiz_text, attempt_numbers in sorted_results:
        if attempt_numbers:
            min_attempt = min(attempt_numbers)
            attempts_str = ', '.join(map(str, attempt_numbers))
            print(
                f'Загадка "{quiz_text}" была угадана с {min_attempt}-й попытки\
                    (всего попыток: {attempts_str})')
        else:
            print(f'Загадка "{quiz_text}" не была угадана')


def quiz(my_str, my_solve, my_try=3):
    print(my_str)
    count = 0
    while count < my_try:
        answer = input('Введите ответ: ')
        if answer in my_solve:
            print(f'Вы угадали: это {answer}  \nС попытки N {count + 1}')
            break
        count += 1
    else:
        print('Вы не угадали')
    return answer  # Возвращаем значение answer


def multi_quiz(my_quit, my_try=3):
    for key, value in my_quit.items():
        print('Загадка ', end='')
        answer = quiz(key, value, my_try)  # Получаем значение answer из quiz
        count = value.index(answer) + 1 if answer in value else None
        record_result(key, count)


my_dic = {'ex1': ['ans1', 'ans2', 'ans3'],
          'ex2': ['ans4', 'ans5', 'ans6'],
          'ex3': ['ans7', 'ans8', 'ans9']}

multi_quiz(my_dic)

# Вывод результатов
print("Результаты угадывания:")
display_results()