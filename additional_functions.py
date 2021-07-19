import re


def separate_name_and_height(info):
    # Separate mountain name and height
    mountain_height = re.findall('[0-9]+', info)[0]
    mountain_name_match = re.search('[0-9]+', info)
    mountain_name = info[:mountain_name_match.start()-1]
    return [mountain_name, mountain_height]


def compare_heights(mountain_height, option_height):
    mh = int(mountain_height)
    oh = int(option_height)
    if abs(mh-oh) < 3:
        return True
    else:
        return False


"""
# Testing functions
# Read mountain peaks from file
import codecs # Yes, wrong place to put import
with codecs.open('test.txt', encoding='utf8') as f:
    lines = f.readlines()

test_list = separate_name_and_height(lines[0])
print(test_list[0])
print(test_list[1])


print(compare_heights(200, 200))
print(compare_heights(201, 200))
print(compare_heights(200, 199))
print(compare_heights(200, 197))
"""