##
##----------------------------
## Nitish Joshi (20811051)
## CS 116, Winter 2019
## Assignment 7, Question 4
##---------------------------
##
import check
## Question 4

def nat_sort(values,upper): 
    '''
    returns the sorted list via steps as in the question.
    
    nat_sort: (listof Nat) Nat -> (listof Nat)
    
    requires: upper >= any entry in values
    Examples:
    nat_sort([1,4,2,3],6) => [1,2,3,4]
    nat_sort([3,0,0,5,1,2],8) => [0,0,1,2,3,5]
    '''
    counts=[]
    i=0
    while i<=upper:
        counts.append(0)
        i += 1
    for item in values:
        counts[item] += 1
    lst=[]
    k=0
    for item in counts:
        while item>0:
            lst.append(k)
            item -= 1
        k +=1
    return lst
            
#Tests:
check.expect("Test#1",nat_sort([0,3,1,5,0,2,2],10),[0,0,1,2,2,3,5])
check.expect("Test#2",nat_sort([7,1,3,3,1,2,7,5,4],7),[1,1,2,3,3,4,5,7,7])
check.expect("Test#3",nat_sort([11,31],35),[11,31])

    