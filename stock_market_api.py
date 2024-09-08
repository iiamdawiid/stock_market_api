import requests
import json
from api_key import API_KEY

# API_URL = f'https://api.polygon.io/v1/open-close/AAPL/2023-01-09?adjusted=true&apiKey={API_KEY}'

# response = requests.get(API_URL)
# data = response.json()
# print(json.dumps(data, indent=4))

def main():
    start_menu()

def start_menu():
    # ask user to select crypto or stock
    # after user selects then display a menu of options - for now just start with open/close data
    print("INVESTING BUDDY".center(30, "="))
    print("1: Stocks\n2: Crypto")
    print("".center(30, "="))
    while True:
        try:
            user_choice = int(input("Enter '1' or '2': "))
            if user_choice not in {1, 2}:
                print("Invalid input. Please enter a valid choice.")
            else:
                break
            
        except ValueError:
            print("Invalid input. Please enter a number.")

    if user_choice == 1:
        # call stock_menu() to display stock options (no not those options you filthy degenerate)
        stock_menu()
    else:
        # call stock_menu() to display crypto options
        crypto_menu()


def stock_menu():
    # only one option for now - open/close data for specific day
    ...

def get_stock_info():
    ...

def fetch_stock_info():
    ...

def crypto_menu():
    ...

def get_crypto_info():
    ...

def fetch_stock_info():
    ...

if __name__ == "__main__":
    main()