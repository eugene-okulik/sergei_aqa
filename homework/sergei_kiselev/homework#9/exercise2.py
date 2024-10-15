temperatures = ([20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                 30, 28, 24, 23])

new_temperature = list(filter(lambda x: x > 28, temperatures))

print(new_temperature)
print(max(new_temperature))
print(min(new_temperature))
print(sum(new_temperature))
print(round(sum(new_temperature) / len(new_temperature), 2))
