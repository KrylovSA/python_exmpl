import requests

token_endpoint = 'https://icdaccessmanagement.who.int/connect/token'
client_id = 'xxx'
client_secret = 'xxxx'
scope = 'icdapi_access'
grant_type = 'client_credentials'


payload = {'client_id': client_id, 
	   	   'client_secret': client_secret, 
           'scope': scope, 
           'grant_type': grant_type}
           

r = requests.post(token_endpoint, data=payload, verify=False).json()
token = r['access_token']


uri = 'https://id.who.int/icd/entity'


headers = {'Authorization':  'Bearer '+token, 
           'Accept': 'application/json', 
           'Accept-Language': 'en',
	   'API-Version': 'v2'}
           

r = requests.get(uri, headers=headers, verify=False)

print (r.text)			