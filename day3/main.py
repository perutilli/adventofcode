"""
DAY 3
"""


def get_wrong_letter(string:str):
    """
    returns the letter that appears in both halfs of the string
    """
    str1 = string[:len(string)//2]
    str2 = string[len(string)//2:]
    for letter in str1:
        if letter in str2:
            return letter
    raise Exception("No letter found")

def get_char_value(char:str):
    """
    returns the value of the character
    """
    if ord(char) >= ord('a') and ord(char) <= ord('z'):
        return ord(char) - ord('a') + 1
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return ord(char) - ord('A') + 27
    raise Exception("Invalid character")

def get_badge_tag(line1:str, line2:str, line3:str):
    """
    returns the only letter that is present in line1, line2 and line3
    """
    for letter in line1:
        if letter in line2 and letter in line3:
            return letter
    raise Exception("No letter found")


if __name__ == "__main__":
    total_part_1 = 0
    total_part_2 = 0
    with open("input.txt", "r") as file_in:
        lines = file_in.readlines()
        for line in lines:
            total_part_1 += get_char_value(get_wrong_letter(line[:-1])) # -1 to remove the newline character
        n_groups = len(lines) // 3
        for group in range(n_groups):
            try:
                total_part_2 += get_char_value(get_badge_tag(lines[group * 3][:-1], lines[group * 3 + 1][:-1], lines[group * 3 + 2][:-1]))
            except Exception:
                print("Error in group", group)
                print(lines[group * 3][:-1], lines[group * 3 + 1][:-1], lines[group * 3 + 2][:-1])
                exit()
    print(total_part_1)
    print(total_part_2)
        