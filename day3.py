# Day 3: Rucksack Reorganization 

#Getting the data 
with open("day3.in") as file:
    data = [i for i in file.read().strip().split("\n")]

# iterate through the data
for rucksack in data: 
    # find half
    half = len(rucksack)//2 #// returns an integer

    left = rucksack[:half]
    right = rucksack[half:]

    print(rucksack, left, right)
