def evolve(raw_fish, days):
    fish = dict()

    for x in range(9):
        fish[x] = 0

    for f in raw_fish:
        fish[f] += 1

    new_fish = 0

    for _ in range(days):
        new_fish = fish[0]
        for x in range(8):
            fish[x] = fish[x + 1]
        fish[6] += new_fish
        fish[8] = new_fish

    total = 0

    for num in fish.values():
        total += num

    return total

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

answer = evolve([int(x) for x in lines[0].split(",")], 80)
p1(answer)

answer = evolve([int(x) for x in lines[0].split(",")], 256)
p2(answer)