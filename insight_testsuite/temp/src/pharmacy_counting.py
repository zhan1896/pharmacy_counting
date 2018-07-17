#!/usr/bin/env python3
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

fin = open(input_file)

dt_cnt = {}
dt_cost = {}

for num, l in enumerate(fin):
    if num == 0: #ignore the first line
        continue
    l = l.strip().split(',')
    id_, prescriber_last_name, prescriber_first_name, drug_name, drug_cost = l
    prescriber = prescriber_last_name + ',' + prescriber_first_name
    if drug_name not in dt_cnt:
        dt_cnt[drug_name] = set()
        dt_cost[drug_name] = 0
    dt_cnt[drug_name].add(prescriber)
    dt_cost[drug_name] += int(drug_cost)


'''

A B C
6 7 7
A = {6: [A], 7: [B,C]}
'''

fout = open(output_file, 'w')
fout.write('drug_name,num_prescriber,total_cost\n')
levels = {}
for key in dt_cost:
    if dt_cost[key] not in levels:
        levels[dt_cost[key]] = []
    levels[dt_cost[key]].append(key)

for cost in sorted(levels.keys(), reverse=True):
    for key in sorted(levels[cost], reverse=True):
        fout.write("%s,%s,%s\n" % (key, len(dt_cnt[key]), dt_cost[key]))


