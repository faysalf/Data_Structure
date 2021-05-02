import requests
url = "https://www.faysalf.me/about.html"
response = requests.get(url)  #attribute dekhar jonno dir() func use korte hobe
print("Attribute 'ok':",response.ok)    #ok diye website url thik thakle True asbe, or false asbe
print("Attribute 'status_code':", response.status_code)
print("Attribute 'reason':",response.reason) #response.reason==ok and .status_code==200 hole website right
print("Attribute 'json':", response.json)
print("Attribute 'links':", response.links)
print("Attribute 'raw':", response.raw)
print("Attribute 'text':", response.text)
print("Attribute 'url':", response.url)
print("Attribute 'close':", response.close)
print("Attribute '__bool__':", response.__bool__)
print("Attribute '__dir__':", response.__dir__)
