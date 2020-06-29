import os
import csv

#Define variables
total_months = 0
total_profit_loss = 0
total_change = 0
previous_month = 0
change = 0
greatest_increase = 0
greatest_decrease = 0
increase_month = 0
decrease_month = 0

# Path to collect data from the Resources folder
budget_csv = os.path.join("python-challenge\Resources",'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

 # Loop through the data
    for row in csvreader:

#Calculate total profit/loss
        total_profit_loss = int(row[1]) + total_profit_loss

        if total_months > 0: 
            change = (int(row[1]) - previous_month)
            total_change += change

            if (change) > greatest_increase: 
                greatest_increase = change
                increase_month = row[0]
    
            if (change) < greatest_decrease: 
                greatest_decrease = change
                decrease_month = row[0]

        total_months += 1
        previous_month = int(row[1])


#Display print statements
    average_change = total_change / (total_months - 1)

    print("Financial Analysis")

    print("-------------------")
    print(f"Total Months: {total_months}")

    print(f"Total: ${total_profit_loss}")

    print(f"Average Change: {average_change}")
  
    print(f"Greatest Increase in Profits: {increase_month} $({greatest_increase})")

    print(f"Greatest Decrease in Profits: {decrease_month} $({greatest_decrease})")

txtpath = os.path.join("python-challenge\pybank","Analysis.txt") 
with open(txtpath, 'w') as txtfile:

    txtfile.write("Financial Analysis \n")
    txtfile.write("------------------- \n")
    txtfile.write(f"Total Months: {total_months} \n")
    txtfile.write(f"Total: ${total_profit_loss} \n")
    txtfile.write(f"Average Change: {average_change} \n")
    txtfile.write(f"Greatest Increase in Profits: {increase_month} $({greatest_increase}) \n")
    txtfile.write(f"Greatest Decrease in Profits: {decrease_month} $({greatest_decrease}) \n")




