#!/usr/bin/env python
#encoding:UTF-8

import random

#初始化
def start_fun(l_sep, l_len, s):    #l_sep 种群个体长度   l_len 种群个数
    #二进制位数           DNA条数
    for i in range(l_len):
        s0 = ''
        for i in range(l_sep):
            si = str(random.randint(0, 1))
            s0 = s0 + si
        s.append(s0)

