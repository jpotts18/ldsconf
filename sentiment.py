import glob, csv
from afinn import sentiment

READ_FILE = 'data/talks/txt/1971-04/life-is-eternal'

files = glob.glob('data/talks/txt/*/*')
# files = glob.glob('data/talks/txt/1971-04/*')

observations = []
headers = ['conference','talk','score']
observations.append(headers)

for f in files:
	text = open(f, 'r').read()
	sent_score = sentiment(text)
	ob = [
		f.split('/')[-2],
		f.split('/')[-1],
		sent_score
	]
	observations.append(ob)

with open('sentiment.csv','w') as fp:
	a = csv.writer(fp, delimiter=',')
	a.writerows(observations)