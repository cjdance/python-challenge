import os
import csv

# Path to collect data from csv in Resources folder
budget_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

#Create list to store Month data
month_list = []
#Create list to store Profit/Loss data for each month
profit_loss = []
#Create list to store output of monthly change in profit/loss
monthly_var = []

#Set function to find average
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

#Open and read csv file with bank data
with open(budget_csv,'r') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    header = next(csvreader)

    #Create list of month data and profit/loss data
    for row in csvreader:
        month_list.append(row[0])
        profit_loss.append(int(row[1]))

    #Get count of number of months in data
    num_month = len(month_list)
    #Calulate total of profit/loss
    total_pl = sum(profit_loss)

    #Calculate change in profit/loss each month
    #Set i as 1 lower than length of list to ensure it does not exceed list limits
    for i in range(num_month - 1):
        
        x = i + 1
        var1 = profit_loss[x]
        var2 = profit_loss[i]
        monthvar = var1 - var2
        monthly_var.append(monthvar)

#Calculate average monthly change in proft/loss using formula
ave_change = average(monthly_var)

#Round value of average to 2 decimal places as currency
ave_change = round(ave_change, 2)

#Find maximum and minimum monthly change in profit/loss
max_value = max(monthly_var)
max_index = monthly_var.index(max_value)
min_value = min(monthly_var)
min_index = monthly_var.index(min_value)

#Set index to find month in which max/min changes occurred
#Add 1 to each index due to difference in length for the lists
min_month_index = min_index + 1
max_month_index = max_index + 1

#Find months in which max/min changes occurred
min_month = month_list[min_month_index]
max_month = month_list[max_month_index]

#Identify path for text output file which will create file if it does not already exist or rewrite if it does
analysis = os.path.join("..", "PyBank","Analysis","Financial_Analysis.txt")

#Open text file for outputs of breakdown
f = open(analysis,'w')

#Print to console and txt file with \n forcing new lines in .txt file
print("Financial Analysis")
f.write("Financial Analysis \n")
print("----------------------------------")
f.write("----------------------------------\n")
print("Total Months: " + str(num_month))
f.write("Total Months: " + str(num_month) +"\n")
print("Total: $" + str(total_pl))
f.write("Total: $" + str(total_pl) + "\n")
print("Average Change: $" + str(ave_change))
f.write("Average Change: $" + str(ave_change) + "\n")
print("Greatest Increase in Profits: " + max_month + " ($" + str(max_value) +")")
print("Greatest Decrease in Profits: " + min_month + " ($" + str(min_value) +")")
f.write("Greatest Increase in Profits: " + max_month + " ($" + str(max_value) +")\n")
f.write("Greatest Decrease in Profits: " + min_month + " ($" + str(min_value) +")\n")