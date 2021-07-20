#Import Modules 
import csv
import os

#Path to CSV File Budget_Data 
budget_csv_path = os.path.join('./PyBank/Resources/budget_data.csv')

# Set Variables 
total_months = 0 
total_amount = 0 
greatest_increase = 0 
greatest_increase_month = 0 
greatest_decrease = 0 
greatest_decrease_month = 0 
monthly_change = []
month_count = []


#Open CSV and Set Variable
with open(budget_csv_path) as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Read Header 
    header = next(csv_reader)
    row = next(csv_reader)



    #Calculate total Number of Months, Net Amount of "Profit/Losses" & Set Variables for Rows 
    total_months += 1 
    prior_amount_row = int(row[1])
    total_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    #Read Each Row 
    for row in csv_reader: 
        total_months += 1 
        total_amount += int(row[1])

        #calculate monthly change
        amount_change = int(row[1]) -  prior_amount_row
        monthly_change.append(amount_change)
        prior_amount_row = int(row[1])
        month_count.append(row[0])

        #Calculate the greatest increase 
       if int(row[1]) > greatest_increase: 
        greatest_increase = int(row[1])
        greatest_increase_month = row[0]

       if int(row[1]) < greatest_decrease: 
        greatest_decrease = int(row[1])
        greatest_decrease_month = row[0]

    #Calculate the average 
    average = sum(monthly_change)/len(monthly_change)
    greatest = max(monthly_change)
    weakest = min(monthly_change)

    #Print Values 
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_amount))
    print("Average Change: " + "$" + str(int(average)))
    print("Greatest Increase in Profits: " + str(greatest_increase_month), greatest)
    print("Greatest Decrease in Profits: " + str(greatest_decrease_month), weakest)

    #Specify where to write file to 
   

with open('Financialanalysis.txt', 'w') as writer:

  writer.write('Financial Analysis')
  writer.write('\n---------------------------------------')
  writer.write('\n' + "Total Months: " + str(total_months))
  writer.write('\n' + "Total Amount: " + "$" + str(total_amount))
  writer.write('\n' + "Average Change: " + "$" + str(int(average)))
  writer.write('\n' + "Greatest Increase in Profits: " + str(greatest_increase_month) + " $" + str(greatest))
  writer.write('\n' + "Greatest Decrease in Profits: " + str(greatest_decrease_month) + " $" + str(weakest))














