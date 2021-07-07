"""
Проверить, является ли число степенью двойки.
Вернуть True или False
Является ли число степенью 2
"""
import math


def is_pow_2(number) -> bool:
    if math.log(number, 2).is_integer():
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_pow_2(4)
    assert is_pow_2(16)
    assert is_pow_2(256)
    assert not is_pow_2(123)
    print("Решено")
