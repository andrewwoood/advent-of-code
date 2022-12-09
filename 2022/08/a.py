def main():
    with open("input.txt") as input_data:
        lines = [x.strip() for x in input_data.readlines()]
        tree_heights = [[int(x) for x in y] for y in lines]
        num_rows, num_cols = len(tree_heights), len(tree_heights[0])

        visible_trees = set()

        # Add all the boundary trees
        for row in range(num_rows):
            visible_trees.add((row, 0))
            visible_trees.add((row, num_cols-1))
        for col in range(num_cols):
            visible_trees.add((0, col))
            visible_trees.add((num_rows-1, col))

        # Check all visible trees from each of the 4 directions

        # From the top
        for col in range(1, num_cols-1):
            tallest_neighbor = -1
            for row in range(1, num_rows-1):
                tallest_neighbor = max(tallest_neighbor, tree_heights[row-1][col])
                is_tall_enough = tree_heights[row][col] > tallest_neighbor

                if is_tall_enough:
                    visible_trees.add((row, col))

        # From the bottom
        for col in range(1, num_cols-1):
            tallest_neighbor = -1
            for row in range(num_rows-2, 0, -1):
                tallest_neighbor = max(tallest_neighbor, tree_heights[row+1][col])
                is_tall_enough = tree_heights[row][col] > tallest_neighbor

                if is_tall_enough:
                    visible_trees.add((row, col))

        # From the left
        for row in range(1, num_rows-1):
            tallest_neighbor = -1
            for col in range(1, num_cols-1):
                tallest_neighbor = max(tallest_neighbor, tree_heights[row][col-1])
                is_tall_enough = tree_heights[row][col] > tallest_neighbor

                if is_tall_enough:
                    visible_trees.add((row, col))
            
        # From the right
        for row in range(1, num_rows-1):
            tallest_neighbor = -1
            for col in range(num_cols-2, 0, -1):
                tallest_neighbor = max(tallest_neighbor, tree_heights[row][col+1])
                is_tall_enough = tree_heights[row][col] > tallest_neighbor

                if is_tall_enough:
                    visible_trees.add((row, col))

        print(f"Total visible trees is {len(visible_trees)}")

main()