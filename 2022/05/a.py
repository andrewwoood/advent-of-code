from collections import deque

def split_instruction(line):
    line = line.split(" ")
    crate, start, end = int(line[1]), int(line[3]) - 1, int(line[5].strip()) - 1
    return [crate, start, end]

with open("input.txt") as input_data:

    lines = input_data.readlines()
    num_stacks = len(lines[0]) // 4

    crate_stacks = [deque([]) for _ in range(num_stacks)]
    move_instructions = []

    # Find when instructions start
    start_instructions_line = 0
    for idx, line in enumerate(lines):
        if line[0] == "m":
            start_instructions_line = idx
            break

    # Get stacks
    stacks_end = start_instructions_line-3
    for line in lines[:stacks_end+1]:
        char_idx = 0
        while char_idx < len(line):
            char = line[char_idx]
            stack_idx = char_idx // 4

            
            if char == " ": # Empty spot or indices
                char_idx += 4
            elif char == "[": # Append crate
                crate_symbol = line[char_idx+1]
                crate_stacks[stack_idx].appendleft(crate_symbol)
                char_idx += 4


    for line in lines[start_instructions_line:]:
        instruction = split_instruction(line)
        move_instructions.append(instruction)


    # Rearrange
    for instruction in move_instructions:
        num_crates, start_stack_idx, end_stack_idx = instruction

        for crate in range(num_crates):
            start_stack = crate_stacks[start_stack_idx]
            end_stack = crate_stacks[end_stack_idx]

            end_stack.append(start_stack.pop())



    # print(crate_stacks)
    output = []
    for stack in crate_stacks:
        output.append(stack[-1])

    print("".join(output))
