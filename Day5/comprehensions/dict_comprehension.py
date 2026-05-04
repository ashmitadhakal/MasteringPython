

currencies=[
    ( "bitcoin","BTC"),
    ("litecoin","LTC"),
    ("ethereum","ETH")
]

# currency_dict = {}

# for curr_name, curr_symbol in currencies:
#     currency_dict[curr_name]=curr_symbol

# print(currency_dict)

currency_dict = {name: sym for name, sym in currencies}

print(currency_dict)