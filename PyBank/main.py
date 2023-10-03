import os
import csv

#The total number of months included in the dataset
#not a len function, but a comparison If month of date is not in dictionary, add to dictionary

    # resulting MonthlyProfit = {1 MonthlyTotalProfitLosses,2,3,4,5,6,7,8,9,10,11,12}

#The net total amount of ProfitLosses over the entire period
#sum of profitlosses column

#The changes in ProfitLosses over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period
#maximum of profitlosses, and return date

#The greatest decrease in profits (date and amount) over the entire period
#minimum of profitlosses, and return date


#Declare variable values
months = []
ChangeInProfit = []

#Import csv file
BudgetData_csv = os.path.join('Resources','budget_data.csv')

# Open and read csv
with open(BudgetData_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header {csv_header}")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csv_reader:
        #Increase MounthCount
        MonthCount += 1

        #TotalProfit calculations
        CurrentProfit = int(row[1])
        TotalProfit += CurrentProfit

        if (MonthCount == 1):
            #Make the value of previous month to be equal to current month
            PriorProfit = CurrentProfit
            continue
        else:
            #Calculate ChangeInProfit
            ChangeInProfit = CurrentProfit - PriorProfit

            #Add month to months list
            months.append(row[0])

            #Add ChangeInProfit to the ChangeInProfit list
            ChangeInProfit.append(ChangeInProfit)

            #Set CurrentProfit to be PriorProfit for the next loop
            PriorProfit = CurrentProfit

    #Total and Average profit for the whole .csv file
    SumProfit = sum(ChangeInProfit)
    AvgProfit = round(SumProfit/(MonthCount - 1), 2)

    #Minimum and Maximum profit for the whole .csv file
    MaxChange = max(ChangeInProfit)
    MinChange = min(ChangeInProfit)

    #What's the index number for the Miniumum and Maximum profits
    BestMonthIndex = ChangeInProfit.index(MaxChange)
    WorstMonthIndex = ChangeInProfit.index(MinChange)

    # Assign best and worst month
    BestMonth = months[BestMonthIndex]
    WorstMonth = months[WorstMonthIndex]

#Print analysis
print("Financial Analysis:")
print(" ")
print(f"Total Months:  {MonthCount}")
print(f"Total:  ${TotalProfit}")
print(f"Average Change:  ${AvgProfit}")
print(f"Greatest Increase in Profits:  {BestMonth} (${MaxChange})")
print(f"Greatest Decrease in Losses:  {WorstMonth} (${MinChange})")


#Export results to .txt file in output folder
budget_file = os.path.join("Output", "Budget_Data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {MonthCount}\n")
    outfile.write(f"Total:  ${TotalProfit}\n")
    outfile.write(f"Average Change:  ${AvgProfit}\n")
    outfile.write(f"Greatest Increase in Profits:  {BestMonth} (${MaxChange})\n")
    outfile.write(f"Greatest Decrease in Losses:  {WorstMonth} (${MinChange})\n")
