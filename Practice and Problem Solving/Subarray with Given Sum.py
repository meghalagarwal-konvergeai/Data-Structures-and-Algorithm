'''
Considering 2 indexes first index as "i" and second index as "j"
[1, 7, 4, 2, 1, 3, 11, 5]
    1st iteration -> index i = 0
    1st iteration -> index j = 0+1
    1st iteration -> sum += 1
        2nd iteration -> index i = 0
        2nd iteration -> index j = 2+1
        2nd iteration -> sum += 8
            3rd iteration -> index i = 0+1
            3rd iteration -> index j = 3
            3rd iteration -> sum += 12
                4th iteration -> index i = 1+1
                4th iteration -> index j = 3
                4th iteration -> sum -= 11
                    5th iteration -> index i = 2
                    5th iteration -> index j = 3+1
                    5th iteration -> sum -= 4
                        6th iteration -> index i = 2
                        6th iteration -> index j = 4+1
                        6th iteration -> sum += 6
                            7th iteration -> index i = 2
                            7th iteration -> index j = 5+1
                            7th iteration -> sum += 7
                                8th iteration -> index i = 2
                                8th iteration -> index j = 6
                                8th iteration -> sum += 10
                                    return 2, 6                  
'''
def subarray_sum(arr, target):
    n = len(arr)
    i, j, s = 0, 0, 0
    # Checking whether the indexes have reached to the end of the list.
    while i < n and j <= n:
        if s == target:
            return i, j
        # Checking if sum of elements is less than the Target value then shifting to the next index in the list.
        elif s < target:
            s += arr[j]
            j += 1
        # Checking if the sum of elements is more than the Target value then substracting the first element of the list and shifting the . 
        elif s > target:
            s -= arr[i]
            i += 1
    return None, None

# Program Starts Here
if __name__ == "__main__":
    arr = [1, 7, 4, 2, 1, 3, 11, 5]
    target = 10
    init_idx, lst_idx = subarray_sum(arr, target)
    print(init_idx, lst_idx, arr[init_idx:lst_idx])