import requests
from bs4 import BeautifulSoup

url = 'https://www.simplilearn.com/tutorials/cyber-security-tutorial/cyber-security-jobs'

html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

results = s.find(id='articleLongDescription')
job_title = results.find_all('h3')

for job in job_title:
	print(job.text)

 
