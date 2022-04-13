def bubble_sort(nums):
    # Create a copy of the list, to avoid changing it
    nums = list(nums)
    
    #Repeat the process n-1 times
    for _ in range(len(nums) - 1):        
        # Iterate over the array (except last element)
        for i in range(len(nums) - 1):            
            # Compare the number with  
            if nums[i] > nums[i+1]:                
                # Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums

# Program Starts Here
if __name__ == "__main__":
    nums = [5, 2, 6, 1, 23, 7, -12, 12, -243, 0]
    b_s = bubble_sort(nums)
    print(b_s)