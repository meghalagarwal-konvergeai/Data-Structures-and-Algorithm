'''
Stepwise Process:
--> Create a table of size (n+1) * (capacity+1) consisting of all 0s, where is n is the number of elements. 
    table[i][c] represents the maximum profit that can be obtained using the first i elements if the maximum capacity is c.
--> We'll fill the table row by row and column by column. table[i][c] can be filled using some values in the row above it.
--> If weights[i] > c i.e. if the current element can is larger than capacity, then table[i+1][c] is simply equal to table[i][c] (since there's no way we can pick this element).
--> If weights[i] <= c then we have two choices: to either pick the current element or not to get the value of table[i+1][c].
    We can compare the maximum profit for both these options and pick the better one as the value of table[i][c].
        A. If we don't pick the element with weight weights[i], then once again the maximum profit is table[i][c]
        B. If we pick the element with weight weights[i], then the maximum profit is profits[i] + table[i][c-weights[i]], since we have used up some capacity.
Time Complexity of Recursive Ksnapsack Problem is O(N * W)
'''

def knapsack_dp(capacity, weights, profits):
    n = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    
    for idx in range(n):
        for c in range(capacity+1):
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            else:
                results[idx+1][c] = max(results[idx][c], profits[idx] + results[idx][c-weights[idx]])
            
    return results[-1][-1]

# Program Starts Here
if __name__ == "__main__":
    capacity = 165
    weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]

    knapsack_result = knapsack_dp(capacity, weights, profits)
    print(knapsack_result)