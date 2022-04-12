'''
Rotational Count Sorting through Binary Search.
-> First Check the mid value is smaller than predecessor, if yes, then return the count
-> Second Check the mid value is smaller than the last value of the list then change High = mid-1 (result lies in LeftHand Side of the list) else Low = mid+1 (result lies in RightHand Side of the list)
'''

def number_of_rotations(nums):
    low, high = 0, len(nums)-1
    
    while low <= high:
        mid = (low+high)//2
        mid_number = nums[mid]
        print({"low":low, "High":high, "Mid":mid, "Number":nums[mid]})
        if(mid > 0 and mid_number <= nums[mid-1]):
            return mid
        elif(mid_number>nums[-1]):
            low = mid+1
        else:
            high = mid-1

if __name__ == "__main__":
    nums = [5,6,6,9,9,9,0,0,2,3,3,3,3,4,4]
    count = number_of_rotations(nums)
    print(count)