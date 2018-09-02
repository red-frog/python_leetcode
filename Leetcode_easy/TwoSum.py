#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def two_sum(nums, target):
    """
    :param nums: list[int]
    :param target: int
    :return: list
    """
    dic = dict()
    alist = list()
    for i, num in enumerate(nums):
        if num in dic:
            alist.append((dic[num], i))
        dic[target-num] = i
    return alist


if __name__ == '__main__':
    nums = [2, 7, 3, 6, 11, 22]
    target = 9
    print(two_sum(nums=nums, target=target))