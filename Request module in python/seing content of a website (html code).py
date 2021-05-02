import requests
url = "http://www.example.com"
res = requests.get(url)
print("Attrubute 'text':", res.text)
