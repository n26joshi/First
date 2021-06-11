##
##----------------------------
## Nitish Joshi (20811051)
## CS 116, Winter 2019
## Assignment 8, Question 1
##---------------------------
##
import check
## Question 1

#Q1

def invert_dictionary(d):
  '''
  consumes a dictionary d of the form (dictof Str (listof
  Int)) and returns an inverted dictionary of the form (dictof Int (listof Str)) 
  with the items in alphabetical order.
  
  invert_dictionary: (dictof Str (listof Int)) -> (dictof Int (listof Str))
  
  Examples:
  invert_dictionary({'s':[1,2],'g':[3,1]}) => {1:['g','s'],2:['s'],3:['g']}
  '''
  new_dict={}
  for item in d:
    for n_item in d[item]:
      if n_item in new_dict:
        new_dict[n_item].append(item)
      else:
        new_dict[n_item] = [item]
  for item in new_dict:
    new_dict[item].sort()
  return new_dict

#Tests:
check.expect("Test#1",invert_dictionary({'r':[1,2],'f':[4,2],'c':[1,4]}),{1:['c','r'],2:['f','r'],4:['c','f']})
check.expect("Test#2",invert_dictionary({'y':[16,8],'o':[9,12]}),{16:['y'],8:['y'],9:['o'],12:['o']})