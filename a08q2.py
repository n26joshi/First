##
##----------------------------
## Nitish Joshi (20811051)
## CS 116, Winter 2019
## Assignment 8, Question 2
##---------------------------
##
import check
## Question 2

#Q2

#Use Format with this string!
#Note: {0:.2f} will print the string 
# correct to two decimal places.
final_cost = "Final total: ${0:.2f}."

'''
  a Store is a (list Str (dictof Str Float)) consisting of a store's 
  name and the items they sell with their prices in a dictionary.
  requires: Each Str in the dictionary has positive Float values.
  a Shopping_List is a (listof Str)
  a Shopping_Trip is a (dictof Str (listof Str)) consisting of store 
  names and a list of items sold at the store
'''
def optimize_shopping(stores, goods):
  '''
    returns a new dictionary Shopping_trip with keys as the name of the stores
    where cheapest 'goods' are available. In this dictionary each stors has the list f goods as items that are bought at that store.
    it returns an empty dictionary if 'goods' is empty. The function prints the 
    total cost of the buying of goods trip.
    
    effects: prints final total cost of the trip.
    
    optimize_shopping: (listof Store) (listof Str) -> (dictof Str (listof Str))
    requires:  each element of goods is in atleast a single store, same items in different stores have different costs, goods do not contain repeated items and if stores is empty then goods must also be an empty list.
    
    Examples:
    stores = [["Costco",{'carrots':3.00,'beans':4.20,'garlic':2.85}],["Farmer Market",{'avocado':4.80,'cheese':6.20,'beans':3.50}],["walmart",{'beans':5.33,'cheese':8.99}]]
    
    optimize_shopping(stores,["beans","garlic"]) => Final cost: $6.35 /n {"Farmer Market":'beans',"Costco":'garlic'}
  '''
  Shopping_trip = {}
  final_total = 0
  for item in goods:
    for a_store in stores:
      if item in a_store[1]:
        min_price = a_store[1][item]
    for store in stores:
      if item in store[1] and store[1][item] <= min_price:
        min_price= store[1][item]
        Shopping_trip[item]= [store[0]]
    final_total += min_price
  print(final_cost.format(final_total))
  return invert_dictionary(Shopping_trip)
def invert_dictionary(d):
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
#Test1
stores = [
["Arnie's" ,{"apples" : 2.32 , "bananas" : 0.77 , "chickens" : 4.50}] ,
["Darlene's" ,{"apples" : 1.50 , "bananas" : 0.20 , "chickens" : 9.50}] ,
["Eddie's" ,{"grapefruits" : 3.31 , "bananas" : 0.97 , "beans" : 2.50}]]

shop_list = ["apples" , "bananas" , "grapefruits"]

check.set_screen("Final total: $5.01")
check.expect("Test#1", optimize_shopping(stores, shop_list), 
             { "Darlene's" :[ "apples" , "bananas" ] , "Eddie's" : [ "grapefruits" ]})
#Test2
stores1 = [
["Costco",{'carrots':3.00,'beans':4.20,'garlic':2.85}],
["walmart",{'beans':5.33,'cheese':8.99,'carrots':2.15}] ,
["Farmer Market",{'avocado':4.80,'cheese':6.20,'beans':3.50}]]
shop_list1 = ["avocado" , "carrots"]

check.set_screen("Final total: $6.95")
check.expect("Test#2", optimize_shopping(stores1, shop_list1), 
             { "Farmer Market" :["avocado"],"walmart":["carrots"]})

#Test3
shop_list2 = ["garlic" ]
check.set_screen("Final total: $2.85")
check.expect("Test#3", optimize_shopping(stores1, shop_list2), 
             { "Costco":["garlic"]})

#Test4
shop_list3 = ["chickens","beans"]
check.set_screen("Final total: $7.00")
check.expect("Test#4", optimize_shopping(stores, shop_list3), 
             { "Arnie's":["chickens"],"Eddie's":["beans"]})