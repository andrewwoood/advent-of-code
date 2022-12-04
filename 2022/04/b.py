def split_into_range(assignment):
    res = assignment.split("-")
    res = set(range(int(res[0]), int(res[1])+1))
    return res

def is_overlapping(r1, r2):
    both = r1.union(r2)
    return len(r1) + len(r2) > len(both)

with open("input.txt") as input_data:
    count = 0

    pairs = input_data.readlines()
    for pair in pairs:
        first, second = pair.split(",")
        range1, range2 = split_into_range(first), split_into_range(second)
        if is_overlapping(range1, range2): count += 1

    print(f"total is {count}")
