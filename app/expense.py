


import requests
import json
import pandas as pd
from pandas import DataFrame



def input_expense():


    item = input("Enter item: ")
    cost = float(input("Enter cost: "))
    date = input("Enter date: ")

    df = pd.DataFrame({'Item':[item],'Cost':[cost], 'Date':[date]})
    
    print(df)

    while True:
        add_row = input("Do you want to add another expense? [Y/N]: ").upper()

        if add_row == "Y":
            item = input("Enter item: ")
            cost = input("Enter cost: ")
            date = input("Enter date: ")

            df2 = pd.DataFrame({'Item':[item],'Cost':[cost], 'Date':[date]})
            df = pd.concat([df,df2], ignore_index=True)

            print(df)
            continue
        else:

            print(df)
            break

input_expense()


