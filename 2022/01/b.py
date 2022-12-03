import heapq

with open("input.txt") as input_data:
    current_calories = 0
    calories_heap = []

    all_calories = input_data.readlines()
    for fruit_calories in all_calories:
        if fruit_calories == "\n":
            calories_heap.append(-1 * current_calories) # Make it a max-heap
            current_calories = 0
            continue
        
        current_calories += int(fruit_calories)

    heapq.heapify(calories_heap)

    top3_sum = 0
    for elf in range(3):
        top3_sum += -1 * heapq.heappop(calories_heap)

    print(f"Top 3 elves have a combined {top3_sum} calories")
