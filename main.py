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

# Run through all mountains
for mountain in lines:
    print(mountain)
    # If mountain region or blank line, skip line
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



