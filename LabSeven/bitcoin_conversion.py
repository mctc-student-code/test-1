import requests

def main():
    currency = get_target_currency()
    bitcoin = get_number_of_bitcoins()
    converted = convert_bitcoin_to_target(bitcoin, currency)
    display_result(bitcoin, currency, converted)

def get_target_currency():
    #Get target currency
    currency = input("Enter target currency code e.g. USD, CNY: ")
    return currency.upper()

def get_number_of_bitcoins():
    #Get number of bitcoin
    bitcoin = float(input('Enter the number of bitcoins: '))
    return bitcoin

def convert_bitcoin_to_target(bitcoin, target_currency):
    #Convert amount of bitcoin to target currency
    exchange_rate = get_exchange_rate(target_currency)
    converted = convert(bitcoin, exchange_rate)
    return converted
    
def get_exchange_rate(currency):
    #Call API with currency as parameter
    response = request_rates(currency)
    rate = extract_rate(response, currency)
    return rate

def request_rates(currency):
    #Perform API request and return response
    params = currency
    url = 'https://api.coindesk.com/v1/bpi/currentprice/' + params
    return requests.get(url).json()

def extract_rate(rate, currency):
    #Process JSON response and extract rate information
    return rate['bpi'][currency]['rate_float']

def convert(amount, exchange_rate):
    #Convert bitcoin to target currency using given exchange rate
    return amount * exchange_rate

def display_result(bitcoin, currency, converted):
    #Format and print information to screen
    print(f'{bitcoin} bitcoin is equal to {currency} {converted}')

if __name__ == '__main__' :
    main()