from bs4 import BeautifulSoup as bs
import glob

read_dir = 'data/conferences/html/*'
write_dir = 'data/conferences/txt/'

files = glob.glob(read_dir)

for f in files:
	file_name = f.split('/')[-1]
	html = open(f, 'r').read()
	soup = bs(html)
	links = [pl['href'] for pl in soup.select('td.print a')]
	text = '\n'.join(links)
	text_file = open(write_dir + file_name, 'w')
	text_file.write(text)
	text_file.close()