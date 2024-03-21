# Allows us to use functions in operating systems
import os 

# Brings in functions for CSV files
import csv

csvpath = os.path.join('.', 'Resources','budget_data.csv')



#open the CSV file
with open(csvpath) as csvfile:

    #creates a reader object
    csvreader = csv.reader(csvfile)

    profit_loss = []    # creates a separates list for Profit/Loss 
    date_list = []      # creates a separates list for dates 
    profit_change = []  # creates a list for the calculated change in profit 

    
      
    csv_header = next(csvreader) #grabs the headers
    print(f"CSV Header: {csv_header}")
    
    total_months = 0    # initializes counter for the months
    net_total = 0       # initializes variable that accumulates the net total "Profit/Loss"

    for row in csvreader:
        total_months += 1           # counts number of months being analyzed
        net_total += int(row[1])    # totals the net profit over period of time

        profit_loss.append(float(row[1]))   # creates a list of profit/loss
        date_list.append(row[0])            # creates a list of months being analyzed
        
 
      
    change=0              
    change_sum = 0  
    min_change = 0  
    max_change = 0  

    # cycles through the profit_loss list to run calcuations
    for i in range(1, total_months):
        #total_amt += profit_loss[i]
        change=int(profit_loss[i]-profit_loss[i-1])     # calculates the change in "Profit/Loss"
        change_sum += change                            # accumulates the change in "Profit/Loss"

        if i < total_months:
            if change >= max_change:            # when change is >= the maximum increase in "Profit/Loss"
                max_change = change             # stores the greatest increase of change
                max_change_date = date_list[i]  # stores date associated with the the greatest increase
            if change <= min_change:            # when change is <= the maximum decrease in "Profit/Loss"
                min_change = change             # stores the greatest decrease of change
                min_change_date = date_list[i]  # stores date associated with the the greatest decrease

     

    # Open a text file in analysis folder with write mode
    with open("analysis/bank_analysis.txt", "w") as file:
        
        # write headers to text file 'bank_analysis.txt'
        file.write("Financial Analysis:\n")    
        file.write("-----------------------\n")

        # writes calculations to text file 'bank_analysis.txt'
        file.write(f'Total Months: {total_months}\n')
        file.write(f'Total: ${net_total}\n')
        formatted_ave = "{: .2f}".format(change_sum/(total_months-1))
        file.write(f'Average Change: ${formatted_ave}\n')
        file.write(f'Greatest Increase in Profit: {max_change_date} (${max_change})\n')
        file.write(f'Greatest Decrease in Profit: {min_change_date} (${min_change})\n')
        #print(int(change_sum))

        # write headers to terminal
        print("\nFinancial Analysis:")    
        print("-----------------------")

        # writes calculations to terminal
        print(f'Total Months: {total_months}')
        print(f'Total: ${net_total}')
        formatted_ave = "{: .2f}".format(change_sum/(total_months-1))
        print(f'Average Change: ${formatted_ave}')
        print(f'Greatest Increase in Profit: {max_change_date} (${max_change})')
        print(f'Greatest Decrease in Profit: {min_change_date} (${min_change})')
    
    