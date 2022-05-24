# Jovian Commit Essentials
# Please retain and execute this cell without modifying the contents for `jovian.commit` to work
!pip install jovian --upgrade -q
import jovian
jovian.set_project('python-divide-and-conquer-assignment')
jovian.set_colab_id('1VGF01oQfILRluWl7XYpKiNyGgqzFVX7-')

     |████████████████████████████████| 68 kB 2.8 MB/s 
  Building wheel for uuid (setup.py) ... done

Assignment 3 - Divide-n-Conquer Algorithms in Python

This assignment is a part of the course "Data Structures and Algorithms in Python".

In this assignment, you will implement an efficient algorithm for polynomial multiplication.

As you go through this notebook, you will find the symbol ??? in certain places. To complete this assignment, you must replace all the ??? with appropriate values, expressions or statements to ensure that the notebook runs properly end-to-end.

Guidelines

    Make sure to run all the code cells, otherwise you may get errors like NameError for undefined variables.
    Do not change variable names, delete cells or disturb other existing code. It may cause problems during evaluation.
    In some cases, you may need to add some code cells or new statements before or after the line of code containing the ???.
    Since you'll be using a temporary online service for code execution, save your work by running jovian.commit at regular intervals.
    Questions marked (Optional) will not be considered for evaluation, and can be skipped. They are for your learning.
    If you are stuck, you can ask for help on the [community forum] (TODO - add link). Post errors or ask for hints, but please don't ask for OR share the full working answer code on the forum.
    There are some tests included with this notebook to help you test your implementation. However, after submission your code will be tested with some hidden test cases. Make sure to test your code exhaustively to cover all edge cases.

Important Links

    Submit your work here: https://jovian.ai/learn/data-structures-and-algorithms-in-python/assignment/assignment-3-sorting-and-divide-conquer-practice
    Ask questions and get help: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-3/89
    Lesson 3 video for review: https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-3-sorting-algorithms-and-divide-and-conquer
    Lesson 3 notebook for review: https://jovian.ai/aakashns/python-sorting-divide-and-conquer

How to Run the Code and Save Your Work

Option 1: Running using free online resources (1-click, recommended): Click the Run button at the top of this page and select Run on Binder. You can also select "Run on Colab" or "Run on Kaggle", but you'll need to create an account on Google Colab or Kaggle to use these platforms.

Option 2: Running on your computer locally: To run the code on your computer locally, you'll need to set up Python & Conda, download the notebook and install the required libraries. Click the Run button at the top of this page, select the Run Locally option, and follow the instructions.

Saving your work: You can save a snapshot of the assignment to your Jovian profile, so that you can access it later and continue your work. Keep saving your work by running jovian.commit from time to time.

project='python-divide-and-conquer-assignment-practice'

!pip install jovian --upgrade --quiet

import jovian
jovian.commit(project=project, privacy='secret', environment=None)

