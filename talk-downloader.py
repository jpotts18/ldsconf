import urllib2, csv, glob, os

READ_FOLDER = 'data/conferences/txt/*'
WRITE_FOLDER = 'data/talks/html/'
files = glob.glob(READ_FOLDER)

for f in reversed(files):
	folder_name = f.split('/')[-1].split('.')[0]
	print 'Folder Name --> ' + folder_name
	lines = open(f).read().splitlines()
	for l in lines:
		file_name = l.split('/')[-1].split('?')[0]
		if os.path.exists(WRITE_FOLDER + folder_name + '/' + file_name):
			print 'File found -->' + WRITE_FOLDER + folder_name + '/' + file_name
		else: 
			try:
				req = urllib2.Request(l)
				resp = urllib2.urlopen(req)
				print 'Download    --> ' + l
				html = resp.read()
				if not os.path.exists(WRITE_FOLDER + folder_name):
					os.makedirs(WRITE_FOLDER + folder_name)
				f = open(WRITE_FOLDER + folder_name + '/' + file_name, 'w')
				f.write(html)
				f.close()
				print 'Write File  --> ' + WRITE_FOLDER + folder_name + '/' + file_name
			except urllib2.HTTPError, e:
				print '404 ' + file_name