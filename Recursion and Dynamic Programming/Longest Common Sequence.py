'''
Longest Common Subsequence:
A "sequence" is a group of items with a deterministic ordering.
Lists, tuples and ranges are some common sequence types in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence.
For example, "edpt" is a subsequence of "serendipitous".
Time Complexity of LCS is O(2^m+n)
'''

def lcs_memo (seq1, seq2):
    memo = {}
    
    def recurse(idx1=0, idx2=0):
        key=(idx1, idx2)
        if(key in memo):
            return memo[key]
        elif(idx1 == len(seq1) or idx2 == len(seq2)):
            memo[key] = 0
        elif(seq1[idx1] == seq2[idx2]):
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        return memo[key]
    return recurse(0, 0)

if __name__ == "__main__":
    seq1, seq2 = 'serendipitous', 'precipitation'

    lcs_count = lcs_memo(seq1, seq2)
    print(lcs_count)