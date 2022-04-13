'''
Hashing Function
A hashing function is used to convert strings and other non-numeric data types into numbers, which can then be used as list indices. For instance, if a hashing function converts the string "Aakash" into the number 4, then the key-value pair ('Aakash', '7878787878') will be stored at the position 4 within the data list.

Here's a simple algorithm for hashing, which can convert strings into numeric list indices.

-> Iterate over the string, character by character
-> Convert each character to a number using Python's built-in "ord function".
-> Add the numbers for each character to obtain the hash for the entire string
-> Take the remainder of the result with the size of the data list
'''

# Defines and return the index value
def get_index(data_list, a_string):
    result = 0    
    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        result += a_number    
    # Random Creation of Index Numbers
    list_index = result % len(data_list)

    return list_index

def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)
    
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        
        # If it is None, return the index
        if kv is None:
            return idx
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx
        
        # Move to the next index
        idx += 1
        
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0

class ProbingHashTable:
    def __init__(self):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None]*12
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key, value)
     
    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]
     
    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key, value)
    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv for kv in self.data_list if kv is not None]

# Program Starts Here
if __name__ == "__main__":
    # Defining the Size of a Data List
    data_list = [None] * 4096
    data_list[get_index(data_list, 'listen')] = ('listen', 99)
    index = get_valid_index(data_list, 'listen')
    print(data_list[index])