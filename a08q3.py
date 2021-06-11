##
##----------------------------
## Nitish Joshi (20811051)
## CS 116, Winter 2019
## Assignment 8, Question 3
##---------------------------
##
import check
## Question 3
#Q3

class Stock:
  ''' Fields: symbol(Str), prices(list of Float)
    requires: each value in prices is non-negative.
  '''
  def __init__(self, name, init_value):
    self.symbol = name
    self.prices = [init_value]
    
  def __eq__(self,other):
    return (isinstance(other, Stock) and
            self.symbol == other.symbol and
            len(self.prices) == len(other.prices) and
            len(self.prices) == len(list(filter(
              lambda x: abs(self.prices[x] - other.prices[x])< 0.000001, 
              range(len(self.prices))))))
     
  
  def __repr__(self):
    return "Stock: {0}\nCurrent Value: {1}".format(self.symbol, self.prices[-1])
  
  def update_prices(self, new_prices):
    '''
    adds the input list of stock prices to the existing price(s)
    by siply adding them to the end of the exising list.
    
    update_prices: Stock (listof Float): None
    requires: prices must be non-negative
    
    Examples:
    stock1 = Stock("S1",4.5)
    stock1.update_prices([2.3,1.2,66.0]) => None
    '''
    (self.prices) += new_prices
  
  def average(self, n):
    ''' 
    returns the average of the last n entries of prices in the prices field in a Stock.
    
    average: Stock Nat : Float
    
    requires: non-negative 'n'.
    
    Examples:
    stock.2 = Stock("S2",[3.2,6.7,12.3,9.0])
    stock2.average(2) => 10.65
    '''
    new=(self.prices)[len(self.prices)-n:]
    return sum(new)/len(new)
  
#Tests for update_prices and average:
#Tests for update_prices...
vordo = Stock("voRDo",8.6)
check.expect("Test#1",vordo.update_prices([3.9,8.6,9.0,7.7]),None)

dikoa = Stock("DA",1.9)
check.expect("Test#2",dikoa.update_prices([88.9]),None)

#Tests for average...
dora = Stock("dorAA",3)
dora.update_prices([4.5,6.2,5.7,8.1,9.0,4.0,5.5])
check.within("Test#1",dora.average(3),6.17,0.01)

bvce = Stock("bE",2)
bvce.update_prices([1.9,7,7,1.0])
check.within("Test#2",bvce.average(1),1.0,0.0001)
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
      
  def __eq__(self, other):
    return (isinstance(other, Trader) and
            self.name == other.name and
            abs(self.cash - other.cash) < 0.00001 and
            self.stocks_owned == other.stocks_owned)
            
  
  def __repr__(self):
    return "Trader: {0}\nStocks: {1}\nCurrent Cash Value: {2}".format(
      self.name, list(map(lambda x: x + " Shares: " + str(self.stocks_owned[x]),
                          self.stocks_owned.keys())), self.cash)
  
  def buy_stocks(self, s, n):
    '''
    returns True if the trader is capable of buying n stocks and false otherwise.
    
    buy_stocks: Trader Stock Nat: Bool
    
    requires: non-negative n.
    
    Examples:
    Deluso = Trader("DeLuso",{},16555.0)
    Deluso.buy_stocks(dora,6) => True
    
    Gin = Trader("Gin",{"dora":19},100)
    Gin.buy_stocks(bvce,110) => False
    '''
    price_of_stocks=n*s.prices[-1]
    if self.cash>=price_of_stocks:
      if s.symbol not in self.stocks_owned:
        self.stocks_owned[s.symbol] = n
      else:
        self.stocks_owned[s.symbol] += n
      self.cash -= price_of_stocks
      return True
    else:
      return False
    
  def sell_stocks(self, s, n):
    '''
    returns True if trader has n or more than n stocks else False.
    
    sell_stocks: Trader Stock Nat -> Bool
    require: non-negative n
    
    Examples:
    winke = Trader("Winke",{},754345.07)
    winke.sell_stocks(bvce,9) => False
    
    Gin = Trader("Gin",{"dora":19},87555)
    Gin.sell_stocks(dora,10) => True
    '''
    if s.symbol in self.stocks_owned and (self.stocks_owned[s.symbol])>=n:
      price_of_stocks = n*s.prices[-1]
      dic={}
      for stock in self.stocks_owned:
        if stock == s.symbol and (self.stocks_owned[stock]) - n != 0:
          self.stocks_owned[stock] -= n
          dic[stock]=self.stocks_owned[stock]
        elif stock!=s.symbol:
          dic[stock]=self.stocks_owned[stock]
      self.stocks_owned = dic
      self.cash += price_of_stocks
      return True
    else:
      return False

#Tests for buy_stocks and sell_stocks:
#Tests for buy_stocks...
bvce = Stock("bE",2)
bvce.update_prices([1.9,7,7,1.0])
alcara = Trader("Alessia",{},9000000.00)
check.expect("Test#1",alcara.buy_stocks(bvce,10),True)

dora = Stock("dorAA",3)
dora.update_prices([4.5,6.2,5.7,8.1,9.0,4.0,5.5])
seinna = Trader("Seinna miller",{"ukon":29},85.0001)
check.expect("Test#2",seinna.buy_stocks(dora,93),False)

#Tests fro sell_stocks...
dikoa = Stock("DA",1.9)
dikoa.update_prices([3.4,5.1,5.8,5.9])
trea = Trader("Troy Nealle",{"grt":99},9870)
check.expect("Test#1",trea.sell_stocks(dikoa,68),False)

apple = Stock ( " APPL " , 3.0)
apple . update_prices ([3.01 , 3.5 , 3.42 , 3.64 , 3.41 , 4.2 , 4.3 , 5.21 ,5.13 , 4.66 , 5.21 , 5.31 , 5.5 , 5.57 , 4.56 ])
warren_buffet = Trader ( " Warren Buffet " , {" APPL ":20} , 1000000000.0)
check.expect("Test#2",warren_buffet.sell_stocks(apple,20),True)