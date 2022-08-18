#save kora webpageti coding er moddhe run korte chaile
import os
import webbrowser as wb
file_path = os.path.realpath("webpage.html")    #file er obosthan ber korar jonno
print(file_path)
wb.open("file://"+file_path)

'''
#Shudhu ai code er maddhomeo ber korte pari. sekkhetre webpage.html name kono file na thakleo se create kore nibe
import requests
import os
import webbrowser as wb
url = "http://www.dimikcomputing.com"
response = requests.get(url)
with open("webpage.html", "w", encoding=response.encoding) as f:
    f.write(response.text)
file_path = os.path.realpath("webpage.html")
print(file_path)
wb.open("file://"+file_path)
'''
