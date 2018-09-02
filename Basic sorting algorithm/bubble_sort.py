#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
author:frog
date:2018.09.02
"""


def bubble_sort(alist):
    unsorted_list_index = len(alist) - 1
    have_sorted = False
    while not have_sorted:
        have_sorted = True
        for i in range(unsorted_list_index):
            if alist[i] > alist[i+1]:
                have_sorted = False
                alist[i], alist[i+1] = alist[i+1], alist[i]
        unsorted_list_index -= 1
    return alist


if __name__ == '__main__':
    unsorted_list = [34, 12, 25, 67, 320]
    sorted_list = bubble_sort(alist=unsorted_list)
    print(sorted_list)