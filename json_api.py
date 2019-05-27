import requests	
import json
import urllib

url = "http://www.recipepuppy.com/api/"

def hitJson(num):
	ResponseData = (requests.get(url)) 
	getUrlRequest = requests.get('http://api.zippopotam.us/us/ma/belmont')
	getJsonRequest = getUrlRequest.json()
	data = json.loads(ResponseData.content.decode('utf-8'))
	print data['results'][num]['ingredients']
		
def selectAnyOption():

	print "\t\t\tRecipe List\n\t\t\t"
	print "\t\t 1. Ginger Champagne\n"
	print "\t\t 2. Potato and Cheese Frittata\n"
	print "\t\t 3. Eggnog Thumbprints\n"
	print "\t\t 4. Succulent Pork Roast\n"
	print "\t\t 5. Irish Champ\n"
	option = int(input("\tEnter any option to know the ingredients\n\t\t\t"))
	
	if option > 5:
		print "\t\t\tBYE"
	else:
		hitJson(option)
	
def main():

	print "\t\t\tHELLO\n"
	print "\t\tWelcome to Recipe Puppy\n"
	selectAnyOption()

if __name__ == '__main__':

	main()