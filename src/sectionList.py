import requests
import re
from time import ctime
import time
import shelve

def sectionListFromUrl(url):
	start_time = time.time()

	# get the page
	response = requests.get(url)
	html = response.text

	# format time to 3 decimal places then print
	load_time = "{:.3f}".format(time.time() - start_time)
	print("--- %s seconds to get page ---" % load_time)
	start_time = time.time() # reset timer

	#parse page
		#sample section of interest:
		#<span class="total-seats-count">270</span>
		#<span class="waitlist-count">0</span>
		#https://regexr.com/5mnn2 to test regEx, has test cases
	pattern = re.compile(r'<span class="(.+)-count">(\d+)<\/span>')
	matches = pattern.finditer(html)
	match_count = 0

	# will be storing a list of dicts, each dict representing a
	#	section and containing key value pairs of data 
	section_list = list()
	cur_section = {}
	for match in matches:

		if match_count > 0 and match.group(1) == 'total-seats':
			#add cur_section to section_list then start new section
			section_list.append(cur_section)
			cur_section = {match.group(1): int(match.group(2))}
		else:
			#add the line of data to cur_section
			cur_section[match.group(1)] = int(match.group(2))

		match_count += 1
		#print(match.group(1), match.group(2))
	section_list.append(cur_section)

	# count number of sections
	num_sections = html.count("\"seats-info\"")
	print('Number of sections:', num_sections)

	# format time to 3 decimal places then print
	parse_time = "{:.3f}".format(time.time() - start_time)	
	print("--- %s seconds to run regex ---" % (parse_time))
	print("")
	return section_list

#adds sections to sectionLists in db file at filePath only if
#sectionListEquals() determines them to be different
def shelveSections(filePath, sections):
	curTime = time.time()
	#time.time() is a float, but what is time.time?

	d = shelve.open(filePath) #"data/sectionSnapshots"

	if "lastAdded" not in d:
		print("First sectionList added to shelve")
		d[str(curTime)] = sections
		d["lastAdded"] = str(curTime)
	else:
		#check if lastAdded is same as new sectionList
		if sectionListsEqual(d[d["lastAdded"]], sections):
			print("Same as last, not adding\n")
		else:
			print("Differrent, adding to shelve\n")
			d[str(curTime)] = sections
			d["lastAdded"] = str(curTime)

	d["lastUpdated"] = curTime

	d.close()

#prints key value pairs in db for debugging
def printShelve(filePath):
	print("Sections stored in", filePath, ":\n")
	d = shelve.open(filePath)
	count = 0
	for key in list(d.keys()):
		count += 1
		if key != "lastAdded" and key != "lastUpdated":
			print(ctime(float(key)))
			print(d[key], "\n")
	print("Printed", count-2, "sectionLists")

	print("Last updated at", ctime(d["lastUpdated"]))
	d.close()

#compares all fields of sl's and returns true if all are equal
def sectionListsEqual(sl1, sl2):
	sectionNumber = 0
	#iterate sections
	for dict in sl1:
		#iterate key value pairs
		for key in dict.keys():
			val1 = dict[key]
			try: #error if different # of sections or attributes
				section = sl2[sectionNumber]
				val2 = section[key]
				if val1 != val2:
					#print("Value mismatch, adding sectionList")
					return False
			except:
				#print("Exception occured, adding sectionList. Make sure this is intentional!")
				return False
		sectionNumber += 1
	#print("sectionLists match, not adding")
	return True