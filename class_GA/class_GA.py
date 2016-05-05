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


class Genetic(object):
    def __init__(self, bit_len, p_n, alfa, belta, object_fun, N):
        #初始化
	self.s=[]#存放种群的列表
        self.bit_len=bit_len#个体二进制位长度
	self.p_n=p_n#种群个体数
	self.alfa=alfa#交叉率
	self.belta=belta#变异率
	self.object_fun=object_fun#目标函数
	self.N=N#迭代次数

        p_init.start_fun(self.bit_len, self.p_n, self.s)

    def choose_fun(self, s, object_fun):#选择
	c_max_min.choose_fun(s, object_fun)
    def cross_fun(self, s, alfa):#交叉
	p_cross.cross_fun(s, alfa)    
    def change_fun(self, s, belta):#变异
	p_change.change_fun(s, belta)

    def run(self):
        for i in xrange(N):# N 100000 :  迭代的次数
    	    self.choose_fun(self.s, self.object_fun)  #选择
            self.cross_fun(self.s, self.alfa)    #交叉
            self.change_fun(self.s, self.belta)   #变异


#目标函数
#p 为每个DNA个体的二进制表示， 即 "11010101"
def object_fun(p):
    object_value = int(p[0:], 2)**2
    return object_value
        

#a为生成的实例
a=Genetic(bit_len, p_n, alfa, belta, object_fun, N)
a.run()
print a.s
