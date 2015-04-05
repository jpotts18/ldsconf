import multiprocessing, string, csv, os

from nltk.corpus import stopwords

from simplemapreduce import SimpleMapReduce

WORD_DIR = 'data/words/csv/'

SEARCHED_WORD = 'twitter'.lower()

def file_to_words(filename):
    """Read a file and return a sequence of (word, occurances) values.
    """
    year = filename.split('/')[-2].split('-')[0]

    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))

    # print multiprocessing.current_process().name, 'reading', filename
    output = []
    with open(filename, 'rt') as f:
        for line in f:
            line = line.translate(TR) # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word == SEARCHED_WORD:
                    print "FOUND", multiprocessing.current_process().name, filename
                    output.append( (year, 1) ) 
    return output


def count_words(item):
    """Convert the partitioned data for a word to a
    tuple containing the word and the number of occurances.
    """
    year, occurances = item
    return (year, sum(occurances))


if __name__ == '__main__':
    import operator
    import glob

    input_files = glob.glob('data/talks/txt/*/*')
    
    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(0))

    print 'Occurrences of', SEARCHED_WORD, 'By Years'

    if not os.path.exists(WORD_DIR):
        os.makedirs(WORD_DIR)

    with open(WORD_DIR + SEARCHED_WORD + '.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerow(('Year', 'Count'))
        a.writerows(word_counts)

