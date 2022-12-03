"""
File in input.txt
each line contains 2 sections separated by a comma:
a section is 2 numbers with a dash in between (e.g. 1-3, in this case the section contains 1, 2, 3)

PART 1
We need to find on how many lines one section fully contains the other section

PART 2
We need to find on how many lines the 2 sections overlap
"""

def section_contains(section1: (int, int), section2: (int, int)) -> bool:
    """
    returns True if section1 contains section2
    """
    return section1[0] <= section2[0] and section1[1] >= section2[1]

def get_sections(line: str):
    """
    returns the 2 sections of the line
    """
    sections = line.split(",")
    section1 = sections[0].split("-")
    section2 = sections[1].split("-")
    return (int(section1[0]), int(section1[1])), (int(section2[0]), int(section2[1]))

def sections_overlap(section1: (int, int), section2: (int, int)) -> bool:
    """
    returns True if the 2 sections overlap
    """
    return (section1[0] <= section2[1] and section1[1] >= section2[0]) or (section2[0] <= section1[1] and section2[1] >= section1[0])

if __name__ == "__main__":
    total = 0
    total_part_2 = 0
    with open("input.txt", "r") as file_in:
        for line in file_in.readlines():
            section1, section2 = get_sections(line)
            if section_contains(section1, section2) or section_contains(section2, section1):
                total += 1
            if sections_overlap(section1, section2):
                total_part_2 += 1
    print(total)
    print(total_part_2)