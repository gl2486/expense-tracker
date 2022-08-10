

import requests
import json
import pandas as pd
from pandas import read_csv, DataFrame
import os
import datetime
#import plotly.express as px
import plotly.graph_objects as go



def convert_currency(currency_base, currency_output, cost):
    request_url = f"https://api.exchangerate.host/latest?base={currency_base}&symbols={currency_output}&amount={cost}&places=2"
    response = requests.get(request_url)
    data = json.loads(response.text)
    #print(type(data))
    #print(data.keys())
    conversion_amt = data['rates'][f'{currency_output}']

    return conversion_amt


def list_currency():
    #https://exchangerate.host/#/#docs
    request_url = "https://api.exchangerate.host/symbols"
    response = requests.get(request_url)
    data = json.loads(response.text)
    symbols = data['symbols']
    currency_list = list(symbols.keys())

    return currency_list


def input_expense():

    ##https://exchangerate.host/#/#docs
    #request_url = "https://api.exchangerate.host/symbols"
    #response = requests.get(request_url)
    #data = json.loads(response.text)
    #symbols = data['symbols']
    #currency_list = list(symbols.keys())
    currency_list = list_currency()

    #CURRENCY INPUT VALIDATION
    while True:
        currency_output = input("Enter <BASE> currency code [e.g. USD]: ").upper()
        if currency_output not in currency_list:
            print("please input valid currency code")
            continue
        else:
            break

    item = input("Enter item: ")

    #CATEGORY INPUT VALIDATION
    cat_lists = ['auto/gas', 'bill/utility', 'education', 'entertainment', 'food/drink', 'misc', 'shopping', 'travel']
    print('-'*60)
    print('Categories:')
    for cat_list in range(len(cat_lists)):
        print(cat_list, cat_lists[cat_list])
    print('-'*60)
    while True:
        cat = input(f"Enter <{item}> category no.: ")
        try:
            cat_num = int(cat)
            if 0 <= cat_num <= 7:
                cat_obj = cat_lists[cat_num]
                break
            else:
                print("Please try again")
                continue
        except ValueError:
            print('please input valid category no.')
            continue

    #COST INPUT VALIDATION
    while True:
        cost = input(f"Enter <{item}> amount: ")
        try: 
            cost_obj = float(cost)
            #print(cost_obj)
            break
        except ValueError:
            print("please input valid amount")
            continue

    #CURRENCY INPUT VALIDATION
    while True:
        currency_base = input(f"Enter <{cost}> currency code: ").upper()
        if currency_base not in currency_list:
            print("please input valid currency code")
            continue
        else:
            break
    
    #DATE INPUT VALIDATION
    while True:
        date = input("Enter date [MMDDYYYY]: ")
        date_format = '%m%d%Y'
        try:
            date_obj = datetime.datetime.strptime(date, date_format).strftime("%Y-%m-%d")
            #print(date_obj)
            break
        except ValueError:
            print("Incorrect data format, should be MMDDYYYY")
            continue

    #CURRENCY CONVERSION
    #request_url = f"https://api.exchangerate.host/latest?base={currency_base}&symbols={currency_output}&amount={cost}&places=2"
    #response = requests.get(request_url)
    #data = json.loads(response.text)
    ##print(type(data))
    ##print(data.keys())
    #conversion_amt = data['rates'][f'{currency_output}']
    conversion_amt = convert_currency(currency_base, currency_output, cost)

    df = pd.DataFrame({'Item':[item],'Cost':[cost_obj], 'Currency':[currency_base], f'{currency_output}':[conversion_amt], 'Category':[cat_obj], 'Date':[date_obj]})
    
    print('-'*60)
    print(df)
    print('-'*60)

    while True:
        add_row = input("Enter [A] to add expense, [D] to delete expense, or any 'key' to end: ").upper()

        if add_row == "A":

            item = input("Enter item: ")
            
            #CATEGORY INPUT VALIDATION
            cat_lists = ['auto/gas', 'bill/utility', 'education', 'entertainment', 'food/drink', 'misc', 'shopping', 'travel']
            print('-'*60)
            for cat_list in range(len(cat_lists)):  
                print(cat_list, cat_lists[cat_list])
            print('-'*60)
            while True:
                cat = input(f"Enter <{item}> category no.: ")
                try:
                    cat_num = int(cat)
                    if 0 <= cat_num <= 7:
                        cat_obj = cat_lists[cat_num]
                        break
                    else:
                        print("Please try again")
                        continue
                except ValueError:
                    print('please input valid category no.')
                    continue

            
            #COST INPUT VALIDATION
            while True:
                cost = input(f"Enter <{item}> amount: ")
                try: 
                    cost_obj = float(cost)
                    #print(cost_obj)
                    break
                except ValueError:
                    print("please input valid amount")
                    continue


            #CURRENCY INPUT VALIDATION
            while True:
                currency_base = input(f"Enter <{cost}> currency code: ").upper()
                if currency_base not in currency_list:
                    print("please input valid currency code")
                    continue
                else:
                    break
            

            #DATE INPUT VALIDATION
            while True:
                date = input("Enter date [MMDDYYYY]: ")
                date_format = '%m%d%Y'
                try:
                    date_obj = datetime.datetime.strptime(date, date_format).strftime("%Y-%m-%d")
                    #print(date_obj)
                    break
                except ValueError:
                    print("Incorrect data format, should be MMDDYYYY")
                    continue


            #CURRENCY CONVERSION
            #request_url = f"https://api.exchangerate.host/latest?base={currency_base}&symbols={currency_output}&amount={cost}&places=2"
            #response = requests.get(request_url)
            #data = json.loads(response.text)
            ##print(type(data))
            ##print(data.keys())
            #conversion_amt = data['rates'][f'{currency_output}']
            conversion_amt = convert_currency(currency_base, currency_output, cost)

            df2 = pd.DataFrame({'Item':[item],'Cost':[cost_obj], 'Currency':[currency_base], f'{currency_output}':[conversion_amt], 'Category':[cat_obj], 'Date':[date_obj]})
            df = pd.concat([df,df2], ignore_index=True)
            print('-'*60)
            print(df)
            print('-'*60)
            continue

        elif add_row == "D":
        
            delete_row = input("Do you want to delete expense row? [input no.]: ")
            try:
                delete_row_obj = int(delete_row)
                if 0 <= delete_row_obj <= len(df.index):
                    df.drop({delete_row_obj}, inplace=True)
                    df.reset_index(drop=True, inplace=True)
                    print('-'*60)
                    print(df)
                    print('-'*60)
                else:
                    print("Please try again")
                continue
            except ValueError:
                print('Please input valid row number')
                continue
    
        else:
            list_ = [f'{currency_output}']
            df.loc['Total',:] = df[list_].sum()
            print('-'*60)
            print(df.sort_values(by='Date'))
            print('-'*60)
            break
    

    #Exporting CSV
    while True:
        export_csv = input("Do you want to export expense report to .CSV file? [Y/N]: ").upper()
        if export_csv == "Y":
            #csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data")
            df.sort_values(by='Date').to_csv(f"{csv_filepath}/my_expense.csv", index=False)
            break
        elif export_csv == "N":
            print("Thank you for using 'International Expense Tracker', Goodbye!")
            break
        else:
            print("Please try again")
            continue


    #df_group = df.groupby(['Category'])[f'{currency_output}'].sum()
    #print(df_group)

    my_pivot = df.groupby(["Category"]).agg({f'{currency_output}': ['sum']})
    #my_pivot.columns = ["_".join(col) for col in my_pivot.columns.ravel()]
    my_pivot.columns = ["_".join(col) for col in my_pivot.columns.values]
    #print(my_pivot)


    #GENERATE PIE CHART
    values = my_pivot[f'{currency_output}_sum'].tolist()
    labels = my_pivot.index.values.tolist()

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                insidetextorientation='radial'
                                )])
    fig.update_layout(title_text='Expense Category Breakdown')

    fig.show()
    print("Thank you for using 'International Expense Tracker', Goodbye!")
    quit()

