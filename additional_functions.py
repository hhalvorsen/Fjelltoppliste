import re
import codecs


def separate_name_and_height(info):
    print(info)
    # Separate mountain name and height
    mountain_height = re.findall('[0-9]+', info)[0]
    mountain_name_match = re.search('[0-9]+', info)
    mountain_name = info[:mountain_name_match.start()-1]
    return [mountain_name, mountain_height]


# Read mountain peaks from file
with codecs.open('test.txt', encoding='utf8') as f:
    lines = f.readlines()


# Testing functions
test_list = separate_name_and_height(lines[0])
print(test_list[0])
print(test_list[1])

