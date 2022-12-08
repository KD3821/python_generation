'''
Реализуйте функцию, которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать строку string:
полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
Примечание: Символы строки, не являющиеся буквами, следует игнорировать.
'''

def convert(x):
    up_count = 0
    low_count = 0
    if x.islower():
        low_count += 1
    elif x.isupper():
        up_count += 1
    else:
        for i in x:
            if i.isalpha():
                if i.islower():
                    low_count += 1
                else:
                    up_count += 1
    if up_count > low_count:
        string = x.upper()
    else:
        string = x.lower()
    return string


print(convert('BEEgeek'))
print(convert('pyTHON'))
print(convert('pi31415!'))