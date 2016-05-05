#!/usr/bin/python
#encoding:UTF-8
import random
import time
import action.population_init as p_init
import action.choose_max_min as c_max_min
import action.population_cross as p_cross
import action.population_change as p_change

random.seed(time.time())

N=1000#迭代的次数
alfa=0.6#交叉率
belta=0.01#变异率
p_n=100#DNA 条数
bit_len=8#每条DNA 二进制位长度

s=[]#存放种群的列表


#目标函数
#p 为每个DNA个体的二进制表示， 即 "11010101"
def object_fun(p):
    object_value = int(p, 2)**2
    return object_value
        



#主函数
p_init.start_fun(bit_len, p_n, s)#初始化

for i in xrange(N):# N 100000 :  迭代的次数

    c_max_min.choose_fun(s, object_fun)  #选择
    
    p_cross.cross_fun(s, alfa)    #交叉

    p_change.change_fun(s, belta)   #变异

print s
