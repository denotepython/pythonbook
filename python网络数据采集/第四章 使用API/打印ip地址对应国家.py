import json
from urllib2 import urlopen

'''无效
def getCountry(ip):
	response = urlopen("http://freegeoip.net/json/" + ip).read().decode('utf-8')
	response_json = json.loads(response)
	return response_json.get("country_code")

print getCountry("50.78.253.58")
'''
