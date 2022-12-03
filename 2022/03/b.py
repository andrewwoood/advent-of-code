with open("input.txt") as input_data:
    rucksacks = input_data.readlines()
    
    total = 0
    for idx in range(0, len(rucksacks), 3):
        first, second, third = set(rucksacks[idx]), set(rucksacks[idx+1]), set(rucksacks[idx+2])

        shared_letter = first.intersection(second).intersection(third)

        for letter in shared_letter:
            if letter == "\n": continue # Messy workaround
            if letter.isupper():
                total += ord(letter) - ord("A") + 27
            else:
                total += ord(letter) - ord("a") + 1

    print(f"Total is {total}")