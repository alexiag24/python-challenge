import pandas as pd
import os 
import csv

#set path for file 
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def analyze_financial_records(financial_data):
    """
    Analyze financial records and display various metrics.
    """
    months = set()
    net_profit_losses = 0
    changes = []
    previous_profit_loss = None
    greatest_increase = {'date': '', 'amount': 0}
    greatest_decrease = {'date': '', 'amount': 0}

    for record in financial_data:
        revenue = record['revenue']
        expenses = record['expenses']
        timestamp = record['timestamp']
        year_month = datetime.strptime(timestamp, '%Y-%m-%d').strftime('%Y-%m')
        months.add(year_month)

        profit_loss = revenue - expenses
        net_profit_losses += profit_loss

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            if change > greatest_increase['amount']:
                greatest_increase['amount'] = change
                greatest_increase['date'] = timestamp
            elif change < greatest_decrease['amount']:
                greatest_decrease['amount'] = change
                greatest_decrease['date'] = timestamp

        previous_profit_loss = profit_loss

        print(f"Timestamp: {timestamp}")
        print(f"Profit/Loss: {profit_loss}\n")

    total_months = len(months)
    average_change = sum(changes) / len(changes)
    print(f"Total number of months: {total_months}")
    print(f"Net Total Profit/Losses: {net_profit_losses}")
    print(f"Changes in Profit/Losses: {changes}")
    print(f"Average Change in Profit/Losses: {average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")


# Example financial data
financial_data = [
    {'timestamp': '2022-01-15', 'revenue': 1000000, 'expenses': 800000},
    {'timestamp': '2022-02-20', 'revenue': 1200000, 'expenses': 900000},
    {'timestamp': '2022-03-10', 'revenue': 1500000, 'expenses': 1000000},
    {'timestamp': '2022-02-25', 'revenue': 800000, 'expenses': 700000},
    {'timestamp': '2022-03-18', 'revenue': 1100000, 'expenses': 900000}
]

analyze_financial_records(financial_data)