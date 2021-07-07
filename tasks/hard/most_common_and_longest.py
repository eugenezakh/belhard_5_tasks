"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Напишите программу, которая принимает текст и выводит два слова:
наиболее часто встречающееся и самое длинное.

можно решить с помощью циклов и переменных, но предпочтительней с
помощью модуля collections, используя collections.Counter
"""
from collections import Counter

def common_and_longest(text: str) -> tuple:
    temp = text.split()
    common = Counter(temp).most_common(1)
    common = common[0][0]
    for i in range(len(temp) - 1):
        if len(temp[i]) > len(temp[i + 1]):
            longest = temp[i]
    return common, longest


if __name__ == '__main__':
    assert common_and_longest(
        "привет пока ялюблюpython привет"
    ) == ('привет', 'ялюблюpython')
    print('Решено!')
