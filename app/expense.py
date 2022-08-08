import requests
import json
import pandas as pd
from pandas import DataFrame



def input_expense():

    request_url = "https://api.exchangerate.host/symbols"
    response = requests.get(request_url)
    data = json.loads(response.text)

    symbols = data['symbols']
    currency_list = list(symbols.keys())

    while True:
        currency_output = input("Enter <BASE> currency code: ").upper()
        if currency_output not in currency_list:
            print("please input valid currency code")
            continue
        else:
            break

    
    item = input("Enter item: ")
    cost = float(input("Enter cost: "))
    while True:
        currency_base = input("Enter currency: ").upper()
        if currency_base not in currency_list:
            print("please input valid currency code")
            continue
        else:
            break
    cat = input("Enter category: ")
    date = input("Enter date: ")


    request_url = f"https://api.exchangerate.host/latest?base={currency_base}&symbols={currency_output}&amount={cost}&places=2"
    response = requests.get(request_url)
    data = json.loads(response.text)
    #print(type(data))
    #print(data.keys())
    conversion_amt = data['rates'][f'{currency_output}']


    df = pd.DataFrame({'Item':[item],'Cost':[cost], 'Currency':[currency_base], f'{currency_output} Amt':[conversion_amt], 'Category':[cat], 'Date':[date]})
    
    print(df)

    while True:
        add_row = input("Do you want to add another expense? [Y/N]: ").upper()

        if add_row == "Y":
            item = input("Enter item: ")
            cost = input("Enter cost: ")
            while True:
                currency_base = input("Enter currency: ").upper()
                if currency_base not in currency_list:
                    print("please input valid currency code")
                    continue
                else:
                    break
            cat = input("Enter category: ")
            date = input("Enter date: ")

            request_url = f"https://api.exchangerate.host/latest?base={currency_base}&symbols={currency_output}&amount={cost}&places=2"
            response = requests.get(request_url)
            data = json.loads(response.text)
            #print(type(data))
            #print(data.keys())
            conversion_amt = data['rates'][f'{currency_output}']

            df2 = pd.DataFrame({'Item':[item],'Cost':[cost], 'Currency':[currency_base], f'{currency_output} Amt':[conversion_amt], 'Category':[cat], 'Date':[date]})
            df = pd.concat([df,df2], ignore_index=True)

            print(df)
            continue
        else:
            
            #delete_row = int(input("Delete row [input row #]"))
            #df.drop(index = {delete_row})

            list_ = [f'{currency_output} Amt']
            df.loc['Total',:] = df[list_].sum()
            
            print(df)
            break

input_expense()
