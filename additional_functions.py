import re
import time
from selenium import common


def separate_name_and_height(info):
    # Separate mountain name and height
    print(info)
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


def try_to_find_title_box(driver):
    a = 1  # Iterator to keep track of number of repetitions
    print("Couldn't find title box, trying again. " + str(a))
    while a < 10:
        a = a + 1
        time.sleep(0.5)
        try:
            # Check if title box exists
            title_box = driver.find_element_by_name('formdata[title]')
        except common.exceptions.NoSuchElementException:
            print("Couldn't find title box, trying again. " + str(a))
        except:
            print("Something else went wrong. " + str(a))
        else:
            return title_box

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