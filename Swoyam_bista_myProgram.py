# Importing the data from previous stats
from Swoyam_bista_Stats import Mean, Median, Mode

# Introducing the empty lists of apples, bananas and strawberries
apples = []
bananas = []
strawberries = []

# Reading the data from the file and parsing the data
with open("50DayFruitData.txt") as file:
    for line in file:
        data = line.split()
        if data[1] == "apple":
            apples.append(int(data[2]))
        elif data[1] == "banana":
            bananas.append(int(data[2]))
        elif data[1] == "strawberry":
            strawberries.append(int(data[2]))

# Calculating Mean, Median and Mode of all apples, bananas and strawberries
mean_apples = Mean([a for a in apples if a != 0])
median_apples = Median([a for a in apples if a != 0])
mode_apples = Mode([a for a in apples if a != 0])

mean_bananas = Mean([b for b in bananas if b != 0])
median_bananas = Median([b for b in bananas if b != 0])
mode_bananas = Mode([b for b in bananas if b != 0])

mean_strawberries = Mean([s for s in strawberries if s != 0])
median_strawberries = Median([s for s in strawberries if s != 0])
mode_strawberries = Mode([s for s in strawberries if s != 0])

# Output of the results in a new file
with open("Swoyam Bista Output.txt", "w") as file:
    file.write(f"Mean Apples: {mean_apples}\n")
    file.write(f"Median Apples: {median_apples}\n")
    file.write(f"Mode Apples: {mode_apples}\n")
    
    file.write(f"Mean Bananas: {mean_bananas}\n")
    file.write(f"Median Bananas: {median_bananas}\n")
    file.write(f"Mode Bananas: {mode_bananas}\n")
    
    file.write(f"Mean Strawberries: {mean_strawberries}\n")
    file.write(f"Median Strawberries: {median_strawberries}\n")
    file.write(f"Mode Strawberries: {mode_strawberries}\n")
    
# Printing the results to console

print(f"The mean number of apples eaten is {mean_apples}\nThe median number of apples eaten is {median_apples}\nThe mode number of apples are {mode_apples}\n\n")
print(f"The mean number of bananas eaten is {mean_bananas}\nThe median number of bananas eaten is {median_bananas}\nThe mode number of bananas are {mode_bananas}\n\n")
print(f"The mean number of strawberries eaten is {mean_strawberries}\nThe median number of strawberries eaten is {median_strawberries}\nThe mode number of strawberries are {mode_strawberries}")


