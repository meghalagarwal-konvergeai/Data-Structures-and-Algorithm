'''
Question: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number. 

Solution:
1. The numbers are sorted in increasing order.
2. We are looking for both the increasing order and the decreasing order.
'''
#This function will return the the 1st Position of the target value.
def first_position(nums, target):

    #It is a generic Binary Search Algorithm
    def binary_search(low, high, query):
        while low <= high:
            # The middle position is the answer
            mid = (low+high)//2
            direction = condition(mid)
            if(direction == "found"):
                return mid
            elif(direction == "left"):
                high = mid-1
            else:
                low = mid+1

    #It is going to check whther the value is repeated second time or first time or t zeroeth position
    def condition(mid):
        if(nums[mid] == target):
            if(mid > 0 and nums[mid-1] == target):
                return "left"
            return "found"
        elif(nums[mid] < target):
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, target)

#This function will return the the last Position of the target value.
def last_position(nums, target):

    #It is a generic Binary Search Algorithm
    def binary_search(low, high, query):
        while low <= high:
            # The middle position is the answer
            mid = (low+high)//2
            direction = condition(mid)
            if(direction == "found"):
                return mid
            elif(direction == "left"):
                high = mid-1
            else:
                low = mid+1

    #It is going to check whther the value is repeated second time or first time or t zeroeth position
    def condition(mid):
        if(nums[mid] == target):
            if(mid < (len(nums)-1) and nums[mid+1] == target):
                return "right"
            return "found"
        elif(nums[mid] < target):
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums)-1, target)

#This function first go to the First Position function to find te 1st position and then it will move to Last position
def first_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

#Program Starts here
if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    # Calling a main function and storing the returned value in a list.
    arr = list(first_last_position(nums, target))
    print(arr)