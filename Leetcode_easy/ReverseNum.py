#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def reverse_num(num):
    """

    :param num: int
    :return: num (int)
    """
    x = int(str(num)[::-1]) if num >= 0 else - int(str(num)[::-1])
    return x if abs(x) < (2**31) else 0


if __name__ == '__main__':
    print(reverse_num(num=2**35))
