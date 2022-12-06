from collections import defaultdict

def main():
    with open("input.txt") as input_data:
        seen = defaultdict(int)
        window_length = 4
        signal = input_data.readlines()[0]

        left = 0
        for right, char in enumerate(signal):
            if len(seen) == window_length:
                print(f"Starting char is {right}")
                return

            if right - left >= window_length:
                leftmost_char = signal[left]
                seen[leftmost_char] -= 1
                if seen[leftmost_char] <= 0:
                    seen.pop(leftmost_char)

                left += 1
    
            seen[char] += 1

main()