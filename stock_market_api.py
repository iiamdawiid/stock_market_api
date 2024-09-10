import requests
import json
from api_key import API_KEY
import sys
from datetime import datetime
from tabulate import tabulate

RED = '\033[91m'
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


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


def validate_date(date):
    try:
        valid_date = datetime.strptime(date, "%Y-%m-%d")
        if valid_date > datetime.now():
            print("Date can not be in the future.")
            return False
        # return True will only execute if valid date format; else exception is raised
        return True

    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
        return False


def get_stock_info():
    # ask user to input the ticker for whatever stock they want
    print("\n" + "STOCKS: Open/Close".center(30, "="))
    while True:
        try:
            stock_ticker = input("Enter stock ticker symbol: ").upper()

            if not stock_ticker.isalpha():
                raise ValueError("Invalid input. Please enter valid ticker symbol.")
            else:
                break

        except ValueError as e:
            print(e)

    while True:
        date = input("Enter any date (YYYY-MM-DD): ")
        # check to see if date entered is valid
        if validate_date(date):
            break

    fetch_stock_info(stock_ticker, date)


def get_crypto_info():
    print("\n" + "STOCKS: Open/Close".center(30, "="))
    while True:
        try:
            crypto_ticker = input("Enter crypto ticker symbol: ").upper()

            if not crypto_ticker.isalpha():
                raise ValueError("Invalid input. Please enter valid ticker symbol.")
            else:
                break

        except ValueError as e:
            print(e)

    while True:
        date = input("Enter any date (YYYY-MM-DD): ")
        if validate_date(date):
            break

    fetch_crypto_info(crypto_ticker, date)


def fetch_stock_info(stock_ticker, date):
    # here is where we will make an api call and receive Open/Close data for stock on specified date
    STOCK_API_URL = f"https://api.polygon.io/v1/open-close/{stock_ticker}/{date}?adjusted=true&apiKey={API_KEY}"

    try:
        response = requests.get(STOCK_API_URL)
        # response.raise_for_status() automatically raises exception for HTTP error status codes
        # makes it easier to handle server-side errors without manually checking the response.status_code after each api call
        response.raise_for_status()
        data = response.json()

        if data.get("status") == "NOT FOUND":
            print(f"Error: {data['message']}")
        else:
            # use tabulate to display data
            # print(json.dumps(data, indent=4))
            table = [
                ["Date", data["from"]],
                ["Symbol", f'{RED}{data["symbol"]}{RESET}'],
                ["Pre-Market", f'{YELLOW}{data["preMarket"]}{RESET}'],
                ["Open", f'{GREEN}{data["open"]}{RESET}'],
                ["High", f'{GREEN}{data["high"]}{RESET}'],
                ["Low", f'{GREEN}{data["low"]}{RESET}'],
                ["Close", f'{GREEN}{data["close"]}{RESET}'],
                ["After-Hours", f'{YELLOW}{data["afterHours"]:.2f}{RESET}'],
                ["Volume", f'{RED}{data["volume"]}{RESET}'],
            ]
            print(tabulate(table, tablefmt="heavy_grid"))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


def fetch_crypto_info(crypto_ticker, date):
    CRYPTO_API_URL = f"https://api.polygon.io/v1/open-close/crypto/{crypto_ticker}/USD/{date}?adjusted=true&apiKey={API_KEY}"

    try:
        response = requests.get(CRYPTO_API_URL)
        response.raise_for_status()
        data = response.json()

        if data.get("open") == 0:
            print(f"Error: Crypto not found")
        else:
            print(json.dumps(data, indent=4))

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
