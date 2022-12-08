from collections import defaultdict

def sum_directory(output, line_idx):
    dir_size = 0

    while line_idx < len(output): 
        line = output[line_idx].split(" ")
        if line[0] == "$": break
        elif line[0] != "dir":
            dir_size += int(line[0])
        line_idx += 1
    return dir_size

def main():
    with open("input.txt") as input_data:
        dir_sizes = defaultdict(int)
        dir_stack = [""]

        output = input_data.readlines()
        for idx, line in enumerate(output):
            line = line.strip().split(" ")
            if line[0] == "$": # Command
                command = line[1]
                if command == "ls":
                    dir_size = sum_directory(output, idx+1)
                    for direc in dir_stack:
                        dir_sizes[direc] += dir_size
                else: # command == "cd"
                    dir_name = line[2]
                    if dir_name == "..":
                        dir_stack.pop()
                    else:
                        dir_stack.append(tuple((dir_stack[-1], dir_name)))
        
        max_size = 100000
        result = sum([val for val in dir_sizes.values() if val <= max_size])

        print(f"Can remove {result} much file size")

main()