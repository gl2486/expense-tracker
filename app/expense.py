
import requests
import json
import pandas as pd
#from pandas import DataFrame
import datetime
            

def input_expense():

    request_url = "https://api.exchangerate.host/symbols"
    response = requests.get(request_url)
    data = json.loads(response.text)

    symbols = data['symbols']
    currency_list = list(symbols.keys())

    #CURRENCY INPUT VALIDATION
    while True:
        currency_output = input("Enter <BASE> currency code: ").upper()
        if currency_output not in currency_list:
            print("please input valid currency code")
            continue
        else:
            break

    item = input("Enter item: ")

    #CATEGORY INPUT VALIDATION
    cat_lists = ['auto/gas', 'bill/utility', 'education', 'entertainment', 'food/drink', 'misc', 'shopping', 'travel']
    print('-'*50)
    for cat_list in range(len(cat_lists)):  
        print(cat_list, cat_lists[cat_list])
    print('-'*50)
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
        currency_base = input(f"Enter <{cost}> currency: ").upper()
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
            date_obj = datetime.datetime.strptime(date, date_format)
            #print(date_obj)
            break
        except ValueError:
            print("Incorrect data format, should be MMDDYYYY")
            continue

    #CURRENCY CONVERSION
    request_url = f"https://api.exchangerate.host/latest?base={currency_base}&symbols={currency_output}&amount={cost}&places=2"
    response = requests.get(request_url)
    data = json.loads(response.text)
    #print(type(data))
    #print(data.keys())
    conversion_amt = data['rates'][f'{currency_output}']


    df = pd.DataFrame({'Item':[item],'Cost':[cost_obj], 'Currency':[currency_base], f'{currency_output} Amount':[conversion_amt], 'Category':[cat_obj], 'Date':[date_obj]})
    
    print(df)

    while True:
        add_row = input("Enter [A] to add expense, [D] to delete expense, or any 'key' to generate report: ").upper()

        if add_row == "A":

            item = input("Enter item: ")
            
            #CATEGORY INPUT VALIDATION
            cat_lists = ['auto/gas', 'bill/utility', 'education', 'entertainment', 'food/drink', 'misc', 'shopping', 'travel']
            print('-'*50)
            for cat_list in range(len(cat_lists)):  
                print(cat_list, cat_lists[cat_list])
            print('-'*50)
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
                currency_base = input(f"Enter <{cost}> currency: ").upper()
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
                    date_obj = datetime.datetime.strptime(date, date_format)
                    #print(date_obj)
                    break
                except ValueError:
                    print("Incorrect data format, should be MMDDYYYY")
                    continue


            #CURRENCY CONVERSION
            request_url = f"https://api.exchangerate.host/latest?base={currency_base}&symbols={currency_output}&amount={cost}&places=2"
            response = requests.get(request_url)
            data = json.loads(response.text)
            #print(type(data))
            #print(data.keys())
            conversion_amt = data['rates'][f'{currency_output}']

            df2 = pd.DataFrame({'Item':[item],'Cost':[cost_obj], 'Currency':[currency_base], f'{currency_output} Amount':[conversion_amt], 'Category':[cat_obj], 'Date':[date_obj]})
            df = pd.concat([df,df2], ignore_index=True)

            print(df)
            continue

        elif add_row == "D":
        
            delete_row = input("Do you want to delete row? [input no.]: ")
            try:
                delete_row_obj = int(delete_row)
                if 0 <= delete_row_obj <= len(df.index):
                    df.drop({delete_row_obj}, inplace=True)
                    df.reset_index(drop=True, inplace=True)
                    print(df)
                else:
                    print("Please try again")
                continue
            except ValueError:
                print('Please try again')
                continue
    
        else:
            list_ = [f'{currency_output} Amount']
            df.loc['Total',:] = df[list_].sum()
            print(df.sort_values(by='Date'))
            break

input_expense()


#def generate_chart():