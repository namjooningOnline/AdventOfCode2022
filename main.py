#day1.py failed question two. this is my second attempt following a Youtube video

with open('day1.in') as file:
    file.seek(0)
    elf_pockets = file.read()

elf_pockets_split = elf_pockets.split("\n\n")

food_calories = []
for elf_pocket in elf_pockets_split: 
    elf_pocket_str = elf_pocket.splitlines()
    food_item_int = []
    for food_item_str in elf_pocket_str:
        food_item_int.append(int(food_item_str))
    food_calories.append(sum(food_item_int))

food_calories.sort(reverse = True)

print('The elf carrying the most Calories is carrying: ' + str(sum(food_calories[:1])) + ' Calories.')
print('The top three elves carrying the most Calories are carrying: ' + str(sum(food_calories[:3])) + ' Calories.')

#The elf carrying the most Calories is carrying: 74711 Calories.
#The top three elves carrying the most Calories are carrying: 209481 Calories.