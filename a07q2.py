##
##----------------------------
## Nitish Joshi (20811051)
## CS 116, Winter 2019
## Assignment 7, Question 2
##---------------------------
##
import check

## An Entry is a (list Str Nat), where the first value is a 
##    key, and the second value is the occurrence count, the
##    number of times that key has been searched for. 


def adjusted_linear_search(db, target):
    '''
    returns the new number of occurances of the target in the list db, by mutating the list with given rules.
    
    adjusted_linear_search: (listof Entry) Str -> Nat
    
    Examples: 
    adjusted_linear_search([["a",6],["k",3]],"k") => 4
    adjusted_linear_search([["a",6],["k",3]],"u") => 1
    '''
    i=0
    for item in db:
        if item[0]==target:
            if i!=0:
                item[1] += 1
                new = db[i-1]
                db[i-1] = item
                db[i] = new
            else:
                item[1] += 1
            return item[1]
        elif i==len(db)-1:
            db.append([target,1])
            return 1
        i += 1

db1 = [["e",4], ["few",1], ["do",3], ["hi",1], ["aa",3]]
#Tests:
check.expect("Test#1",adjusted_linear_search([["h",2],["t",90],["j",2],["n",2]],"j"),3)
check.expect("Test#1",adjusted_linear_search([["x",2],["z",1],["v",5],["b",5]],"j"),1)
