import requests
import os
import webbrowser as web
url = "https://www.faysalf.me/about.html"
response = requests.get(url)
webpage = response.text
with open("webpagesave.html","w", encoding=response.encoding) as f:
    f.write(webpage)
file_path = os.path.realpath("webpagesave.html")
print(file_path)
web.open("file://"+file_path)
