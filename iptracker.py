import requests
import json

# IP address to test
ip_address = input("Target Ip Adress: ")

# URL to send the request to
request_url = 'https://extreme-ip-lookup.com/json/{}?key=j7tBzUISRphyQOtHdsnh'.format(ip_address)
# Send request and decode the result
response = requests.get(request_url)

result = response.content.decode()

print(response)

print(result)
# Clean the returned string so it just contains the dictionary data for the IP address
