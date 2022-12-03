with open("input.txt") as input_data:
    current_calories = 0
    max_calories = -1
    
    all_calories = input_data.readlines()
    for fruit_calories in all_calories:
        if fruit_calories == "\n":
            max_calories = max(max_calories, current_calories)
            current_calories = 0
            continue
        
        current_calories += int(fruit_calories)

    print(f"Elf with max calories has {max_calories} calories")
