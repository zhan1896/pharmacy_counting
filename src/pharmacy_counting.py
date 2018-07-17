#!/usr/bin/env python3
import sys

# input and output file names obtained from command line
input_file = sys.argv[1]
output_file = sys.argv[2]

fin = open(input_file)

dt_cnt = {} # number of unique prescribers
dt_cost = {} # total cost

for num, l in enumerate(fin):
    if num == 0: # ignore the first line
        continue
    l = l.strip().split(',') # split a line of texts 
    id_, prescriber_last_name, prescriber_first_name, drug_name, drug_cost = l # evaluate each parameters
    prescriber = prescriber_last_name + ',' + prescriber_first_name 
    if drug_name not in dt_cnt:
        dt_cnt[drug_name] = set() # add drug name into the dictionaries
        dt_cost[drug_name] = 0
    dt_cnt[drug_name].add(prescriber) # store unique prescriber names; use "set" in case the same name appeared multiple times 
    dt_cost[drug_name] += int(drug_cost) # accumulate drug cost


'''

A B C
6 7 7
A = {6: [A], 7: [B,C]}
'''

fout = open(output_file, 'w')
fout.write('drug_name,num_prescriber,total_cost\n')
levels = {}
# save unique drug costs and its associated drug names in the dictionary 
for key in dt_cost: 
    if dt_cost[key] not in levels:
        levels[dt_cost[key]] = []
    levels[dt_cost[key]].append(key)
# list the information in descending order based on the total drug cost and if there is a tie, drug name
for cost in sorted(levels.keys(), reverse=True):
    for key in sorted(levels[cost], reverse=True):
        fout.write("%s,%s,%s\n" % (key, len(dt_cnt[key]), dt_cost[key]))


