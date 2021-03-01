
from src.sectionList import sectionListFromUrl, shelveSections, printShelve

URL = "https://app.testudo.umd.edu/soc/202101/CMSC/CMSC351"

sectionList = sectionListFromUrl(URL)
print(sectionList)

shelveSections("data/sectionSnapshots", sectionList)
printShelve("data/sectionSnapshots")

print("done")