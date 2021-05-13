import requests 
from bs4 import BeautifulSoup

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

def search_google(q,pages):
    s = requests.Session()
    q = '+'.join(q.split()) 
    result_search = ''
    for page in range(0,(pages*10),10):
        url = f'https://www.google.com/search?q={q}&ie=utf-8&oe=utf-8&start={page}'
        r = s.get(url, headers=headers_Get)
        soup = BeautifulSoup(r.text, "html.parser")
        data = soup.find_all('div',class_='g')
        for i in data:
            try:
                result_search += i.find_all('span')[0].text +'\n'
                result_search += i.find_all('span')[-1].text
            except:
                pass
            result_search +='\n\n'
    return result_search

def search_bing(q : str,pages=1):
    result = ''
    headers_Get = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        'content-type':  "*/*",
        "accept-language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7",}
    pages *= 10
    q= q.strip()
    q = q.replace('  ',' ').replace(' ','+')
    for page in range(0,pages,10):
        page +=1
        query = f'https://www.bing.com/search?q={q}&pq=test+search&first={page}'
        request = requests.get(query,headers=headers_Get)
        soup = BeautifulSoup(request.text,'html.parser')
        result_ol = soup.find('ol',id='b_results')
        li = result_ol.find_all('li')
        for i in li:
            try:
                data =  i.find_all('span')
                title = data[0].text
                caption = data[-1].text
                result += f'{title}\n{caption}\n\n'
            except :
                pass
    return result


