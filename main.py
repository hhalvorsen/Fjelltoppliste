from selenium import webdriver
import codecs
import time
import re
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
    # Select drop down menu
    drop_down_menu = driver.find_element_by_class_name('suggestions')

    # Sleep to let search load
    time.sleep(0.5)

    # Get options from drop down menu
    drop_down_options = drop_down_menu.find_elements_by_tag_name('li')

    mountain_match = True
    # If no mountain has the same name
    if len(drop_down_options) == 0:
        mountain_match = False
    else:
        for option in drop_down_options:
            # Get mountain option height
            option_text = option.find_element_by_class_name('suggestor_text').text
            option_height = re.findall('[0-9]+', option_text)[0]
            if af.compare_heights(mountain_info[1], option_height):
                option.click()
                action_line = driver.find_element_by_class_name('actionLine')
                save_button = action_line.find_elements_by_tag_name('input')[0]
                save_button.click()
                break
            else:
                mountain_match = False

    # If unable to find mountain, add to notAdded list and continue to next mountain
    if not mountain_match:
        notAdded.append(mountain_info[0] + ' ' + mountain_info[1])

    # Press home button
    home_button = driver.find_element_by_xpath("//a[contains(text(), 'Hjem')]")
    home_button.click()


# Save notAdded in text file
f2 = open("notAdded.txt", "w")
f2.writelines(notAdded)
f2.close()

