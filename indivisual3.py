#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    s = input("Введите слово: ")
    n = int(input("На место какой переставить первую букву: ")) - 1
    
    # Проверить требуюемую длину.
    if len(s) < n:
        print(
            "Заданная буква должна быть не больше длины длины слова",
            file=sys.stderr
        )
        exit(1)

    first_letter = s[:1 - len(s)]
    word = s[1 - len(s):] # без первой
    word = word[:n] + first_letter + word[n:]
    
    print(word)