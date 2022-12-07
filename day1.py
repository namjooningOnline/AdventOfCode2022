#this fails part two. values for max2 and max3 are wrong

# Getting data
with open('day1.in') as file:
    data = [i for i in file.read().strip().split("\n")]


    print(data)


# Traversing every STRING in our DATA
max = 0
max2 = 0 # second place ELF
max3 = 0 # third place ELF
count = 0
for item in data: 
    if item == '':
        count = 0 #restarts the count
    else: 
        num = int(item) # makes the string an integer 
        count += num

    if count > max: 
        max = count
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count


print("Answer to part 1:", max)
print("Answer to part 2:", max+max2+max3)

#Answer to part 1: 74711
#Answer to part 2: 206955 WRONG