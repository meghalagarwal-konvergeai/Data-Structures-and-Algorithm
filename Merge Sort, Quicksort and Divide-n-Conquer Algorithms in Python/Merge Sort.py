'''
Merge Sort divides the list into 2.
Then compare 2 divided list on each iteration with each other and store it in sorted list.
This continues till all the elements of both the list are exusted.
If any one list is exusted early then the remaining list is add at the last.
'''

def merge(nums1, nums2):
    # Defining a List to store the results 
    merged = []
    # Indices for points and their iterations
    i, j = 0, 0

    # Loop over the two lists
    while i < len(nums1) and j <len(nums2):
        # Include the smaller element in the result and move to next element
        if(nums1[i]<=nums2[j]):
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    # Get the remaining parts by simply adding them to the list.
    return merged + nums1[i:] + nums2[j:]

def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if(len(nums) <= 1):
        return nums

    # Get the midpoint
    mid = len(nums)//2
    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    # Solve the problem for each half recursively
    left_sort, right_sort = merge_sort(left), merge_sort(right)
    # Combine the results of the two halves
    sorted_num = merge(left_sort, right_sort)

    return sorted_num

if __name__ == "__main__":
    nums = [1,5,4,2,12,35,78,65,0,4,3]
    l = merge_sort(nums)
    print(l)