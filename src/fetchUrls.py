# To Do: write a script to scrape https://app.testudo.umd.edu/soc/
# for class name/number to be used to scrape section data
# sample course name: <div id="AASP100H" class="course">
# maybe use regEx /<div id="*+" class="course"/
# semester id for Fall 2021 is "202108"
# semester id for Spring 2021 is "202101"
import requests
import re

url = "https://app.testudo.umd.edu/soc/202108/CMSC"

response = requests.get(url)
html = response.text

pattern = re.compile(r'<div id="(.{7})" class="course">')
matches = pattern.finditer(html)


for match in matches:
	print(match.group(1))