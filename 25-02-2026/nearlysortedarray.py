# Searching in nearly sorted array using binary search

from typing import List

def search_nearly_sorted(arr: List[int], target: int) -> int:
    """
    Search for target in a nearly sorted array.
    In a nearly sorted array, each element is at most k positions away from its sorted position.
    
    Args:
        arr: A nearly sorted list of integers
        target: The value to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if mid is the target
        if arr[mid] == target:
            return mid
        
        # Check left neighbor
        if mid - 1 >= left and arr[mid - 1] == target:
            return mid - 1
        
        # Check right neighbor
        if mid + 1 <= right and arr[mid + 1] == target:
            return mid + 1
        
        # Decide which half to search
        if arr[mid] < target:
            left = mid + 2  # Skip mid+1 as we already checked
        else:
            right = mid - 2  # Skip mid-1 as we already checked
    
    return -1


# Example usage:
if __name__ == "__main__":
    arr = [10,3,40,20,50,80,70]  
    target = 3

    result = search_nearly_sorted(arr, target)
    if result == -1 :
        print("Element not found in the nearly sorted array")
    else:
        print(f"Element {target} found at index: {result}")
