with open("input.txt") as input_data:
    rucksacks = input_data.readlines()
    
    total = 0
    for rucksack in rucksacks:
        half = len(rucksack)//2
        first, second = set(rucksack[:half]), set(rucksack[half:])

        shared_letter = first.intersection(second)

        for letter in shared_letter:
            if letter.isupper():
                total += ord(letter) - ord("A") + 27
            else:
                total += ord(letter) - ord("a") + 1
        
        print(f"Total for {shared_letter} is {total}")

    print(f"Total is {total}")