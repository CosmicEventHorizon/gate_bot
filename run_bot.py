from file_io import *
from gate_io import *

def automatic_order(API_KEY, API_SECRET):
    currency = input("Currency to buy: ")
    amount = input("Amount to buy in USD: ")
    buy_trigger = float(input("Price of "+ currency +" to buy: "))
    sell_trigger = float(input("Price of "+ currency +" to sell: "))
    while True:
        market_price = fetch_currecy_pair_price(currency)
        print(f"Current market price of {currency} is {market_price}")
        if market_price<buy_trigger:
            print(buy_currency(API_KEY,API_SECRET,currency,amount,market_price))
            break
        time.sleep(2)
    while True:
        market_price = fetch_currecy_pair_price(currency)
        print(f"Current market price of {currency} is {market_price}")
        if market_price>=sell_trigger:
            print(sell_max_currency(API_KEY,API_SECRET,currency))
            break
        time.sleep(2)


if __name__ == '__main__':
    API_KEY, API_SECRET = read_token() if all(read_token()) else create_token()
    while True:
        #List menu items
        print("Please choose a transaction:\n")
        print("1 - List all currencies")
        print("2 - Buy a currency")
        print("3 - Sell a currency")
        print("4 - Place an automatic order\n")
        choice = int(input("Choice: "))
        
        #Call function based on choice
        if choice == 1:
            print(fetch_currecy_pair())
        elif choice == 2:
            currency = input("Currency to buy: ")
            amount = input("Amount to buy in USD: ")
            price = input("Price of " +currency+ " to buy: ")
            print()
            print(buy_currency(API_KEY,API_SECRET,currency,amount,price))
        elif choice == 3:
            currency = input("Currency to sell: ")
            print()
            print(sell_max_currency(API_KEY,API_SECRET,currency))
        elif choice == 4:
            automatic_order(API_KEY,API_SECRET)
