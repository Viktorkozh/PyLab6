#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    words_that_start_with_H = 0
    words_that_end_with_P = 0
    s = input("Введите предложение: ")

    words = s.split(' ')

    for i in range(len(words) - 1):
        word = str(words[i])
        if word[0] == 'н' or word[0] == 'Н':
            words_that_start_with_H += 1
        if word[-1].isalpha():
            if word[-1] == 'р' or word[-1] == 'Р':
                words_that_end_with_P += 1
        else:
            if word[-2] == 'р' or word[-2] == 'Р':
                words_that_end_with_P += 1

    print("Начинающиеся с буквы н: ", words_that_start_with_H)
    print("Оканчивающиеся буквой р: ", words_that_end_with_P)
