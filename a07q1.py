##
##----------------------------
## Nitish Joshi (20811051)
## CS 116, Winter 2019
## Assignment 7, Question 1
##---------------------------
##
import check
## Make sure to follow question 1 as directed.

# Question 1. 
#
# Determine the worst-case runtime of the following functions. 
# The answer will be stated in terms of the size of the problem.
# Some bounds may appear more than once.
#
# Note. In all cases, choose the 'tightest' bound from:
# A. O(1)
# B. O(log n)
# C. O(n)
# D. O(n log n)
# E. O(n**2)
# F. O(2**n)

# (a)
# Let n = len(L)

def fn_a(L):
    L1 = list(filter(lambda x: x%2==0, L))
    L2 = list(map(lambda y: 2*y, L1))
    L3 = list(map(lambda z: z%2, L2))
    return L3

# (b)
# Let n = len(L)

def fn_b(L):
    if L == []: 
        return 0
    if len(L) == 1:
        return L[0]
    mid = len(L) // 2
    s1 = fn_b(L[:mid])
    s2 = fn_b(L[mid:])
    return s1+s2
    

# (c)
# Let n = len(L)

def fn_c(L):
    return list(map(lambda k: list(map(lambda x: x*k, list(range(len(L))))), L))


# (d)
# Let n be a natural number

def fn_d(n):
    
    def help_d(x):
        v = 1
        for q in range(x):
            v = v + q*q
        return v
       
    t = 0
    for i in range(n):
        t = t + help_d(i)
    return t


# (e)
# Let n be a natural number

def fn_e(n): 
    if n == 0: 
        return 1000
    if n == 1: 
        return -1000
    f1 = abs(fn_e(n-1))
    f2 = abs(fn_e(n-2))
    if f1 + f2 == 0:
        return 0
    elif f1 * f2 >= 0:
        return f1
    else:
        return f2

# (f)
# Let n = len(L)
    
def fn_f(L):
    M = []
    for i in range(len(L)):
        for j in range(len(L)):
            M.append(i*j + i)
    return M
            

# Place one of A,B,C,D,E or F inside the string quotes;
# e.g., if you think fn_a has a running time of O(2**n),
# then change a_answer = "" to a_answer = "F".
#
# In all cases, choose the 'tightest' bound from:
# A. O(1)
# B. O(log n)
# C. O(n)
# D. O(n log n)
# E. O(n**2)
# F. O(2**n)

a_answer = "C"
b_answer = "B"
c_answer = "E"
d_answer = "E"
e_answer = "F"
f_answer = "E"