if __name__ == "__main__":

    ##https://exchangerate.host/#/#docs
    #request_url = "https://api.exchangerate.host/symbols"
    #response = requests.get(request_url)
    #data = json.loads(response.text)
    #symbols = data['symbols']
    #currency_list = list(symbols.keys())
    currency_list = list_currency()


    #READ CSV
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data")

    while True:
        if os.path.exists(f"{csv_filepath}/my_expense.csv"):
            df = read_csv(f"{csv_filepath}/my_expense.csv", skipfooter=1 , engine='python')
            print('-'*60)
            print(df)
            print('-'*60)
            column_list = df.columns.tolist()
            currency_output = column_list[3]

            new_report = input("Do you want to delete existing report? [Y/N]: ").upper()

            if new_report =="Y":
                os.remove(f"{csv_filepath}/my_expense.csv")
                input_expense()

            if new_report == "N":
                while True:
                    add_row = input("Enter [A] to add expense, [D] to delete expense, or any 'key' to end: ").upper()

                    if add_row == "A":

                        item = input("Enter item: ")
                        
                        #CATEGORY INPUT VALIDATION
                        cat_lists = ['auto/gas', 'bill/utility', 'education', 'entertainment', 'food/drink', 'misc', 'shopping', 'travel']
                        print('-'*60)
                        for cat_list in range(len(cat_lists)):  
                            print(cat_list, cat_lists[cat_list])
                        print('-'*60)
                        while True:
                            cat = input(f"Enter <{item}> category no.: ")
                            try:
                                cat_num = int(cat)
                                if 0 <= cat_num <= 7:
                                    cat_obj = cat_lists[cat_num]
                                    break
                                else:
                                    print("Please try again")
                                    continue
                            except ValueError:
                                print('please input valid category no.')
                                continue

                        
                        #COST INPUT VALIDATION
                        while True:
                            cost = input(f"Enter <{item}> amount: ")
                            try: 
                                cost_obj = float(cost)
                                #print(cost_obj)
                                break
                            except ValueError:
                                print("please input valid amount")
                                continue


                        #CURRENCY INPUT VALIDATION
                        while True:
                            currency_base = input(f"Enter <{cost}> currency code: ").upper()
                            if currency_base not in currency_list:
                                print("please input valid currency code")
                                continue
                            else:
                                break
                        

                        #DATE INPUT VALIDATION
                        while True:
                            date = input("Enter date [MMDDYYYY]: ")
                            date_format = '%m%d%Y'
                            try:
                                date_obj = datetime.datetime.strptime(date, date_format).strftime("%Y-%m-%d")
                                print(date_obj)
                                break
                            except ValueError:
                                print("Incorrect data format, should be MMDDYYYY")
                                continue


                        #CURRENCY CONVERSION
                        #request_url = f"https://api.exchangerate.host/latest?base={currency_base}&symbols={currency_output}&amount={cost}&places=2"
                        #response = requests.get(request_url)
                        #data = json.loads(response.text)
                        ##print(type(data))
                        ##print(data.keys())
                        #conversion_amt = data['rates'][f'{currency_output}']
                        conversion_amt = convert_currency(currency_base, currency_output, cost)


                        df2 = pd.DataFrame({'Item':[item],'Cost':[cost_obj], 'Currency':[currency_base], f'{currency_output}':[conversion_amt], 'Category':[cat_obj], 'Date':[date_obj]})
                        df = pd.concat([df,df2], ignore_index=True)
                        print('-'*60)
                        print(df)
                        print('-'*60)
                        continue

                    elif add_row == "D":
                    
                        delete_row = input("Do you want to delete row? [input no.]: ")
                        try:
                            delete_row_obj = int(delete_row)
                            if 0 <= delete_row_obj <= len(df.index):
                                df.drop({delete_row_obj}, inplace=True)
                                df.reset_index(drop=True, inplace=True)
                                print('-'*60)
                                print(df)
                                print('-'*60)
                            else:
                                print("Please try again")
                            continue
                        except ValueError:
                            print('Please input valid row number')
                            continue
                
                    else:
                        list_ = [f'{currency_output}']
                        df.loc['Total',:] = df[list_].sum()
                        print('-'*60)
                        print(df.sort_values(by='Date'))
                        print('-'*60)
                        break
                

                #Exporting CSV
                while True:
                    export_csv = input("Do you want to export expense report to .CSV file? [Y/N]: ").upper()
                    if export_csv == "Y":
                        #csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data")
                        df.to_csv(f"{csv_filepath}/my_expense.csv", index=False)
                        break
                    elif export_csv == "N":
                        print("Thank you for using 'International Expense Tracker', Goodbye!")
                        break
                    else:
                        print("Please try again")
                        continue

                my_pivot = df.groupby(["Category"]).agg({f'{currency_output}': ['sum']})
                #my_pivot.columns = ["_".join(col) for col in my_pivot.columns.ravel()]
                my_pivot.columns = ["_".join(col) for col in my_pivot.columns.values]
                #print(my_pivot)

                #GENERATE PIE CHART
                values = my_pivot[f'{currency_output}_sum'].tolist()
                labels = my_pivot.index.values.tolist()

                fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                            insidetextorientation='radial'
                                            )])
                fig.update_layout(title_text='Expense Category Breakdown')
                fig.show()
                print("Thank you for using 'International Expense Tracker', Goodbye!")
                quit()

        else:
            input_expense()


    #values = [1, 10, 1000]
    #labels = ['food', 'travel', 'shopping']
    #
    #fig = px.pie(names = labels, values = values, title = 'our chart')
    #fig.show()