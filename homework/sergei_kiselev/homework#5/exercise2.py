result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'
list1 = result1[result1.index(':') + 1:]
list1 = list1.strip()
list11 = int(list1) + 10
list2 = result2[result2.index(':') + 1:]
list1 = list1.strip()
list12 = int(list2) + 10
list3 = result3[result3.index(':') + 1:]
list1 = list1.strip()
list13 = int(list3) + 10
print(list11)
print(list12)
print(list13)