[jovian] Detected Colab notebook...
[jovian] Please enter your API key ( from https://jovian.ai/ ):
API KEY: ··········
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice

'https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice'

Problem Statement - Polynomial Multiplication

    Given two polynomials represented by two lists, write a function that efficiently multiplies given two polynomials. For example, the lists [2, 0, 5, 7] and [3, 4, 2] represent the polynomials 

and

.

Their product is

i.e.

    It can be represented by the list [6, 8, 19, 41, 38, 14].

The Method

Here's the systematic strategy we'll apply for solving problems:

    State the problem clearly. Identify the input & output formats.
    Come up with some example inputs & outputs. Try to cover all edge cases.
    Come up with a correct solution for the problem. State it in plain English.
    Implement the solution and test it using example inputs. Fix bugs, if any.
    Analyze the algorithm's complexity and identify inefficiencies, if any.
    Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

This approach is explained in detail in Lesson 1 of the course. Let's apply this approach step-by-step.
Solution
1. State the problem clearly. Identify the input & output formats.

While this problem is stated clearly enough, it's always useful to try and express in your own words, in a way that makes it most clear for you.

Problem

    Write a function that multiplies two polynomials, represented by two lists.


Input

    [2, 4, 0, 0, 5] and [4, 9, 5, 4]
    [2, 4] and [2, 7, 5]

Output

    [8 34 46 28 36 45 25 20]
    [4 22 38 20]


Based on the above, we can now create a signature of our function:

def multiply(poly1, poly2):
    pass

import jovian

jovian.commit()

[jovian] Detected Colab notebook...
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice

'https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice'

2. Come up with some example inputs & outputs. Try to cover all edge cases.

Our function should be able to handle any set of valid inputs we pass into it. List a few scenarios here:

    One list is empty (result would be 0s)
    One list is of 1s (result would be Other List).
    Both lists are same.
    Both lists are of same/different size (a really long list.).
    A list containing just one element. (add more if required)

Create a test case of each of the above scenarios. We'll express our test cases as dictionaries, to test them easily. Each dictionary will contain 2 keys: input (a dictionary itself containing one key for each argument to the function and output (the expected result from the function).

test0 = {
    'input': {
        'poly1': [2, 0, 5, 7],
        'poly2': [3, 4, 2]
    },
    'output': [6, 8, 19, 41, 38, 14]
}

test1 = {
    'input': {
        'poly1': [2, 4, 0, 0, 5],
        'poly2': [4, 9, 5, 4]
    },
    'output': [8, 34, 46, 28, 36, 45, 25, 20]
}

test2 = {
    'input': {
        'poly1': [2, 4],
        'poly2': [2, 7, 5]
    },
    'output': [4, 22, 38, 20]
}

test3 = {
    'input': {
        'poly1': [1, 1, 1],
        'poly2': [2, 7, 5]
    },
    'output': [2, 9, 14, 12, 5]
}

test4 = {
    'input': {
        'poly1': [],
        'poly2': [2, 7, 4]
    },
    'output': []
}

test5 = {
    'input': {
        'poly1': [0, 1],
        'poly2': [2, 6, -5, 3, 4]
    },
    'output': [0, 2, 6, -5, 3, 4]
}

test6 = {
    'input': {
        'poly1': [1],
        'poly2': [2, 6, 5, 3, 4]
    },
    'output': [2, 6, 5, 3, 4]
}

test7 = {
    'input': {
        'poly1': [],
        'poly2': [1]
    },
    'output': []
}

test8 = {
    'input': {
        'poly1': [2, 5, 3, 1, -1],
        'poly2': [1, 2, 2, 3, 6]
    },
    'output': [2, 9, 17, 23, 34, 39, 19, 3, -6]
}

Let's store all the test cases in a list, for easier automated testing.

tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

import jovian

jovian.commit()

[jovian] Detected Colab notebook...
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice

'https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice'

3. Come up with a correct solution for the problem. State it in plain English.

Our first goal should always be to come up with a correct solution to the problem, which may not necessarily be the most efficient solution.

Here's the simplest solution: If you have lists poly1 and poly2 representing polynomials of length
and respectively, the highest degree of the exponents are and respectively. Their product has the degree i.e . The list representing the product has the length . So, we can create a list result of length

, and set

result[k] = Sum of all the pairs poly1[i] * poly2[j] where i+j = k

Example:

Explain this solution in your own words below:

    Create an emply list (result) with len(poly1) + len(poly2) - 1. Set the first element result[0] to poly1[0]*poly2[0] as this would be the value with multiplier x 0 .
    Second element result[1] would be poly1[1]poly2[0] + poly1[0]poly2[1], as these would have x 1 multiplier.
    Effectively, index could be read as the degree of the exponents and the value at the index as multiplier. i.e. result[k] = Sum of all the pairs poly1[i] * poly2[j] where i+j = k

Let's save and upload our work before continuing.

import jovian

jovian.commit()

[jovian] Detected Colab notebook...
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice

'https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice'

4. Implement the solution and test it using example inputs. Fix bugs, if any.

Implement the solution

def multiply_basic(poly1, poly2):
    m = len(poly1)
    n = len(poly2)
    
    if m>0 and n>0:
      result = [0]*(m + n - 1) 
      for i in range(m):
        for j in range(n):
          result[i+j] += poly1[i] * poly2[j]           
    
    elif m==0 or n==0:
        result = [] 
    
    elif n==0:
        result = []
    
    return result

Test your solution using the test cases you've defined above.

print('Input-1:', test1['input']['poly1'])
print('Input-2:', test1['input']['poly2'])
print('Expected output:', test1['output'])
result1 = multiply_basic(test1['input']['poly1'], test1['input']['poly2'])
print('Actual output:', result1)
print('Match:', result1 == test1['output'])

Input-1: [2, 4, 0, 0, 5]
Input-2: [4, 9, 5, 4]
Expected output: [8, 34, 46, 28, 36, 45, 25, 20]
Actual output: [8, 34, 46, 28, 36, 45, 25, 20]
Match: True

from jovian.pythondsa import evaluate_test_cases

results = evaluate_test_cases(multiply_basic, tests)

TEST CASE #0

Input:
{'poly1': [2, 0, 5, 7], 'poly2': [3, 4, 2]}

Expected Output:
[6, 8, 19, 41, 38, 14]


Actual Output:
[6, 8, 19, 41, 38, 14]

Execution Time:
0.015 ms

Test Result:
PASSED


TEST CASE #1

Input:
{'poly1': [2, 4, 0, 0, 5], 'poly2': [4, 9, 5, 4]}

Expected Output:
[8, 34, 46, 28, 36, 45, 25, 20]


Actual Output:
[8, 34, 46, 28, 36, 45, 25, 20]

Execution Time:
0.018 ms

Test Result:
PASSED


TEST CASE #2

Input:
{'poly1': [2, 4], 'poly2': [2, 7, 5]}

Expected Output:
[4, 22, 38, 20]


Actual Output:
[4, 22, 38, 20]

Execution Time:
0.011 ms

Test Result:
PASSED


TEST CASE #3

Input:
{'poly1': [1, 1, 1], 'poly2': [2, 7, 5]}

Expected Output:
[2, 9, 14, 12, 5]


Actual Output:
[2, 9, 14, 12, 5]

Execution Time:
0.013 ms

Test Result:
PASSED


TEST CASE #4

Input:
{'poly1': [], 'poly2': [2, 7, 4]}

Expected Output:
[]


Actual Output:
[]

Execution Time:
0.004 ms

Test Result:
PASSED


TEST CASE #5

Input:
{'poly1': [0, 1], 'poly2': [2, 6, -5, 3, 4]}

Expected Output:
[0, 2, 6, -5, 3, 4]


Actual Output:
[0, 2, 6, -5, 3, 4]

Execution Time:
0.012 ms

Test Result:
PASSED


TEST CASE #6

Input:
{'poly1': [1], 'poly2': [2, 6, 5, 3, 4]}

Expected Output:
[2, 6, 5, 3, 4]


Actual Output:
[2, 6, 5, 3, 4]

Execution Time:
0.009 ms

Test Result:
PASSED


TEST CASE #7

Input:
{'poly1': [], 'poly2': [1]}

Expected Output:
[]


Actual Output:
[]

Execution Time:
0.003 ms

Test Result:
PASSED


TEST CASE #8

Input:
{'poly1': [2, 5, 3, 1, -1], 'poly2': [1, 2, 2, 3, 6]}

Expected Output:
[2, 9, 17, 23, 34, 39, 19, 3, -6]


Actual Output:
[2, 9, 17, 23, 34, 39, 19, 3, -6]

Execution Time:
0.019 ms

Test Result:
PASSED


SUMMARY

TOTAL: 9, PASSED: 9, FAILED: 0

import jovian

jovian.commit()

[jovian] Detected Colab notebook...
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice

'https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice'

5. Analyze the algorithm's complexity and identify inefficiencies, if any.

Can you analyze the time and space complexity of this algorithm?

multiply_basic_time_complexity = 'O(n^2)'

multiply_basic_space_complexity = 'O(N*N)' 

import jovian

jovian.commit()

[jovian] Detected Colab notebook...
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice

'https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice'

6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

We can apply the divide and conquer technique to solve this problem more efficiently. Given two polynomials A and B, we can express each of them as a sum of two polynomials as follows:

We need to compute the terms A0 * B0, A1 * B0 + A0 * B1 and A1 * B1. This can obviously be done using 4 multiplications, but here's a way of doing it with just three multiplications:

Each of the products can themselves be computed recursively. For a more detailed explanation of this approach see http://www.cse.ust.hk/~dekai/271/notes/L03/L03.pdf .

Need help? Discuss and ask questions on the forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/assignment-3/89
7. Come up with a correct solution for the problem. State it in plain English.

Explain the approach described above in your own words below:

1.Divide the polynomials A & B in smaller polynomials Such as A(x)as A0(x) and A1(x)(say half)

    The original problem of size n is divided into 4 problems of input size n/2.
    Solve the four subproblems, by recursively calling the algorithm 4 times.

Let's save and upload our work before continuing.

import jovian

jovian.commit()

[jovian] Detected Colab notebook...
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice

'https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice'

8. Implement the solution and test it using example inputs. Fix bugs, if any.

We are now ready to implement the solution. You may find the following functions add, split and increase_exponent useful.

def add(poly1, poly2):
    """Add two polynomials"""
    result = [0] * max(len(poly1), len(poly2))
    for i in range(len(result)):
        if i < len(poly1):
            result[i] += poly1[i]
        if i < len(poly2):
            result[i] += poly2[i]
    return result

add([1, 2, 3, 4], [0, 4, 3])

[1, 6, 6, 4]

def split(poly1, poly2):
    """Split each polynomial into two smaller polynomials"""
    mid = max(len(poly1), len(poly2)) // 2
    return  (poly1[:mid], poly1[mid:]), (poly2[:mid], poly2[mid:])

split([1, 2, 3, 4], [0, 4, 3, 6, 7, 8, 2])

(([1, 2, 3], [4]), ([0, 4, 3], [6, 7, 8, 2]))

def increase_exponent(poly, n):
    """Multiply poly1 by x^n"""
    return [0] * n + poly

increase_exponent([1, 2, 3, 4], 3)

[0, 0, 0, 1, 2, 3, 4]

Implement the optimized multiplication algorithm below. You may use the some or all of the helper functions defined above.

# What this does is takes the first element of poly1, multiplies all elements of poly2


# Standardizes the polynomial (Gets rid of trailing 0s)
def standardize(poly):
    poly = list(poly) # make a copy
    if poly[len(poly)-1] == 0: # Check if the last element in the list is 0
        poly.pop() #If last element is zero, remove from the list
    return poly

# Finds if the polynomial is 0
def isZeroPoly(poly):
    if poly == []: # Check if poly is blank [] or [0]<= standardize would remove the zero and return []
        return True
    else:
        return False

# Scales the polynomial by the scale variable ((3,[1,2,3]) => [3,6,9])
def scalePoly(scale,poly):
    poly = list(poly)
    for x in range(0,len(poly)): # For final assembly of resulting poly
        poly[x] = (poly[x] * scale)
    poly = standardize(poly)
    return poly

# Gives the constant in the polynomial ([2,3,4] => [2])
def constCoef(poly):
    constant = poly[0]
    return constant

# Shifts the polynomial left ([2,3,4] => [0,2,3,4])
def shiftLeft(poly):
    newpoly = []
    newpoly.append(0)
    for x in range(0,len(poly)): # Increase exponent
        newpoly.append(poly[x])
    return newpoly

# Shifts the polynomial right ([2,3,4] => [3,4])
def shiftRight(poly):
    #poly.remove(poly[0])
    return poly[1:]

def multiply_optimized(poly1, poly2):
    # print (poly1, poly2)
    if isZeroPoly(poly1):
        return []
    else:
        return add(multiply_optimized(shiftRight(poly1), shiftLeft(poly2)),
            scalePoly(constCoef(poly1), poly2))
        

Test your solution using the empty cells below.

multiply_optimized([1, 2, 3, 4], [0, 4, 3, 6, 7, 8, 2])

[0, 4, 11, 24, 44, 52, 63, 56, 38, 8]

results = evaluate_test_cases(multiply_optimized, tests)

TEST CASE #0

Input:
{'poly1': [2, 0, 5, 7], 'poly2': [3, 4, 2]}

Expected Output:
[6, 8, 19, 41, 38, 14]


Actual Output:
[6, 8, 19, 41, 38, 14]

Execution Time:
0.086 ms

Test Result:
PASSED


TEST CASE #1

Input:
{'poly1': [2, 4, 0, 0, 5], 'poly2': [4, 9, 5, 4]}

Expected Output:
[8, 34, 46, 28, 36, 45, 25, 20]


Actual Output:
[8, 34, 46, 28, 36, 45, 25, 20]

Execution Time:
0.081 ms

Test Result:
PASSED


TEST CASE #2

Input:
{'poly1': [2, 4], 'poly2': [2, 7, 5]}

Expected Output:
[4, 22, 38, 20]


Actual Output:
[4, 22, 38, 20]

Execution Time:
0.03 ms

Test Result:
PASSED


TEST CASE #3

Input:
{'poly1': [1, 1, 1], 'poly2': [2, 7, 5]}

Expected Output:
[2, 9, 14, 12, 5]


Actual Output:
[2, 9, 14, 12, 5]

Execution Time:
0.043 ms

Test Result:
PASSED


TEST CASE #4

Input:
{'poly1': [], 'poly2': [2, 7, 4]}

Expected Output:
[]


Actual Output:
[]

Execution Time:
0.003 ms

Test Result:
PASSED


TEST CASE #5

Input:
{'poly1': [0, 1], 'poly2': [2, 6, -5, 3, 4]}

Expected Output:
[0, 2, 6, -5, 3, 4]


Actual Output:
[0, 2, 6, -5, 3, 4]

Execution Time:
0.046 ms

Test Result:
PASSED


TEST CASE #6

Input:
{'poly1': [1], 'poly2': [2, 6, 5, 3, 4]}

Expected Output:
[2, 6, 5, 3, 4]


Actual Output:
[2, 6, 5, 3, 4]

Execution Time:
0.028 ms

Test Result:
PASSED


TEST CASE #7

Input:
{'poly1': [], 'poly2': [1]}

Expected Output:
[]


Actual Output:
[]

Execution Time:
0.003 ms

Test Result:
PASSED


TEST CASE #8

Input:
{'poly1': [2, 5, 3, 1, -1], 'poly2': [1, 2, 2, 3, 6]}

Expected Output:
[2, 9, 17, 23, 34, 39, 19, 3, -6]


Actual Output:
[2, 9, 17, 23, 34, 39, 19, 3, -6]

Execution Time:
0.082 ms

Test Result:
PASSED


SUMMARY

TOTAL: 9, PASSED: 9, FAILED: 0

import jovian

jovian.commit()

[jovian] Detected Colab notebook...
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice

'https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice'

Make a Submission

Congrats! You have now implemented hash tables from scratch. The rest of this assignment is optional.

You can make a submission on this page: https://jovian.ai/learn/data-structures-and-algorithms-in-python/assignment/assignment-3-sorting-and-divide-conquer-practice

Submit the link to your Jovian notebook (the output of the previous cell). You can also make a direct submission by executing the following cell:

jovian.submit(assignment="pythondsa-assignment3")

[jovian] Detected Colab notebook...
[jovian] Uploading colab notebook to Jovian...
Committed successfully! https://jovian.ai/deepak-dewani/python-divide-and-conquer-assignment-practice
[jovian] Submitting assignment..
[jovian] Verify your submission at https://jovian.ai/learn/data-structures-and-algorithms-in-python/assignment/assignment-3-sorting-and-divide-conquer-practice

(Optional) 9. Analyze the algorithm's complexity and identify inefficiencies, if any.

Can you analyze the time and space complexity of this algorithm?

Hint: See the tree of subproblems below (source). Substitute the right values for n and b to determine the time complexity.

import jovian

jovian.commit()

[jovian] Attempting to save notebook..
[jovian] Updating notebook "aakashns/python-divide-and-conquer-assignment" on https://jovian.ai/
[jovian] Uploading notebook..
[jovian] Capturing environment..
[jovian] Committed successfully! https://jovian.ai/aakashns/python-divide-and-conquer-assignment

'https://jovian.ai/aakashns/python-divide-and-conquer-assignment'

