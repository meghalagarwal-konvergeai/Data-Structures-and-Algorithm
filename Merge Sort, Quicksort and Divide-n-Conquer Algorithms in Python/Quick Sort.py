'''
Quick Sort is better than Merge Sort in terms of Time Complexity and Space Complexity
Quick Sort considers Pivot point in the list which is the last element of the list
and then considers 2 points at the start of the list and at the end-1 of the list.
These 2 pointers are then compared with the pivot value and swap the element left side or right side of the list based on the smaller or greater element.
This process is then recursive till the entire list is sorted.
Time Complexity of Quick Sort is O(n^2)
Space Complexity of Quick Sort is O(1)
'''

def partition(nums, start, end):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums)-1
    
    # Initialize right and left pointers
    l, r = start, end-1
    # Iterate while they're apart
    while r > l:
        # Decrement right pointer if number is greater than pivot
        if(nums[r] > nums[end]):
            r -= 1
        # Increment left pointer if number is less or equal to pivot
        elif(nums[l] <= nums[end]):
            l += 1
        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    
    # Place the pivot between the two parts
    if(nums[l] > nums[end]):
        nums[l], nums[end] = nums[end], nums[l]
    else:
        return end

def quick_sort(nums, start=0, end=None):
    if(end is None):
        nums = list(nums)
        end = len(nums)-1

    if(start < end):
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot-1)
        quick_sort(nums, pivot+1, end)
    return nums

if __name__ == "__main__":
    nums = [2,4,3,25,1,78,6,45,20,9,90,102]
    l = quick_sort(nums,0, None)
    print(l)