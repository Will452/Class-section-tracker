
from src.sectionList import sectionListFromUrl, shelveSections, printShelve

endPoint = "CMSC351"
URL = "https://app.testudo.umd.edu/soc/202101/"
fullURL = URL + endPoint[0:4] + "/" + endPoint

sectionList = sectionListFromUrl(fullURL)
print(sectionList)

shelveSections("data/" + endPoint, sectionList)
printShelve("data/" + endPoint)

print("done")