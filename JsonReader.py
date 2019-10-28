import json

# some JSON:
with open('/home/khaledawad/PdfCreator/data.json') as f:
    data = json.load(f)

# parse x:


for i in range(len(data)):
    print(data[i])
    print("============")