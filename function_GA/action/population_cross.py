#!/usr/bin/env python
#encoding:UTF-8

import random

#交叉
def cross_fun(s, alfa):

    rand_table=range(0, len(s))         #生成种群的下标位表
    random.shuffle(rand_table)          #将下标位表随机化 

    """
    按照随机化的下标位表， 将种群两两交叉
    """
    for i in range(0, int(len(s)*alfa), 2):
        """
        在DNA单条下标位中（不包括0位）随机选取一个交叉位点
        """
        j = random.randint(1,len(s[0])-1 )

        temp0 = s[rand_table[i]][j:]
        temp1 = s[rand_table[i+1]][j:]
        s[rand_table[i]] = s[rand_table[i]][0:j]+temp1
        s[rand_table[i+1]] = s[rand_table[i+1]][0:j]+temp0

