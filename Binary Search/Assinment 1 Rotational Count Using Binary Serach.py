'''
Rotational Count Sorting through Binary Search.
-> First Check the mid value is smaller than predecessor, if yes, then return the count
-> Second Check the mid value is smaller than the last value of the list then change High = mid-1 (result lies in LeftHand Side of the list) else Low = mid+1 (result lies in RightHand Side of the list)
'''
#This function first go to the First Position function to find te 1st position and then it will move to Last position
def number_of_rotations(nums):
    low, high = 0, len(nums)-1
    
    while low <= high:
        # The middle position is the answer
        mid = (low+high)//2
        mid_number = nums[mid]
        
        if(mid > 0 and mid_number <= nums[mid-1]):
            return mid
        elif(mid_number>nums[-1]):
            # Answer lies in the right half
            low = mid+1
        else:
            # Answer lies in the left half
            high = mid-1

#Program Starts here
if __name__ == "__main__":
    nums = [5,6,6,9,9,9,0,0,2,3,3,3,3,4,4]
    # Calling a main function.
    count = number_of_rotations(nums)
    print(count)