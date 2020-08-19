import os, shutil
from jinja2 import Environment, FileSystemLoader
import markdown
from bs4 import BeautifulSoup
from template import getcontent, getmain, moveinside, heading

def mark(markdownfile, templatefile="templates/template.j2"):
	current_directory = os.path.dirname(os.path.abspath(__file__))
	env = Environment(loader=FileSystemLoader(current_directory))

	html = markdown.markdown(open(markdownfile).read(), extensions=['attr_list'])
	soup = BeautifulSoup(html, 'html.parser')

	# https://stackoverflow.com/questions/47116572/generate-html-from-html-template-in-python
	s = env.get_template(templatefile).render(heading=heading(soup), tags=getcontent("Tags", soup), content=getmain(soup))


	test = open(markdownfile.split('.')[0]+".html",'w')
	test.write(s)
	# test.write(s.prettify())
	test.close()

mfiles = os.listdir('mdfiles')
hfiles = os.listdir('blogposts')
for file in mfiles:
	# mark('markdownfiles/{}'.format(file))
	# move file+.html using shutil
	if file.split('.')[0]+'.html' in hfiles:
		print("Re-rendering file: " + file)
	else:
		mark('mdfiles/{}'.format(file))
		shutil.move('mdfiles/{}.html'.format(file.split('.')[0]), 'blogposts')
		# print(file)

# print("Finished templating files")