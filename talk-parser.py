from bs4 import BeautifulSoup as bs
import glob, os

read_dir = 'data/talks/html/*/*'
write_dir = 'data/talks/txt/'

files = glob.glob(read_dir)
for f in files:
	folder_name = f.split('/')[-2]
	file_name = f.split('/')[-1]
	html = open(f, 'r').read()
	soup = bs(html)
	ps = soup.find_all('p')
	paragraph_text = [p.get_text().encode('ascii','ignore') for p in ps]
	text = '\n\n'.join(paragraph_text)
	if not os.path.exists(write_dir + folder_name):
		os.makedirs(write_dir + folder_name)

	text_file = open(write_dir + folder_name + '/' + file_name, 'w')
	text_file.write(text)
	text_file.close()
	print 'Writing to  --> ' + folder_name + '/' + file_name