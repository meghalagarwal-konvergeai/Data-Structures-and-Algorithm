'''
Stepwise Process:
    --> We'll write a recursive function that computes max_profit(weights[idx:], profits[idx:], capacity), with idx starting from 0.
    --> If weights[idx] > capacity, the current element is cannot be selected, so the maximum profit is the same as max_profit(weights[idx+1:], profits[idx+1:], capacity).
    --> Otherwise, there are two possibilities: we either pick weights[idx] or don't. We can recursively compute the maximum
            A. If we don't pick weights[idx], once again the maximum profit for this case is max_profit(weights[idx+1:], profits[idx+1:], capacity)
            B. If we pick weights[idx], the maximum profit for this case is profits[idx] + max_profit(weights[idx+1:], profits[idx+1:], capacity - weights[idx]
    --> If weights[idx:] is empty, the maximum profit for this case is 0.
Time Complexity of Recursive Ksnapsack Problem is O(2^N)
'''

def knapsack_memo(capacity, weights, profits):
    memo = {}
    
    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx+1, remaining)
        else:
            memo[key] = max(recurse(idx+1, remaining), profits[idx] + recurse(idx+1, remaining-weights[idx]))
        return memo[key] 
        
    return recurse(0, capacity)

# Program Starts Here
if __name__ == "__main__":
    capacity = 165
    weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]

    knapsack_result = knapsack_memo(capacity, weights, profits)
    print(knapsack_result)