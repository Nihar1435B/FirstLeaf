# Filename: bogo_sort.py
import random

def is_sorted(arr: list[int]) -> bool:
    """Checks if the list is sorted in ascending order."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def bogo_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list by repeatedly shuffling it until it's sorted.
    WARNING: Do NOT use this on lists with more than ~10 elements.
    """
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
        # It's fun to see how many tries it takes!
        print(f"Attempt {attempts}: {arr}")

    print(f"\nSorted successfully after {attempts} attempts!")
    return arr

# --- Example Usage ---
# Use a very small list for demonstration
my_list = [4, 1, 5, 2]
print(f"Original: {my_list}\n")

sorted_list = bogo_sort(my_list)
print(f"\nSorted:   {sorted_list}")
