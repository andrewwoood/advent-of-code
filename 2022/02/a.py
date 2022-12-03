with open("input.txt") as input_data:
    score = 0
    shape_value = {"X": 1, "Y": 2, "Z": 3}
    winning_matchup = {"Y": "A", "X": "C", "Z": "B"}
    tying_matchup = {"X": "A", "Y": "B", "Z": "C"}

    matches = input_data.readlines()
    for match in matches:
        opponent, player = match.split()

        if winning_matchup[player] == opponent:
            score += 6

        elif tying_matchup[player] == opponent:
            score += 3

        score += shape_value[player]

    print(f"Total score of player is {score}")
