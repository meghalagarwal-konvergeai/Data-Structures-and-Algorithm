'''
String 1 -> "saturday"
String 2 -> "sunday"

Stepwise Checking of letters:
    String1 index i1 = 0+1
    String2 index i2 = 0+1
    "s" == "s"
        String1 index i1 = 1+1
        String2 index i2 = 1
        "a" != "u" --> Count = 1
            String1 index i1 = 2+1
            String2 index i2 = 1
            "t" != "u" --> Count = 2
                String1 index i1 = 3+1
                String2 index i2 = 1+1
                "u" == "u"        
                    String1 index i1 = 4+1
                    String2 index i2 = 2
                    "r" != "n" --> Count = 3
                    ."d"
                    ."a"
                    ."y"
                        return 3
'''

def min_edit_distance(str1, str2):
    # Creating a Dictonary to avoid implementation same index combinations repatedly
    memo = {}

    def recurse(i1, i2):
        key = (i1, i2)
    
        if key in memo:
            return memo[key]
        # If index of i1 is exausted in String1 then storing the remaining letters of String2 into the dictonary
        elif i1 == len(str1):
            memo[key] = len(str2) - i2
        # If index of i2 is exausted in String2 then storing the remaining letters of String1 into the dictonary
        elif i2 == len(str2):
            memo[key] = len(str1) - i1
        # If the letters of both the strings matches then moving to the next index
        elif str1[i1] == str2[i2]:
            memo[key] = recurse(i1+1, i2+1)
        else:
            memo[key] = 1 + min(recurse(i1, i2+1), recurse(i1+1, i2), recurse(i1+1, i2+1))
        
        return memo[key]
    
    return recurse(0, 0)

# Program Starts Here
if __name__ == "__main__":
    steps1 = min_edit_distance('intention', 'execution')
    steps2 = min_edit_distance('saturday', 'sunday')

    print("intention, execution --> ", steps1)
    print("saturday, sunday --> ", steps2)