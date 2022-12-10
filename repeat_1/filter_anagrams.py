'''
Реализуйте функцию, которая принимает два аргумента в следующем порядке:
word — слово в нижнем регистре
words — список слов в нижнем регистре
Функция должна возвращать список, элементами которого являются слова из списка words,
которые представляют анаграмму слова word. Если список words пуст или не содержит
анаграмм, функция должна вернуть пустой список.

Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.
Примечание 2. Считайте, что слово является анаграммой самого себя.
'''

def filter_anagrams(word, words):
    letter_list = []
    words_list = []
    if len(words) != 0:
        for i in range(len(word)):
            letter_list.append(word[i])
        for w in words:
            if len(letter_list) == len(w):
                counter = len(w)
                w_ok = w
                for letter in letter_list:
                    if w.find(letter) != -1:
                        w = w.replace(letter,'', 1)
                        counter -= 1
                        if counter == 0:
                            words_list.append(w_ok)
                            break
                        continue
                    break
    return words_list


word = 'abba'
words = ['aabb', 'abcd', 'bbaa', 'dada']
print(filter_anagrams(word, words))

print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))

print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))

print(filter_anagrams('стекло', []))