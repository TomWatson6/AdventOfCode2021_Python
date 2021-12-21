
def advance(player, move):
    player += move
    while player > 10:
        player -= 10
    return player

def play_game(player1, player2):
    p1_score = 0
    p2_score = 0
    end_state = lambda p1, p2: p1 >= 1000 or p2 >= 1000

    rolls = 0
    die_roll = 1
    player1_move = True

    while not end_state(p1_score, p2_score):
        move = 0
        for _ in range(3):
            move += die_roll
            die_roll += 1
            rolls += 1
            if die_roll > 100:
                die_roll = 1
        if player1_move:
            player1 = advance(player1, move)
            p1_score += player1
        else:
            player2 = advance(player2, move)
            p2_score += player2
        player1_move = not player1_move
    return (p1_score, p2_score, rolls)

def play_game2(player1, player2, p1_score, p2_score, p1_turn, memo):
    end_state = lambda p1, p2: p1 >= 21 or p2 >= 21
    total = (0, 0)

    if end_state(p1_score, p2_score):
        return (1, 0) if p1_score > p2_score else (0, 1)
    elif memo.get((player1, player2, p1_score, p2_score, p1_turn)) is not None:
        return memo[(player1, player2, p1_score, p2_score, p1_turn)]
    else:
        for m1 in range(1, 4):
            for m2 in range(1, 4):
                for m3 in range(1, 4):
                    wins = (0, 0)

                    if p1_turn:
                        p1_copy = int(player1)
                        p1_score_copy = int(p1_score)
                        p1_copy = advance(p1_copy, m1)
                        p1_copy = advance(p1_copy, m2)
                        p1_copy = advance(p1_copy, m3)
                        p1_score_copy += p1_copy
                        wins = play_game2(p1_copy, player2, p1_score_copy, p2_score, not p1_turn, memo)
                        memo[(p1_copy, player2, p1_score_copy, p2_score, not p1_turn)] = wins
                    else:
                        p2_copy = int(player2)
                        p2_score_copy = int(p2_score)
                        p2_copy = advance(p2_copy, m1)
                        p2_copy = advance(p2_copy, m2)
                        p2_copy = advance(p2_copy, m3)
                        p2_score_copy += p2_copy
                        wins = play_game2(player1, p2_copy, p1_score, p2_score_copy, not p1_turn, memo)
                        memo[(player1, p2_copy, p1_score, p2_score_copy, not p1_turn)] = wins

                    total = (total[0] + wins[0], total[1] + wins[1])
    return total

def p1(output):
    print("Part 1:", output)

def p2(output):
    print("Part 2:", output)

with open("input.txt") as f:
    lines = [x.strip() for x in f.readlines()]

player1 = int(lines[0][-1])
player2 = int(lines[1][-1])

p1_score, p2_score, rolls = play_game(player1, player2)

loser = min(p1_score, p2_score)

p1(loser * rolls)

memo = dict()

player1 = int(lines[0][-1])
player2 = int(lines[1][-1])

u1, u2 = play_game2(player1, player2, 0, 0, True, memo)

p2(max(u1, u2))
