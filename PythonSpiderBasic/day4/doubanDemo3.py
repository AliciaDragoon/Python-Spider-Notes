import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}

with open('豆瓣排行榜100.txt',"w")as f:
    for i in range(5):
        url = f"https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={i * 20}&limit=20"
        resp = requests.get(url, headers=headers)
        lst = resp.json()
        for item in lst:
            # print(f"名字: {item['title']}, 分数: {item['score']}, 封面图链接: {item['cover_url']}")
            f.write(f"名字: {item['title']}, 分数: {item['score']}, 封面图链接: {item['cover_url']}\n")