def num_increasing(array):
    increasing = 0
    
    for x in range(1, len(array), 1):
        if array[x] > array[x - 1]:
            increasing += 1

    return increasing

f = open("input.txt")
depths = [int(x.strip("\n")) for x in f.readlines()]
f.close()

num_increased = num_increasing(depths)

print("Part 1:", num_increased)

triplets = []

for x in range(1, len(depths) - 1, 1):
    sum = depths[x - 1] + depths[x] + depths[x + 1]
    triplets.append(sum)

num_increased = num_increasing(triplets)

print("Part 2:", num_increased)