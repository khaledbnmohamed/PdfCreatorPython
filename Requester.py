import requests
import json

url = 'http://localhost:8888/v1/createPDF'
headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}
contents = open('/home/khaledawad/PdfCreator/data.json', 'rb').read()
r = requests.post(url, data=contents, headers=headers)