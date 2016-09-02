import requests
from bs4 import BeautifulSoup
def get_rank(url):
	html = requests.get(url)
	t = html.text
	for table in t.findAll('table'):
		table_content = table.find('tbody')
		for row in table_content.findAll('tr'):
			print row
			break
		# print table
		break
if __name__=='__main__':
	url = 'http://www.eduarena.com/nit-goa-jee-main-2015-cutoff/'
	url = 'http://www.eduarena.com/nit-mizoram-jee-main-2015-cutoff/'
	get_rank(url)
