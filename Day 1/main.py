

f = open("input.txt")
depths = [int(x.strip("\n")) for x in f.readlines()]
f.close()

num_increased = 0

for x in range(1, len(depths), 1):
    if depths[x] > depths[x - 1]:
        num_increased += 1

print("Part 1:", num_increased)

num_increased = 0
triplets = []

for x in range(1, len(depths) - 1, 1):
    sum = depths[x - 1] + depths[x] + depths[x + 1]
    triplets.append(sum)

for x in range(1, len(triplets), 1):
    if triplets[x] > triplets[x - 1]:
        num_increased += 1

print("Part 2:", num_increased)