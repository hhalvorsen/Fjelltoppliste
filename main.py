import selenium as s

# Script made to automatically add the mountains I've climbed from my list into peakbook

# Read mountain peaks from file
with open('Fjelltopper jeg har vært på.txt') as f:
    lines = f.readlines()

# List of mountains not added to peakbook for some reason
notAdded = ["test"]

# Open peakbook.org and log in
# Using Chrome to access web
driver = s.webdriver.Chrome()
# Open the website
driver.get('https://peakbook.org')
# Open log in dialog
open_login_button = driver.find_element_by_class('login')
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
for mountain in lines:
    print(mountain)
    # Open "Register new trip"-dialog
    # Add title
    # Check for unknown time of ascent
    # Enter mountain into search field
    # Choose correct mountain
        # If unable to find mountain, add to notAdded list and continue to next mountain
    # Press home button

# Save notAdded in text file
f2 = open("notAdded.txt", "w")
f2.writelines(notAdded)
f2.close()



