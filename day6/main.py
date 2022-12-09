"""
DAY 6

PART 1
input.txt contains a list of characters
we have to iterate through the list until the last 4 characters read are all different
and return the number of characters read 

PART 2
we have to do the same thing but with a sliding window of size 14

"""

def get_number_of_chars(string: str, window_len: int) -> int:
    """
    returns the number of characters read until the last window_len characters read are all different
    """
    chars = dict()
    for idx, char in enumerate(string):
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
        if idx > window_len - 1:
            chars[string[idx - window_len]] -= 1
        
            for char in chars:
                if chars[char] > 1:
                    break
            else: # no break
                return idx + 1

if __name__ == "__main__":
    with open("input.txt", "r") as file_in:
        string = file_in.read()
    # part 1
    print(get_number_of_chars(string, 4))
    # part 2
    print(get_number_of_chars(string, 14))
    