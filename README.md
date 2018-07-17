# Table of Contents
1. [Description](README.md#description)
2. [Approach](README.md#approach)
3. [Instructions](README.md#instructions)
4. [Repo Directory Structure](README.md#repo-directory-structure)

# Descriptions

This program is written in Python. The input is data is the simplified data set from the Centers for Medicare & Medicaid Services. It provides information on id number, names of prescribers, prescription drug names and drug cost. The program reads the input data sets and generate a list of all drugs, the total number of unique prescribers for each drug and the total drug cost. The output information is listed in descending order based on the total drug cost and if there is a tie, drug name. 

# Approach 

The program read the input data set and seperate the information of each catergories (id number, names of prescribers, prescription drug names and drug cost`). Then it uses a hashtable to store the drug names as the key and corresponding unique prescribers in "set" as the value (in case the same name appeared multiple times), and uses another hashtable to store the drug names as the key and the total drug cost as the value. The total drug cost is accumulated in the iteration.

For output, the unique drug costs and its associated drug names are first saved in a hashtable. The ouput infomation is then sorted in the decending order of the total drug cost first, and if multiple drug names are listed under one drug cost, or in other words, if there is a tie with the total drug cost, then the information are sorted in the decending order of the drug name.  

# Instructions

The main python code is "/src/pharmacy_counting.py". The input data set should be specified as "input/`itcont.txt". The user can execute "run.sh" to run the python program. The generated output will be saved as "/output/top_cost_drug.txt".

# Repo Directory Structure

The directory structure is:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── top_cost_drug.txt


