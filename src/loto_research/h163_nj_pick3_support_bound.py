from math import ceil

TOTAL_OUTCOMES = 1000
MAX_PLAYS_PER_TICKET = 10

BET_SUPPORT = {
    "Straight": 1,
    "Box/Wheel 3-way": 3,
    "Box/Wheel 6-way": 6,
    "Pair": 10,
}

max_support = max(BET_SUPPORT.values())
min_plays = ceil(TOTAL_OUTCOMES / max_support)
min_tickets = ceil(min_plays / MAX_PLAYS_PER_TICKET)

assert max_support == 10
assert min_plays == 100
assert min_tickets == 10

if __name__ == "__main__":
    print(f"max support per play: {max_support}")
    print(f"minimum plays for all 1000 outcomes: {min_plays}")
    print(f"minimum tickets at 10 plays/ticket: {min_tickets}")
