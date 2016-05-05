#!/usr/bin/env python
#encoding:UTF-8

#选择
def choose_fun(s, object_fun):
    #将最小的个体替换为最大的个体       
    s_max=max(s, key=lambda x:object_fun(x) )#找出最大的个体
    s_min=min(s, key=lambda x:object_fun(x) )#找出最小的个体
    loc_max=s.index(s_max)              #找出最大的个体位置
    loc_min=s.index(s_min)              #找出最小的个体位置
    s[loc_min]=s_max 
