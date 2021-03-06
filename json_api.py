import requests	
import json

def getJsonData():
	url = "http://www.recipepuppy.com/api/"	
	ResponseData = requests.get(url) 
	data = json.loads(ResponseData.content.decode('utf-8'))
	return data

def printJsonData(num):
	data = getJsonData()
	print "\t{}".format(data['results'][num]['ingredients'])
		
def selectAnyOption():
	data = getJsonData()
	n = 5
	a = data["results"]
	for idd, results in enumerate(a[:n]):
		print "\t\t {} {}".format(idd,results["title"])
	c = int(input("\n\t\tDo you want more?\t1 or 0\n\t\t\t"))
	if c == 1:
		for idd, results in enumerate(data["results"]):
			print "\n\t\t {} {}".format(idd,results["title"])
		option = int(input("\tEnter any option to know the ingredients\n\t\t\t"))
		printJsonData(option)
	else:
		option = int(input("\n\tEnter any option to know the ingredients\n\t\t\t"))
		if option > n-1:
			print "\n\t\t\tERROR"
		else:
			printJsonData(option)
			
def main():
	print "\t\t\tHELLO\n"
	print "\t\tWelcome to Recipe Puppy\n"
	selectAnyOption()

if __name__ == '__main__':
	main()
