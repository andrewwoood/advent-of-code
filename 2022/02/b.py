with open("input.txt") as input_data:
    shape_value = {"X": 1, "Y": 2, "Z": 3}
    shape_mapping = {"A": "X", "B": "Y", "C": "Z"}
    result_bonus = {"Z": 6, "Y": 3, "X": 0}

    winning_matchup = {"Y": "A", "X": "C", "Z": "B"}
    tying_matchup = {"X": "A", "Y": "B", "Z": "C"}
    losing_matchup = {"X": "B", "Y": "C", "Z": "A"}

    score = 0
    matches = input_data.readlines()
    for match in matches:
        opponent, result = match.split()

        if result == "X": # Loss
            our_shape = shape_mapping[winning_matchup[shape_mapping[opponent]]]

        elif result == "Y": # Draw
            our_shape = shape_mapping[tying_matchup[shape_mapping[opponent]]]
        
        else: # Win
            our_shape = shape_mapping[losing_matchup[shape_mapping[opponent]]]

        score += result_bonus[result] + shape_value[our_shape]

    print(f"Total score of player is {score}")