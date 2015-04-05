import multiprocessing, string, os, csv, glob, operator
from nltk.corpus import stopwords

from simplemapreduce import SimpleMapReduce

STOP_WORDS = stopwords.words('english')

def file_to_words(filename):
    """Read a file and return a sequence of (word, occurances) values.
    """
    TR = string.maketrans(string.punctuation, ' ' * len(string.punctuation))

    print multiprocessing.current_process().name, 'reading', filename
    output = []

    with open(filename, 'rt') as f:
        for line in f:
            line = line.translate(TR) # Strip punctuation
            for word in line.split():
                word = word.lower()
                if word.isalpha() and word not in STOP_WORDS:
                    output.append( (word, 1) )
    return output


def count_words(item):
    """Convert the partitioned data for a word to a
    tuple containing the word and the number of occurances.
    """
    word, occurances = item
    return (word, sum(occurances))


if __name__ == '__main__':

    NUM_WORDS = 50
    TOP_WORDS_DIR = 'data/words/'
    input_files = glob.glob('data/talks/txt/*/*')
    
    mapper = SimpleMapReduce(file_to_words, count_words)
    word_counts = mapper(input_files)
    word_counts.sort(key=operator.itemgetter(1))
    word_counts.reverse()
    
    top_words = word_counts[:NUM_WORDS]

    if not os.path.exists(TOP_WORDS_DIR):
        os.makedirs(TOP_WORDS_DIR)

    with open(TOP_WORDS_DIR + 'top-' + str(NUM_WORDS) + '-words.csv', 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerow(('Word', 'Count'))
        a.writerows(top_words)
