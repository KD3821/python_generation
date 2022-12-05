'''
Функция должна возвращать новый список, элементами которого
являются числа из списка numbers, имеющие ту же четность,
что и первый элемент этого списка.
'''

numbers_1 = [6, 0, 67, -7, 10, -20]
numbers_2 = []
numbers_3 = [-7, 0, 67, -9, 70, -29, 90]

def same_parity(x):
    y = []
    l = len(x)
    if l != 0:
        if x[0] % 2 == 0:
            for i in range(l):
                if x[i] % 2 == 0:
                    y.append(x[i])
        else:
            for i in range(l):
                if x[i] % 2 != 0:
                    y.append(x[i])
    return y

print(same_parity(numbers_1))
print(same_parity(numbers_2))
print(same_parity(numbers_3))
