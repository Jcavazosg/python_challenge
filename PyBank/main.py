import os 
import csv

csvpath = os.path.join('Resources/budget_data.csv')

number_months = []
budget_profit = []
monthly_change = []

with open(csvpath, newline="") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader: 
        number_months.append(row[0])
        budget_profit.append(int(row[1]))
        
    for x in range(len(budget_profit)-1):
        monthly_change.append(budget_profit[x+1]-budget_profit[x])
        
    max_increase = max(monthly_change)
    monthly_max_increase = monthly_change.index(max(monthly_change)) + 1
    
    max_decrease = min(monthly_change)
    monthly_max_increase = monthly_change.index(min(monthly_change)) + 1

output_path = os.path.join(".", 'BudgetAnalysis.txt')

with open (output_path, 'w') as txt: 
    txt.write("Budget Analysis")
    txt.write("\n")
    txt.write("-----------------")
    txt.write("\n")
    txt.write(f"Total Months: {len(number_months)}")
    txt.write("\n")
    txt.write(f"Total: ${sum(budget_profit)}")
    txt.write("\n")
    txt.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    txt.write("\n")
    txt.write(f"Greatest Increase in Profits: {number_months[monthly_max_increase]} (${(str(max_increase))})")
    txt.write("\n")
    txt.write(f"Greatest Decrease in Profits: {number_months[monthly_max_increase]} (${(str(max_decrease))})")





  














