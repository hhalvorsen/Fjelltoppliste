from selenium import webdriver
from selenium.webdriver.support.ui import Select
import codecs
import additional_functions as af
# Script made to automatically add the mountains I've climbed from my list into peakbook


# Read mountain peaks from file
with codecs.open('Fjelltopper jeg har vært på.txt', encoding='utf8')as f:
    lines = f.readlines()

# List of mountains not added to peakbook for some reason
notAdded = ["test"]

# Open peakbook.org and log in
# Using Chrome to access web
driver = webdriver.Chrome()

# Open the website
driver.get('https://peakbook.org')

# Open log in dialog
open_login_button = driver.find_element_by_class_name('login')
open_login_button.click()

# Enter username and password
username_box = driver.find_element_by_name('logindata[username]')
username_box.send_keys('hhalvorsen')
password_box = driver.find_element_by_name('logindata[password]')
password_box.send_keys('Jul38rus')

# Log in
login_button = driver.find_element_by_name('login')
login_button.click()

# Run through all mountains
for mountain_string in lines:
    # Separate mountain name and height
    mountain_info = af.separate_name_and_height(mountain_string)

    # Open "Register new trip"-dialog
    register_trip_button = driver.find_element_by_link_text('Registrer tur')
    register_trip_button.click()

    # Add title
    title_box = driver.find_element_by_name('formdata[title]')
    title_box.send_keys(mountain_info[0])

    # Check for unknown time of ascent
    time_unknown_box = driver.find_element_by_name('formdata[dateUnknown]')
    time_unknown_box.click()

    # Enter mountain into search field
    mountain_box = driver.find_element_by_id('toursPBEs_input')
    mountain_box.send_keys(mountain_info[0])

    # Choose correct mountain
    # Get options from drop down menu
    drop_down_selector = Select(driver.find_element_by_class_name('suggestions'))
    drop_down_options = drop_down_selector.options

    mountain_match = True
    # If no mountain has the same name
    if len(drop_down_options) == 0:
        notAdded.append(mountain_info[0] + ' ' + mountain_info[1])
        mountain_match = False
    else:
        for option in drop_down_options:
            option_height = option.find_element_by_class_name('suggestor_text')
            print(option_height.text)
        # If unable to find mountain, add to notAdded list and continue to next mountain
    # Press home button
    break


# Save notAdded in text file
f2 = open("notAdded.txt", "w")
f2.writelines(notAdded)
f2.close()

