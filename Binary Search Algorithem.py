
def first_position(nums, target):
    def binary_search(low, high, query):
        while low <= high:
            mid = (low+high)//2
            direction = condition(mid)
            if(direction == "found"):
                return mid
            elif(direction == "left"):
                high = mid-1
            else:
                low = mid+1

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


def last_position(nums, target):
    def binary_search(low, high, query):
        while low <= high:
            mid = (low+high)//2
            direction = condition(mid)
            if(direction == "found"):
                return mid
            elif(direction == "left"):
                high = mid-1
            else:
                low = mid+1

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

def first_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    arr = list(first_last_position(nums, target))
    print(arr)