temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

new_temperature = filter(lambda x: x > 28, temperatures)
# print(list(new_temperature)) не понял почему после выполнения этой строки список становится пустым :(

list_hot_temp = []
for x in new_temperature:
        list_hot_temp.append(x)

print(list_hot_temp)
print(max(list_hot_temp))
print(min(list_hot_temp))
