# Script to make new notAdded list because of fuck up in first run of main
import xlrd
import codecs
import additional_functions as af

# Read all mountain peaks from file of form
# Mountain name Mountain height
with codecs.open('Fjelltopper jeg har vært på.txt', encoding='utf8')as f:
    climbed_mountains = f.readlines()

f.close()

# Load mountains that are registered from excel file
# Location of file
loc = r'C:\Users\Henrik\Documents\GitHub\Fjelltoppliste\mytours.xls'

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

notAdded = []
added = []

for i in range(4, sheet.nrows):
    added.append(sheet.cell_value(i, 0).strip())

for mountain in climbed_mountains:
    # Separate mountain name and height
    mountain_info = af.separate_name_and_height(mountain)
    print(mountain_info[0].strip())
    print()
    if mountain_info[0].strip() not in added:
        notAdded.append(mountain_info[0] + ' ' + mountain_info[1])

# Save the mountains not added in text file
f2 = codecs.open("notAddedFirstRun.txt", "w", "utf-8")
for m in notAdded:
    f2.write(m + '\n')

f2.close()

