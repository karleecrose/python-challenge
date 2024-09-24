#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:05:22 2024

@author: karleecrose
"""

#Import Dependencies
import csv
import os

#Files to load and output
file_to_load = os.path.join('Desktop','python-challenge','PyBank','Resources','budget_data.csv')
file_to_output = os.path.join('Desktop','python-challenge','PyBank','analysis','budget_analysis.txt')

#Define variables
total_months = []
total_profit = []
profit_change = []

#Open and read csv 
with open(file_to_load) as financial_data:
    data=csv.reader(financial_data,)
   
    #Skip header
    header=next(data)
   
    #Append total months and total profit
    for row in data:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
     
    #Iterate to find monthly change in profits
    for i in range(len(total_profit)-1):
        
        profit_change.append(total_profit[i+1]-total_profit[i])

#Calculate max and min of monthly profit change 
greatest_increase_value = max(profit_change)
greatest_decrease_value = min(profit_change) 

#Correlate to proper month
greatest_increase_month = profit_change.index(max(profit_change))+1
greatest_decrease_month = profit_change.index(min(profit_change))+1

#Print statements
print("Financial Analysis")
print("----------------------")  
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_value))})")

#Output files
with open(file_to_output, "w") as file:

  file.write("Financial Analysis")
  file.write("\n")
  file.write("----------------------------")
  file.write("\n")
  file.write(f"Total Months: {len(total_months)}")
  file.write("\n")
  file.write(f"Total: ${sum(total_profit)}")
  file.write("\n")
  file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
  file.write("\n")
  file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase_value))})")
  file.write("\n")
  file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease_value))})")        
        
    