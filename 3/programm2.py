import urllib.request
import concurrent.futures
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

# Используем ThreadPoolExecutor для запуска функции urlstatus в нескольких потоках
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(urlstatus, urls)

# Выводим результаты
for url, status in zip(urls, results):
    print(url, status)

print(time.time() - start)
