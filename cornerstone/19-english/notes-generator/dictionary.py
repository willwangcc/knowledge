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

	url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

	code = r.status_code
	# print(code, type(code))
	definitions = "Not Found"
	if code == 200:
		# print("text \n" + r.text)
		word_json = json.dumps(r.json())
		# print(type(word_json))
		word_json2 = json.loads(word_json)
		# print(type(word_json2))
		# print(word_json2)

		# print("json \n" + json.dumps(r.json()))
		senses = word_json2["results"][0]["lexicalEntries"][0]["entries"][0]["senses"]
		for sense in senses:
			if "short_definitions" in sense:
				definitions = sense["short_definitions"][0]
				break				
			if "definitions" in sense:
				definitions = sense["definitions"][0]
				break
	return definitions
	
# test: ["fella", "victoria"]
word_id = "victoria"
print(define(word_id))
