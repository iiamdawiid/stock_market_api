import requests
import json
from api_key import API_KEY
import sys

# API_URL = f'https://api.polygon.io/v1/open-close/AAPL/2023-01-09?adjusted=true&apiKey={API_KEY}'

# response = requests.get(API_URL)
# data = response.json()
# print(json.dumps(data, indent=4))


def main():
    start_menu()


def start_menu():
    # ask user to select crypto or stock
    # after user selects then display a menu of options - for now just start with open/close data
    print("\n" + "INVESTING BUDDY".center(30, "="))
    print("0: Quit\n1: Stocks\n2: Crypto")
    print("".center(30, "="))
    while True:
        try:
            user_choice = int(input("Enter choice: "))
            if user_choice not in {0, 1, 2}:
                print("Invalid input. Please enter a valid choice.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    if user_choice == 0:
        sys.exit("\n*Program Terminated*")
    elif user_choice == 1:
        # call stock_menu() to display stock options (no not those options you filthy degenerate)
        stock_menu()
    else:
        # call stock_menu() to display crypto options
        crypto_menu()


def stock_menu():
    # only one option for now - open/close data for specific day
    print("\n" + "STOCKS".center(30, "="))
    print("0: Go Back\n1: Daily Open/Close")
    print("".center(30, "="))
    while True:
        try:
            stock_menu_choice = int(input("Enter choice: "))
            # will have to alter conditional later if more options added
            if stock_menu_choice not in {0, 1}:
                print("Invalid input. Please enter a valid choice.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    if stock_menu_choice == 0:
        start_menu()
    elif stock_menu_choice == 1:
        # call func to collect stock choice from user
        get_stock_info()


def crypto_menu():
    print("\n" + "CRYPTO".center(30, "="))
    print("0: Go Back\n1: Daily Open/Close")
    print("".center(30, "="))
    while True:
        try:
            crypto_menu_choice = int(input("Enter choice: "))
            if crypto_menu_choice not in {0, 1}:
                print("Invalid input. Please enter a valid choice.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    if crypto_menu_choice == 0:
        start_menu()
    elif crypto_menu_choice == 1:
        get_crypto_info()


def get_stock_info(): ...


def fetch_stock_info(): ...


def get_crypto_info(): ...


def fetch_stock_info(): ...


if __name__ == "__main__":
    main()
