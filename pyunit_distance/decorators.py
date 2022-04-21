#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time  : 2022/4/21 15:28
# @Email: jtyoui@qq.com
import functools
import re


class ParameterNotEmptyError(Exception):
    """参数不能为空"""
    pass


class CoordinateLengthNotEqualError(Exception):
    """坐标维数不相等"""
    pass


def parameter_set_length(fun):
    """参数集合长度验证修饰器"""

    @functools.wraps(fun)
    def wraps(x, y):
        if not (x and y):
            raise ParameterNotEmptyError("参数不能为空")
        if len(x) != len(y):
            raise CoordinateLengthNotEqualError("两个参数长度不一致")
        return fun(x, y)

    return wraps


def replace_regular(re_, replace_):
    """根据正则来修改参数

    :param re_: 匹配的正则
    :param replace_: 替换正则的数据
    :return: 被替换完毕的参数
    """
    r = re.compile(re_)

    def remove_replace(fun):

        @functools.wraps(fun)
        def wraps(*args, **kwargs):
            args_, kwargs_ = list(args), {}
            for i in range(len(args)):
                if isinstance(args[i], str):
                    args_[i] = r.sub(replace_, args[i])
                else:
                    args_[i] = args[i]
            for k, v in kwargs.items():
                if isinstance(v, str):
                    kwargs_.setdefault(k, r.sub(replace_, v))
                else:
                    kwargs_.setdefault(k, v)

            return fun(*args_, **kwargs_)

        return wraps

    return remove_replace
