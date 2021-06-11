##
##----------------------------
## Nitish Joshi (20811051)
## CS 116, Winter 2019
## Assignment 8, Question 4
##---------------------------
##
import check
## Question 4

class Trader:
  ''' Fields:  name(Str), stocks_owned(dictof Str Nat), init_cash(Float)
    requires: stocks_owned is a dictionary mapping from the 
               names of stocks to the positive number of shares 
               of that stock held by this trader.
              init_cash is non-negative.
  '''
  def __init__(self, name, stocks, init_cash):
    self.name = name
    self.stocks_owned = stocks
    self.cash = init_cash
  def __repr__(self):
    return "Trader: {0}\nStocks: {1}\nCurrent Cash Value: {2}".format(
      self.name, list(map(lambda x: x + " Shares: " + str(self.stocks_owned[x]),
                          self.stocks_owned.keys())), self.cash)  
class Stock:
  ''' Fields: symbol(Str), prices(list of Float)
    requires: each value in prices is non-negative.
  '''
  def __init__(self, name, init_value):
    self.symbol = name
    self.prices = [init_value]
  def __repr__(self):
    return "Stock: {0}\nCurrent Value: {1}".format(self.symbol, self.prices[-1])  

def minimal_majority(company, traders):
  '''
  returns tthe list of minimum number of traders who can buy the maximum number 
  of stocks.
  
  minimal_majority: (listof Stock Int) Trader : (listof Str)
  requires: unique Traders
  
  Examples:
  apple = Stock ( " APPL " ,3.0)
  microsoft = Stock ( " MSFT " ,2.75)
  warren_buffet = Trader ( " Warren Buffet " , { apple.symbol : 30 , microsoft.symbol : 100} , 1000000000.0)
  tim_cook = Trader ( " Tim Cook " , { apple.symbol : 45} , 1000000000.0)
  paul_tudor_jones = Trader ( " Paul Tudor Jones " , { apple . symbol : 20} , 1000000000.0)
  minimal_majority ([ apple , 140] ,[ warren_buffet , tim_cook , paul_tudor_jones ]) => 
  [ " Tim Cook " , " Warren Buffet " ]
  '''
  traders.sort(key=lambda item: item.stocks_owned[company[0].symbol], reverse =True)
  req_min_stocks = company[1]//2
  sum_stocks = 0
  list_traders = []
  for trader in traders:
    sum_stocks += trader.stocks_owned[company[0].symbol]
    list_traders.append(trader.name)
    if sum_stocks>=req_min_stocks:
      list_traders.sort()
      return list_traders
    
#Tests:
sony = Stock ( " Sony " ,3.0)
samsung = Stock ( " SamSung " ,2.75)
quilquo_rana = Trader ( " Quilidara Rana " , { sony . symbol : 12 , samsung .symbol : 100} , 4455000.0)
tony_kilki = Trader ( " Tony Kiliont " , { samsung . symbol : 65, sony.symbol:65} , 912000000.0)
drula_lipa = Trader ( " drulalae lipa " , { sony . symbol : 20} ,250000.0)
check.expect("Test#1",minimal_majority ([ sony , 150] ,[ quilquo_rana , tony_kilki ,drula_lipa ]),[" Tony Kiliont "," drulalae lipa " ])

apple = Stock ( " APPL " ,3.0)
microsoft = Stock ( " MSFT " ,2.75)
warren_buffet = Trader ( " Warren Buffet " , { apple.symbol : 30 , microsoft.symbol : 100} , 1000000000.0)
tim_cook = Trader ( " Tim Cook " , { apple.symbol : 45} , 1000000000.0)
paul_tudor_jones = Trader ( " Paul Tudor Jones " , { apple . symbol : 20} , 1000000000.0)
check.expect("Test#2",minimal_majority ([ apple , 90] ,[ warren_buffet , tim_cook , paul_tudor_jones ]),[" Tim Cook "])