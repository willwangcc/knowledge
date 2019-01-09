# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# TODO: replace with your own app_id and app_key

def define(word_id):
	"""
	word: str
	r: define: str 
	"""
	app_id = 'beed99a1'
	app_key = '33f531ce2353d5f73bedb9ee0f6175c6'

	language = 'en'
	word_id = 'ineffable'

	url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

	# print("code {}\n".format(r.status_code))
	# print("text \n" + r.text)
	word_json = json.dumps(r.json())
	# print(type(word_json))
	word_json2 = json.loads(word_json)
	# print(type(word_json2))

	# print("json \n" + json.dumps(r.json()))
	senses = word_json2["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]

	short_definitions = senses[0]["short_definitions"][0]
	return short_definitions
	
print(define('ineffable'))