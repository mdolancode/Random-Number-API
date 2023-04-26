import requests 

# Can test endpoints by adding them to the end of the URL
request = requests.get("http://127.0.0.1:8000")
print(request.json())
