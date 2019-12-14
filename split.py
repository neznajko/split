#!                                          /usr/bin/env python3
#                                          -*- coding: utf-8 -*-
#    Okay, we'll represent a tree as an n-tuple, vhere the first
#  element is the node nombre, and the next two elements are the
#            left and the right sub-trees. For example 1-tree is 
#         represented as (1, (), ()), 2-tree as (2, (1, (), ()),
#                                       (1, (), ())), and so on.
import sys #_____|______________________________________________
root = 13 #______|_____________________________ main tree nombre
if sys.argv[1:]: root = int(sys.argv[1]) #______________________
forest = [[] for j in range(root + 1)] #_____ all root sub-trees
debug = False #__|___________________________________ debug flag
def odd(n): return (n & 1) #___________ ck least significant bit
def bld4(n): #___|___________________  \___________ build forest
    forest[1].append((1, (), ())) #  \____________ terminal node
    for j in range(2, n + 1):
        split = j >> 1
        if not odd(j):
            for t in forest[split]:
                forest[j].append((j, t, t))
        else:
            for p in range(1, split + 1):
                q = j - p
                for u in forest[p]:
                    for v in forest[q]:
                        forest[j].append((j, u, v))
                        ########################################
                    ########################   ## ###   ####  ##
                ############################ ## # ### ## ## # ##
            ################################   ## ### ## # ## ##
        #################################### ## # ### ## #     #
    ########################################   ##   #   ##### ##
################################################################
def dump3(indent, t):
    if not t: return
    print(f"{indent}{t[0]}")
    dump3(indent + " ", t[1])
    dump3(indent + " ", t[2])
bld4(root)                 #     #     #     #     #     #     #
def set3(stk, t):         ###   ###   ###   ###   ###   ###   ##
    if not t: return stk ##### ##### ##### ##### ##### ##### ###
    n = t[0]            ######################################## 
    if n not in stk: stk.append(n) #############################
    stk = set3(stk, t[1])          #############################
    stk = set3(stk, t[2])          # w h a t   i s   t h i s ? #
    return stk                     #############################
def gerhemin(n):
    min_len = float('inf') # . . . . . . . . . . . . . . . . . .
    stk = [] #. . . . . . . . . . . . . . . stack with solutions
    for t in forest[root]: # 
        set_len = len(set3([], t)) #
        if set_len < min_len: #
            min_len = set_len #
            stk.clear() #
        elif set_len > min_len: # 
            continue #
        stk.append(t) # . . . . . . . . . . . . . . . . . . . .
    return stk # . . . . . . . . . . . . . . . . . . . . . . . .
def salute(aux, t):
    if t[0] == 1 or t[0] in aux: return
    print(f"X{t[0]}=X{t[1][0]}*X{t[2][0]}")
    aux.append(t[0])
    salute(aux, t[1])
    salute(aux, t[2])
if debug: ######################################################
    for t in forest[root]:
        dump3("", t)
        print()
        print(set3([], t))
for t in gerhemin(root):
    salute([], t)
    print()
########################################################### log:
