def merge(nums1, nums2):
    merged = []
    i, j = 0, 0

    while i < len(nums1) and j <len(nums2):
        if(nums1[i]<=nums2[j]):
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    return merged + nums1[i:] + nums2[j:]

def merge_sort(nums):
    if(len(nums) <= 1):
        return nums
    
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    left_sort, right_sort = merge_sort(left), merge_sort(right)
    sorted_num = merge(left_sort, right_sort)

    return sorted_num

if __name__ == "__main__":
    nums = [1,5,4,2,12,35,78,65,0,4,3]
    l = merge_sort(nums)
    print(l)