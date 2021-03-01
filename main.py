#Practicing Web Scraping in Python
#
#TODO:
#[X] Get and parse data
#   optional:
#		[-] Use numpy arrays if you need more speed
#		[X] Measure how long this takes: <0.01s is fast enough -2/17/2021
#[X] Store responses in a data structure -2/17/2021
#[X] Convert into a function that takes url and returns obj -2/18/2021
#[X] Use persistant storage eg. file, or database -> shelve	-2/19/2021
#		[X] Only store new sectionList if it's different -2/21/2021
#			 [X] Write function to check sectionList equality - 2/21/2021
#		[X] Consider storing timestamp of last scraping to draw better graph -> now stored in "lastUpdated" - 2/21/2021
#		[ ] Consider making individual db files for each class eg CMSC351
#[ ] Write function to calculate total seats, waitlist, etc. from obj
#[ ] Learn how to draw a line chart with the collected data
#[ ] Learn how to ?make a server? run this script periodically
#[ ] Use regular expressions to edit URL and scrape more pages
#[ ] Scrape the page w links to diff majors to get all classes at once

#returns List of 
from src.sectionList import sectionListFromUrl, shelveSections, printShelve


URL = "https://app.testudo.umd.edu/soc/202101/CMSC/CMSC351"

sectionList = sectionListFromUrl(URL)
print(sectionList)

shelveSections("data/sectionSnapshots", sectionList)
printShelve("data/sectionSnapshots")

print("done")