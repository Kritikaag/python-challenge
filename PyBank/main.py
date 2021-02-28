

# Module for reading CSV files
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('.', 'budget_data.csv')

# Recdcdnth_list = []
profit_loss_list = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        month_list.append(str(row[0]))
        profit_loss_list.append(int(row[1]))

        #print(row)

#print(month_list)
#print(profit_loss_list)

print("Financial Analysis")
print("----------------------------")
total_months = len(month_list)
print("Total Months: ",total_months)

##net total amount of "Profit/Losses" over the entire period

net_profit = 0

for row_index in profit_loss_list :
    net_profit = row_index + net_profit

print("Total : $", net_profit)


#average of the changes in "Profit/Losses" over the entire period

average_monthly_change_list = []
previous_month = 0
for r in range(len(profit_loss_list)):
    if r == 0: 
        previous_month = profit_loss_list[r]
    else:
        monthly_change = profit_loss_list[r] - previous_month
        average_monthly_change_list.append(monthly_change)
        previous_month = profit_loss_list[r]


count = len(average_monthly_change_list)
total_net_change = sum(average_monthly_change_list)

avg_profit_loss = round(total_net_change / count, 2)

print("Average  Change: $",avg_profit_loss)

##greatest increase in profits (date and amount) over the entire period
grt_inc = max(average_monthly_change_list)

index = average_monthly_change_list.index(grt_inc)

x = month_list[index + 1]      # adding 1 to index so as to get the grt inc month
print("Greatest Increase in Profits:",x, grt_inc)


##greatest decrease in losses (date and amount) over the entire period

grt_dec = min(average_monthly_change_list)
index = average_monthly_change_list.index(grt_dec)

y = month_list[index + 1]
print("Greatest decrease in Profits:",y, grt_dec)