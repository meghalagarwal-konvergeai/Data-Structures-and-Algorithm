'''
Dynamic Programing works on the basis of the Matrix

                    - p r e c i p i t a t i o n
                -
                s   0 0 0 0 0 0 0 0 0 0 0 0 0 0
                e   0 0 0 1 1 1 1 1 1 1 1 1 1 1
                r   0 0 1 1 1 1 1 1 1 1 1 1 1 1
                e   0 0 1 2 2 2 2 2 2 2 2 2 2 2
                n   0 0 1 2 2 2 2 2 2 2 2 2 2 3
                d   0 0 1 2 2 2 2 2 2 2 2 2 2 2
                i   0 0 1 2 2 3 3 3 3 3 3 3 3 3
                p   0 0 1 2 2 3 4 4 4 4 4 4 4 4
                i   0 0 1 2 2 3 4 5 5 5 5 5 5 5
                t   0 0 1 2 2 3 4 5 6 6 6 6 6 6
                o   0 0 1 2 2 3 4 5 6 6 6 6 7 7
                u   0 0 1 2 2 3 4 5 6 6 6 6 7 7
                s   0 0 1 2 2 3 4 5 6 6 6 6 7 7

Time Complexity of Dynamic Programing if O(n1 * n2)
'''

def lcq_dp(seq1, seq2):
    n1, n2 = len(seq1), len(seq2)
    # Creating a Matrix based on the length of both the strings
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if seq1[i] == seq2[j]:
                results[i+1][j+1] = 1 + results[i][j]
            else:
                results[i+1][j+1] = max(results[i][j+1], results[i+1][j])
    return results[-1][-1]

# Program Starts Here
if __name__ == "__main__":
    seq1, seq2 = 'serendipitous', 'precipitation'

    lcs_count = lcq_dp(seq1, seq2)
    print(lcs_count)