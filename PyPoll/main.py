#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:05:00 2024

@author: karleecrose
"""

#Import dependencies
import csv
import os

#Establish paths
file_to_load = os.path.join('Desktop','python-challenge','PyPoll','Resources','election_data.csv')
file_to_output = os.path.join('Desktop','python-challenge','PyPoll','analysis','election_analysis.txt')

#Define variables
total_votes = 0

#Open and read csv file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data,)
    
    #Skip header and count total number of votes cast
    next(reader)
    data = list(reader)
    row_count = len(data)
    
    #Create list of candidates who received votes
    candidate_list = list()
    tally = list()
    
    for i in range(0, row_count):
        candidate = data[i][2]
        tally.append(candidate)
        
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    candidate_count = len(candidate_list)

#Calculate total number of votes & percentage won
votes = list() 
percentage = list() 
for j in range (0,candidate_count):
    name= candidate_list[j]
    votes.append(tally.count(name))
    vote_percentage = votes[j]/row_count
    percentage.append(vote_percentage)
    
#Winner of the election *Drum Roll please*
winner = votes.index(max(votes))

#Print to terminal
print("Election Results")
print("--------------------")
print(f"Total Votes: {row_count:,}")
print("--------------------")
for k in range (0, candidate_count):
    print(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
print("--------------------") 
print(f"Winner: {candidate_list[winner]}")
print("--------------------")

#Print to output txt file
with open(file_to_output, "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("--------------------")
    file.write("\n")
    file.write(f"Total Votes: {row_count:,}")
    file.write("\n")
    file.write("--------------------")
    file.write("\n")
    for k in range (0, candidate_count):
        file.write(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    file.write("\n")
    file.write("--------------------")
    file.write("\n")
    file.write(f"Winner: {candidate_list[winner]}")
    file.write("\n")
    file.write("--------------------")













   
    