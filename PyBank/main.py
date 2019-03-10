import os
import csv

#PATHFILE
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
#cvspath = os.path.join ('Resources', 'budget_data.csv')
#/Users/miroslavavillalobos/Downloads/RepositorioGitLab/TECMC201902DATA2/02-Homework/03-Python/Instructions/
#set the output of the text file
text_path = "output.txt"
totalMonths = 0
totalRevenue = 0
revenue = []
previousRevenue = 0
monthChange = []
revenueChange = 0
greatestDecrease = ["", 9999999]
greatestIncrease = ["", 0]
revenueChangeList = []
revenueAverage = 0


#OPEN CVS FILE
with open('budget_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #FOR IN TO THE MONTHS
    for row in csvreader:

        #TOTAL MONTHS
        totalMonths += 1

        #TOTAL AVERAGE REVENUE
        totalRevenue = totalRevenue + int(row["Profit/Losses"])

        #AVERAGE
        revenueChange = float(row["Profit/Losses"])- previousRevenue
        previousRevenue = float(row["Profit/Losses"])
        revenueChangeList = revenueChangeList + [revenueChange]
        monthChange = [monthChange] + [row["Date"]]
       

        #GREATEST INCREASE
        if revenueChange>greatestIncrease[1]:
            greatestIncrease[1]= revenueChange
            greatestIncrease[0] = row['Date']

        #GREATES DECREASE
        if revenueChange<greatestDecrease[1]:
            greatestDecrease[1]= revenueChange
            greatestDecrease[0] = row['Date']
    revenueAverage = sum(revenueChangeList)/len(revenueChangeList)

#CVS OUTPATH
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % totalMonths)
    file.write("Total : $%d\n" % totalRevenue)
    #file.write("Average Change $%d\n" % revenueAverage)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatestIncrease[0], greatestIncrease[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatestDecrease[0], greatestDecrease[1]))