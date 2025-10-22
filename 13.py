def linear_search(roll_numbers, target):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] == target:
            return True
    return False

def binary_search(roll_numbers, target):
    low = 0
    high = len(roll_numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if roll_numbers[mid] == target:
            return True
        elif roll_numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def main():
    roll_numbers = [104, 102, 120, 110, 130, 101, 115]

    print("Registered Roll Numbers (unsorted):", roll_numbers)

    try:
        target = int(input("Enter roll number to check registration: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Linear Search
    found_linear = linear_search(roll_numbers, target)
    print("\nLinear Search Result:")
    if found_linear:
        print(f"Roll number {target} is registered.")
    else:
        print(f"Roll number {target} is NOT registered.")

    # Binary Search (requires sorted list)
    sorted_roll_numbers = sorted(roll_numbers)
    found_binary = binary_search(sorted_roll_numbers, target)
    print("\nBinary Search Result (on sorted list):")
    if found_binary:
        print(f"Roll number {target} is registered.")
    else:
        print(f"Roll number {target} is NOT registered.")

if __name__ == "__main__":
    main()
