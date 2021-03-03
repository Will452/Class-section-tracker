# Class-section-tracker
Web scraping to later build a course availability tracker

## What's next


- [X] Get and parse data
  - [X] Measure how long this takes: <0.01s is fast enough -2/17/2021
- [X] Store responses in a data structure -2/17/2021
- [X] Convert into a function that takes url and returns obj -2/18/2021
- [X] Use persistant storage eg. file, or database -> shelve	-2/19/2021
  - [X] Only store new sectionList if it's different -2/21/2021
  - [X] Write function to check sectionList equality - 2/21/2021
  - [X] Consider storing timestamp of last scraping to draw better graph -> now stored in "lastUpdated" - 2/21/2021
  - [X] Consider making individual db files for each class eg CMSC351 - 2/23/2021
- [ ] Write function to calculate total seats, waitlist, etc. from obj
- [ ] Learn how to draw a line chart with the collected data
- [ ] Learn how to ?make a server? run this script periodically
- [ ] Use regular expressions to scrape a list? of all courses
- [ ] Add gitIgnore file to avoid storing data on GitHub
- [ ] Add multithreading on page requests to save time on many requests