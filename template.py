import markdown
from bs4 import BeautifulSoup

# html = markdown.markdown(open('apis.md').read(), extensions=['attr_list'])
# soup = BeautifulSoup(html, 'html.parser')


def testsoup(content):
	"""
	Create a file named blog.html for viewing HTML output
	"""
	test = open('blog.html', 'w')
	test.write(content)
	test.close()


def getcontent(tag, csoup):
	""" 
	Get Content based on tag
	"""
	allp = csoup.findAll('p')
	tags = ''
	for item in allp:
		if(tag in item.string):
			tags = item.string
	return (tags.split(':')[1]).split(',')


def getmain(csoup):
	"""
	Get main content from text without Identifying tags	
	"""
	x = list(csoup)
	l = []
	for i in x:
		if(i != '\n'):
			l.append(str(i))
	return ' '.join(l[3:])

def moveinside(tag,contents, csoup):
	"""
	Move contents into the specified tag
	"""
	newtag = csoup.new_tag(tag) 
	newtag['class'] = 'tags'
	for tag in contents:
		newtag.append(BeautifulSoup('<p> {} </p>'.format(tag), "html.parser"))
	print(newtag.prettify())

def heading(csoup):
	return csoup.findAll('h1')[0]

# moveinside('div', getcontent('Tags', soup), soup) # Move contents inside a tag

# getcontent('Tags', soup) # Get content based on Tag

# getmain(soup) # Get main text content