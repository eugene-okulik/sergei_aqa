result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 209'
result4 = 'результат: 2'
numb = 10


def new_result(result):
    list1 = result[result.index(':') + 1:]
    list1 = list1.strip()
    list11 = int(list1) + numb
    print(list11)


new_result(result1)
new_result(result2)
new_result(result3)
new_result(result4)
