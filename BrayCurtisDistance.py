#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time  : 2022/4/21 15:28
# @Email: jtyoui@qq.com
from decorators import parameter_set_length


@parameter_set_length
def bray_curtis_distance(dimension_x, dimension_y):
    """
    布雷柯蒂斯距离

    Bray Curtis距离主要用于生态学和环境科学，计算坐标之间的距离。
    该距离取值在[0,1]之间。它也可以用来计算样本之间的差异。

    :param dimension_x: 一个维度的集合,不是一个点
    :param dimension_y: 另一个维度的集合.不是另一个点
    :return: 布雷柯蒂斯距离
    """
    all_ = []
    for x, y in zip(dimension_x, dimension_y):
        all_.append(abs(x - y))
    return sum(all_) / (sum(dimension_y) + sum(dimension_x))


if __name__ == '__main__':
    print(bray_curtis_distance([11, 0, 7, 8, 0], [24, 37, 5, 18, 1]))  # 0.5675675675675675
