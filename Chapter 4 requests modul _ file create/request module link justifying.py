#wrong url
import requests
url = "https://www.faysalf.me/about"
res = requests.get(url)
print("Attribute 'ok':",res.ok) #shudhu ok diyee jachai kora jay jodi onno attributegulo mone na thake, ok=True
print("Attribute 'status_code':", res.status_code) #status_code==200 and reason==ok hole right
print("Attribute 'reason':",res.reason)
