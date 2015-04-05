import urllib2, csv

WRITE_FOLDER = 'data/conferences/html/'

lines = open('links.txt').read().splitlines()

for l in lines:
	print 'Downloading --> ' + l
	path_components = l.split('/')
	file_name = WRITE_FOLDER + path_components[-2] + '-' + path_components[-1].split('?')[0] + '.html'
	try:
		req = urllib2.Request(l)
		resp = urllib2.urlopen(req)
		html = resp.read()
		f = open(file_name, 'w')
		f.write(html)
		f.close()
	except urllib2.HTTPError, e:
		print '404 ' + file_name
