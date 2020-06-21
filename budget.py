import csv 
import os

outputfile = os.path.join("Analysis", "budget.txt")

inputfile = os.path.join("Resources", "budget_data.csv")
#print(" ".join(row)) # printed each row as a string
#print (type(row[1])) # print each row as a list
#establish your variables
count = 0
output = ""
#setting profits
profit_and_losses = []
curent_total = 0
#Setting Date
#date = row[0]
previous_profit = 0
average_change = 0
curent_difference = 0
profit_differences = []
greatest_increase = 0
greatest_increase_month = " "
greatest_decrease = 0
greatest_decrease_month = " "


with open(inputfile) as budget_data: #telling where to look and how to read the file
    csvreader =csv.reader(budget_data, delimiter=',')

    print(csvreader)

    header = next(csvreader) #we are telling what the header is
   
    for row in csvreader: #establishing the loop to count the amount of rows in the file to start with 1. If only we used R for this! hahahahaha
     count =  count + 1 # the +1 is because python is not like R. It starts at 0. This counts the number of rows. This will also give us the amount of total months. Bwa ha ha ha 
     
     curent_total = curent_total + int(row[1]) # row 1 is the profit for the current month
     curent_difference = int(row[1]) - previous_profit
     if count > 1: # cancels out the first value
       if curent_difference > greatest_increase:
         greatest_increase = curent_difference #these two if conditions will find the greatest increase/decrease then it will publish the month/year when.
         greatest_increase_month = row [0]
       if curent_difference < greatest_decrease:
         greatest_decrease = curent_difference
         greatest_decrease_month = row [0]
     previous_profit = int(row[1])  #save the profit for the month we just looked at
     profit_differences.append(curent_difference)
profit_differences = profit_differences[1:len(profit_differences)]

#print (profit_differences)

average_change = (sum(profit_differences)/len(profit_differences))
#print(profit_differences[1:]) # this will start with index 1 and not 0

countstr = "analysis\n{str(count)}" 
with open(outputfile, "w") as outbudget:
  outbudget.write(countstr)  

print("Financial Analysis")
print("---------------------------------------------------------------------------------")
print("Total Months: " + str(count))
print("Total: " + "$" + str(curent_total)) 
print("Average Change: " + "$" + str(average_change))
print("Greatest Increase in Profits: " + str(greatest_increase_month) +" "+ "$" + "(" + str(greatest_increase)+")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_month) +" "+ "$" + "(" + str(greatest_decrease)+")")

#this is to write to another file
with open(outputfile, 'w') as budget:
    budget.write("Financial Analysis")
    budget.write("\n")
    budget.write("-------------------\n")
    budget.write("Total Months: " + str(count))
    budget.write("\n")
    budget.write("Total: " + "$" + str(curent_total))
    budget.write("\n")
    budget.write("Average Change: " + "$" + str(average_change))
    budget.write("\n")
    budget.write("Greatest Increase in Profits: " + str(greatest_increase_month) +" "+ "$" + "(" + str(greatest_increase)+")")
    budget.write("\n")
    budget.write("Greatest Decrease in Profits: " + str(greatest_decrease_month) +" "+ "$" + "(" + str(greatest_decrease)+")")
    