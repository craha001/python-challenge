import os
import csv

totalmonths = 0
totalprofits = 0

#month to month changes list to match up with profit/loss changes list
mtm_changes = [] 

#profit/loss differences between each row
profit_loss_changes = [] 

#profit/loss row list
profit_loss = [] 

#path to csv file
csv_budget_data = os.path.join('PyBank', 'Resources', 'budget_data.csv') 
with open(csv_budget_data) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        totalmonths += 1 #total months
        totalprofits += int(row[1]) #total profits
        profit_loss.append(int(row[1])) #profit/loss list
        mtm_changes.append(row[0]) #dates list

#getting the profit loss changes for average change equation
for i in range(1, len(profit_loss)):
    profit_loss_changes.append(profit_loss[i] - profit_loss[i - 1]) 

average_change = sum(profit_loss_changes) / len(profit_loss_changes) #average change equation 
average_change_total = round(average_change, 2) #rounding average change
ginc_profits = max(profit_loss_changes) #greatest increase in profits 
gdec_profits = min(profit_loss_changes) #greatest decrease in profits
gmax_date = mtm_changes[profit_loss_changes.index(ginc_profits) + 1] #month the greatest increase occurred in
gmin_date = mtm_changes[profit_loss_changes.index(gdec_profits) + 1] #month the greatest decrease occurred in

#results list turns into the text file for our financial analysis to export to the file
results = [
    "Financial Analysis",
    "---------------------------",
    f"Total Months: {totalmonths}",
    f"Total: ${totalprofits}",
    f"Average Change: ${average_change_total}",
    f"Greatest Increase in Profits: {gmax_date} ${ginc_profits}",
    f"Greatest Decrease in Profits: {gmin_date} ${gdec_profits}"
]

#prints each line from above and prints them into line
for line in results:
    print(line)

#text file output
output_file = os.path.join('PyBank', 'analysis', 'PyBank_results.txt')
with open(output_file, 'w') as f:
    for line in results:
        f.write(line + '\n')

