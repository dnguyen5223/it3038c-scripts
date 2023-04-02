import json
import requests

r = requests.get('http://localhost:3000/')

data = r.json()

for widget in data:
	color = widget['color']
	name = widget['name']

print('%s color %s \n' (name,color))
