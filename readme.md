# ldsconf

You may need to create a data folder with the following structure

```bash
data
├── conferences
│   ├── html
│   └── txt
├── talks
│   ├── html
│   └── txt
└── words
    └── csv
```

## Download Conference Home Pages

```bash
# downloads into data/conferences/html/{Year}-{Month}
$ python conference-downloader.py
```
## Parse Conference Pages to extract Talk

```bash
# extracts links into data/conferences/txt/{Year}-{Month}
$ python conference-parser.py
```

## Download Talks

```bash
# downloads into data/talks/html/{Year}-{Month}/{file_name}
$ python talk-downloader.py
```

## Parse Talks

```bash
# extracts into data/talks/txt/{Year}-{Month}/{file_name}
$ python talk-parser.py
# writes
```

## Run AFINN word polarity on every talk

```bash
$ python sentiment.py
# outputs sentiment.csv
```



