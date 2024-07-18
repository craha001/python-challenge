import os
import csv

totalmonths = 0
totalprofits = 0
mtm_changes = []
profit_loss_changes = []
profit_loss = []

csv_budget_data = os.path.join('PyBank', 'Resources', 'budget_data.csv')
with open(csv_budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        totalmonths += 1
        totalprofits += int(row[1])
        profit_loss.append(int(row[1]))
        mtm_changes.append(row[0])

for i in range(1, len(profit_loss)):
    profit_loss_changes.append(profit_loss[i] - profit_loss[i - 1])

average_change = sum(profit_loss_changes) / len(profit_loss_changes)
average_change_total = round(average_change, 2)
ginc_profits = max(profit_loss_changes)
gdec_profits = min(profit_loss_changes)
gmax_date = mtm_changes[profit_loss_changes.index(ginc_profits) + 1]
gmin_date = mtm_changes[profit_loss_changes.index(gdec_profits) + 1]

results = [
    "Financial Analysis",
    "---------------------------",
    f"Total Months: {totalmonths}",
    f"Total: ${totalprofits}",
    f"Average Change: ${average_change_total}",
    f"Greatest Increase in Profits: {gmax_date} ${ginc_profits}",
    f"Greatest Decrease in Profits: {gmin_date} ${gdec_profits}"
]

for line in results:
    print(line)

output_file = os.path.join('PyBank', 'analysis', 'PyBank_results.txt')
with open(output_file, 'w') as f:
    for line in results:
        f.write(line + '\n')

