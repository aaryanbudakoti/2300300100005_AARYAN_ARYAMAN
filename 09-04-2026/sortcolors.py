# Code to sort colors in place - dutch national flag problem
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    def swap(i,j):
        nums[i], nums[j] = nums[j], nums[i]
    while mid <= high:
        if nums[mid] == 0:
            swap(low, mid)
            low += 1
            mid += 1
            
        elif nums[mid] == 2:
            swap(mid, high)
            high -= 1
            mid -=1
        mid += 1

# Example usage
if __name__ == "__main__":
    colors = [2, 0, 2, 1, 1, 0]
    sort_colors(colors)
    print(colors)  # Output: [0, 0, 1, 1, 2, 2]
    