##
##----------------------------
## Nitish Joshi (20811051)
## CS 116, Winter 2019
## Assignment 7, Question 3
##---------------------------
##
import check
## Question 3

## A Player is a list of length >=2, where
##   * the first entry in Player is of type Str
##   * the remaining entries in Player are of type Nat. 

# a.
def vowel_sort(words):
    '''
    returns the list 'words' by sorting the strings according to number of vowels in the word.
    
    vowel_sort: (listof Str) -> (listof Str)
    
    requires: Non-empty list of Strings in 'words'. Srings must be lowercase strings.
    
    Examples:
    vowel_sort(["aiw","ab","aiuoobc","aab"]) => ["ab","aiw","aab","aiuoobc"]
    vowel_sort(["joy","sad","anger","disgust","fear","inside","out"]) => ["joy","sad","anger","disgust","fear","out","inside"]
    '''
    def is_vowel(char):
        if char in "aeiou":
            return True
        else:
            return False
    def vowel_count(item):
        length = len(list(filter(is_vowel,item)))
        return length
    words.sort(key=vowel_count)
    return words
    
#Tests:
check.expect("Test#1",vowel_sort(["king","kong","gone","to","jungle"]),['king', 'kong', 'to', 'gone', 'jungle'])
check.expect("Test#2",vowel_sort(["what","to","do","now"]),['what', 'to', 'do', 'now'])

# b.
def player_basic_sort(competitors):
    '''
    mutates the list competitors by sorting the on basis of minimum score and in descending order.
    
    player_basic_sort: (listof Player) -> None
    
    requires: list must have no. of Players >= 2.
    Examples:
    player_basic_sort([["A",3,2,6,3,4],["S",1,3,2,8,9]]) => None
    '''
    competitors.sort(key=lambda item: min(item[1:]), reverse = True)

#Tests:
check.expect("Test#1",player_basic_sort([["D",8,2,3,7,4],["J",9,5,6,7,8],["K",4,7,5,6,9]]),None)
check.expect("Test#2",player_basic_sort([["O",3,5,5,5,5],["R",7,8,2,2,4]]),None)
check.expect("Test#3",player_basic_sort([["P",1,9,10,6,9],["W",4,8,6,7,7],["Z",2,7,4,11,8],["B",8,9,10,11,9]]),None)

#c. 
def player_full_sort(competitors):
    '''
    mutates the list competitors by sorting them on the basis of the min-score then on max_score and then on the name of the Player.
    
    player_full_sort: (listof Player) -> None
    
    requires:  atleast 2 players in the list.
    
    Examples:
    player_full_sort([["A",3,2,6,3,4],["S",1,3,2,8,9]]) => None
    '''
    lst=[]
    lst=competitors
    lst=(sorted((sorted((sorted(competitors,key=lambda item: item[0])),key= lambda item: max(item[1:]),reverse=True)),key= lambda item: min(item[1:]),reverse=True))
#Tests:
check.expect("Test#1",player_full_sort([["D",8,2,3,7,4],["J",9,5,6,7,8],["K",4,7,5,6,9]]),None)
check.expect("Test#2",player_full_sort([["O",3,5,5,5,5],["R",7,8,2,2,4]]),None)
check.expect("Test#3",player_full_sort([["P",1,9,10,6,9],["W",4,8,6,7,7],["Z",2,7,4,11,8],["B",8,9,10,11,9]]),None)
