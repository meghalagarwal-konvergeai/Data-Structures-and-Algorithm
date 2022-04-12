'''
Hashing Function
A hashing function is used to convert strings and other non-numeric data types into numbers, which can then be used as list indices. For instance, if a hashing function converts the string "Aakash" into the number 4, then the key-value pair ('Aakash', '7878787878') will be stored at the position 4 within the data list.

Here's a simple algorithm for hashing, which can convert strings into numeric list indices.

-> Iterate over the string, character by character
-> Convert each character to a number using Python's built-in "ord function".
-> Add the numbers for each character to obtain the hash for the entire string
-> Take the remainder of the result with the size of the data list
'''

def get_index(data_list, a_string):
    result = 0    
    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        result += a_number    
    list_index = result % len(data_list)

    return list_index

if __name__ == "__main__":
    phone_numbers = {'Aakash' : '9489484949','Hemanth' : '9595949494','Siddhant' : '9231325312'}
    data_list = [None] * 235
    index = get_index(data_list, "Aakash")
    print(index)