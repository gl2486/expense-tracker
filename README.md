# Expense Tracker

This is a python application that allows you to create an expense tracker for your personal or professional expenses! You can convert from one currency to another and generate a report with a pie chart.

# Setup 

Optionally fork or close this [remote repository](https://github.com/gl2486/expense-tracker) to create a copy under your own control. Then "clone" or download the remove repository (or your forked copy) onto your local computer, for example your Desktop. Then navigate to wherever you downloaded the repo using the Terminal, e.g.:

```
cd ~/Desktop/expense-tracker
```

Create a virtual environment:

```
conda create -n expense-env python=3.8
```

Activate the virtual environment:
```
conda activate expense-env
```
Install package dependencies within the virtual environment:

```
pip install -r requirements.txt
```


# Usage
Once you have completed the setup described, above, you can now start running the program.

## Generate Expense Report

Run your expense report:

```
python app/expense.py
```

## Testing
Run tests:
```
pytest
```

# User Instructions

## Processing User Inputs
The application should prompt the user to input details of the expenses via command-line interface (CLI). For example:
+ base report currency code [e.g. USD]
    + note: This will serve as the currency that all your inputs are converted to
+ item description
+ select category option
+ cost amount
+ cost currency code [e.g. EUR]. This is the currency of your expense
+ date [e.g. MMDDYYYY format]

User will be able to add expenses or delete rows in the DataFrame within the program.

## Validating User Inputs
The application should compare the user's selections against the list of valid options for the various inputs to determine whether the user has selected a valid option to be included in the final expense report.

It should be able to handle various capitalizations and iterations of the valid options - especially with currency inputs (e.g., "usd", "USD" or "Usd").

If the selection is invalid, the program should display a friendly message to the user and prompt the user to try again. The program should not try to further process an invalid input as it may lead to runtime errors.

# Displaying the Results
As expenses are input into the program, the details are stored in a DataFrame and a preliminary report will be generated at the end.

# Demo

## Expense Data Input
```
Enter <BASE> currency code [e.g. USD]: USD
Enter item: Coffee
------------------------------------------------------------
Categories:
0 auto/gas
1 bill/utility
2 education
3 entertainment
4 food/drink
5 misc
6 shopping
7 travel
------------------------------------------------------------
Enter <Coffee> category no.: 4
Enter <Coffee> amount: 5.50
Enter <5.50> currency code: USD
Enter date [MMDDYYYY]: 08082022
------------------------------------------------------------
     Item  Cost Currency         USD    Category       Date
0  Coffee   5.5      USD         5.5  food/drink 2022-08-08
------------------------------------------------------------
Enter [A] to add expense, [D] to delete expense, or any 'key' to end:
```
## Preliminary Report

```
             Item    Cost Currency         USD    Category       Date
0          Coffee     5.5      USD        5.50  food/drink 2022-08-08
1  Flight Tickets  1000.0      EUR     1020.64      travel 2022-08-09
2        Sandwich     7.8      USD        7.80  food/drink 2022-08-08
3          Amazon   250.0      USD      250.00    shopping 2022-08-10
Total         NaN     NaN      NaN     1283.94         NaN        NaT

```

## Generate your expense report
If you prefer, you can generate your report and export it into a .csv file along with a pie chart that will open in your web browser.

## Storage (.csv file)
The .csv file will be in the "data" folder within the folder where your repo is saved on your computer, e.g.:

```
../Desktop/expense-tracker/data
```
You will be able to delete existing .csv if it exist, or continue editing the report when you run the program


