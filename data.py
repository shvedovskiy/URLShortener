import os

DATA_ENCODING = 'utf-8'
DATA_FILENAME = os.path.dirname(__file__) + '/urls.txt'


def _load_urls():
    with open(DATA_FILENAME, 'r', encoding=DATA_ENCODING) as data_file:
        return eval(data_file.read())


entries, next_url = _load_urls()


def _save_urls():
    with open(DATA_FILENAME, 'w', encoding=DATA_ENCODING) as data_file:
        print(repr((entries, next_url)), file=data_file)


def init_with_file(filename):
    global DATA_FILENAME, entries, next_url
    DATA_FILENAME = filename
    entries, next_url = _load_urls()


def add_url(old_url, new_url):
    global next_url
    if new_url in entries and entries[new_url] != old_url:
        return None
    if new_url == '' or new_url == str(next_url):
        new_url = str(next_url)
        next_url += 1
    entries[new_url] = old_url
    _save_urls()
    return new_url


def read_url(url_id):
    return entries[url_id]
