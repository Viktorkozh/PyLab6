#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Введите слово: ")

    for i in range(3, len(word) + 1, 3):
        word = word[:i-1] + 'a' + word[i:]

print(word)
