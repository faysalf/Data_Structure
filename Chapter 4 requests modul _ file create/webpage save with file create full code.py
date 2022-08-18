import requests
url = "https://pythoncode.cf"
response = requests.get(url)
with open("webpage.html", "w", encoding=response.encoding) as f: #code error dekhale encoding=response.encoding use kora lage
    f.write(response.text)
