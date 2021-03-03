
from src.sectionList import sectionListFromUrl, shelveSections, printShelve

endPointList = ["CMSC351", "CMSC216"]
debug = False

for endPoint in endPointList:

	URL = "https://app.testudo.umd.edu/soc/202101/"
	fullURL = URL + endPoint[0:4] + "/" + endPoint

	sectionList = sectionListFromUrl(fullURL, debug)
	#print(sectionList)

	shelveSections("data/" + endPoint[0:4] + "/" + endPoint, sectionList, debug)
	#printShelve("data/" + endPoint[0:4] + "/" + endPoint)

print("done")