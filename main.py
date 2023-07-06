import os
import csv

budget_data_csv = os.path.join ("Resources", "budget_data.csv")

file_to_save = "file_to_save/analysis"

#initalizing list
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
# Read the csv and convert it into a list of dictionaries
with open(budget_data_csv) as budget_data:
    reader = csv.reader(budget_data)
    # Read the header row
    header = next(reader)
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])
    for row in reader:
        # Track the total
        total_months += 1
        total_net += int(row[1])
        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)
#Output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
# Print output to terminal
print(output)

#adding results to text file
with open(file_to_save, 'w') as txt_file:
    txt_file.write(output)



        

