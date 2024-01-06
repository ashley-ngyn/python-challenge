#PyBank main.py

#create file path
import os

#reading csv file
import csv

#path to find the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

#source 01 to create empty lists
total_months = []
total_amount = []
average_change = []

#source 02 and source 03 to open cvs file
with open(csvpath, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)

    #source 04 used to read headers
    csvheader = next(csvfile)

    #loop through rows in csv file
    for row in csvreader:

        #source 05 add to the empty lists
        #int() converts string to integers
        total_months.append(row[0])
        total_amount.append(int(row[1]))
    
#source 06, len() function returns the number of items in a list
        
    #loop through totals
    #source 07 assumes len(total_amount) is 1 so we add -1 to include the 0 of the index
    for i in range(len(total_amount)-1):
        #calculate differences and add to list of average_change
        average_change.append((total_amount[i+1])-(total_amount[i]))
    
    #find max and min of average change
    greatest_increase_amount = max(average_change)
    greatest_decrease_amount = min(average_change)

    #find month of the max and min of average change
    #vs_code said return index of first value, we have to +1 to get the next month
    greatest_increase_month = average_change.index(max(average_change)) + 1
    greatest_decrease_month = average_change.index(min(average_change)) + 1
    


#print the analysis in terminal
#f-string combines string with functions

print("Financial Analysis")
print("----------------------------")
#len() calculates total amount of items
print(f"Total Months: {len(total_months)}")
#sum() adds up sum of integers
print(f"Total: ${sum(total_amount)}")
#soure 08 for round() function
print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")

#within the total months we are trying to find the months accordingly
#{greatest_increase/decrease_month} would only give us a value, not string
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${greatest_decrease_amount})")


#export a text file with the results

#source 09 used to:
    #write text in file, find path, \n creates a new line, f.write() writes a list of txt strings

filepath = os.path.join("analysis", "PyBank_analysis.txt")
with open(filepath, 'w') as textfile:
    textfile.write("Financial Analysis")
    textfile.write("\n----------------------------")
    textfile.write(f"\nTotal Months: {len(total_months)}")
    textfile.write(f"\nTotal: ${sum(total_amount)}")
    textfile.write(f"\nAverage Change: ${round(sum(average_change)/len(average_change),2)}")
    textfile.write(f"\nGreatest Increase in Profits: {total_months[greatest_increase_month]} (${greatest_increase_amount})")
    textfile.write(f"\nGreatest Decrease in Profits: {total_months[greatest_decrease_month]} (${greatest_decrease_amount})")
