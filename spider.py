__author__ = 'Administrator'
import requests,re,json

def get_one_page(url):
    headers = {
        "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None
def parse_one_page(html):
    # url = "http://maoyan.com/board/4"
    # html = get_one_page(url)
    # print(html,type(html))
    # print("---------")
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?title="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i>.*?class="fraction">(.*?)</i>',re.S)
    items = re.findall(pattern,html)
    # print(items,type(items))
    for item in items:
        print (item,type(item))
        print (item[3].strip()[3:])
        print (item[4].strip()[5:])
        print(item[5].strip() + item[6].strip())
        yield {
            "index":item[0],
            "image":item[1],
            "title":item[2].strip(),
            "actor":item[3].strip()[3:],
            "time":item[4].strip()[5:],
            "score":item[5].strip() + item[6].strip()

        }

def write_to_file(content):
    with open('result.txt',"a",encoding="utf-8") as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+"\n")

def main():
    for i in range(10):
        offset = i *10
        url = "http://maoyan.com/board/4?offset=" + str(offset)
        html = get_one_page(url)
        for item in parse_one_page(html):
            print(item)
            write_to_file(item)



main()
