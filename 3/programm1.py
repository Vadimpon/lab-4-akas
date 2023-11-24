import urllib.request
import time
urls = [
    'https://www.pnzgu.ru/',
    'https://moodle.pnzgu.ru/my/',
    'https://lk.pnzgu.ru/portfolio/my',
    ]
def urlstatus(url):
    with urllib.request.urlopen(url) as u:
        return u.getcode()
start = time.time()
for url in urls:
    urlstatus(url)
    print(url,urlstatus(url))
print(time.time() - start)
