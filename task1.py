#!python3
"""
Create a function that converts the price of Bitcoin into Canadian Dollars .
The function will require 2 input parameters:
float: amount of currency being converted

return: float value in Canadian Dollars
You will make use of a local variable called "currBTC"
currBTC shows that the conversion is 1 btc = 45000 cad

Sample assertions:

assert btcTocad(1) == 45000
(2 points) 
"""

def btcTocad(amount):
    currbtc = 45000
    if isinstance(amount, (int, float)):
        return float(amount * currbtc)
    else:
        return 'error'




if __name__ == "__main__":
    assert btcTocad(1) == 45000
    assert btcTocad(2.5) == 112500
    assert btcTocad('one') == 'error'
