def calculate_score(row, col, tree_heights):
    candidate_height = tree_heights[row][col]

    up_score = 0
    curr_row, curr_col = row, col
    while curr_row > 0:
        up_score += 1
        neighbor_height = tree_heights[curr_row-1][curr_col]
        if neighbor_height >= candidate_height:
            break
        curr_row -= 1

    down_score = 0
    curr_row, curr_col = row, col
    while curr_row < len(tree_heights) - 1:
        down_score += 1
        neighbor_height = tree_heights[curr_row+1][curr_col]
        if neighbor_height >= candidate_height:
            break
        curr_row += 1

    left_score = 0
    curr_row, curr_col = row, col
    while curr_col > 0:
        left_score += 1
        neighbor_height = tree_heights[curr_row][curr_col-1]
        if neighbor_height >= candidate_height:
            break
        curr_col -= 1

    right_score = 0
    curr_row, curr_col = row, col
    while curr_col < len(tree_heights[0])-1:
        right_score += 1
        neighbor_height = tree_heights[curr_row][curr_col+1]
        if neighbor_height >= candidate_height:
            break
        curr_col += 1

    final_score = up_score * down_score * left_score * right_score
    return final_score
    


def main():
    with open("input.txt") as input_data:
        lines = [x.strip() for x in input_data.readlines()]
        tree_heights = [[int(x) for x in y] for y in lines]
        num_rows, num_cols = len(tree_heights), len(tree_heights[0])

        highest_score = 1
        for row in range(num_rows):
            for col in range(num_cols):
                current_score = calculate_score(row, col, tree_heights)
                highest_score = max(highest_score, current_score)

        print(f"Highest scenic score is {highest_score}")

main()