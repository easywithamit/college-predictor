import urllib2
from bs4 import BeautifulSoup
def get_rank(url):
	html = urllib2.urlopen(url)
	print "cp1"
	soup = BeautifulSoup(html,'html.parser')
	print "cp2"
	branch_list = []
	my_content = soup.find('div',{'class':'entry-content'})
	for table in my_content.findAll('table'):
		table_content = table.find('tbody')
		for row in table_content.findAll('tr')[2:]:
			branch_list.append
			break
		# print table
		break
if __name__=='__main__':

	url = 'http://www.eduarena.com/nit-goa-jee-main-2015-cutoff/'
	url = 'http://www.eduarena.com/nit-mizoram-jee-main-2015-cutoff/'
	url = 'http://www.eduarena.com/nit-allahabad-jee-main-2015-cutoff/'

	get_rank(url)
