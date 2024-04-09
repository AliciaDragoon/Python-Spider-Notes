import requests
from lxml import etree
import pymongo

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36 Edg/122.0.0.0"
}


# 获取页面源代码
def get_page_source(url):
    resp = requests.get("https://cm.lianjia.com/ershoufang/", headers=headers)
    return resp.text


# 解析页面源代码，获取房源数据
def parse_data(pagesource):
    tree = etree.HTML(pagesource)
    li_list = tree.xpath("//*[@class='sellListContent']/li")
    # print(len(li_list))
    # 31, 30条房源数据，一条引流信息
    result = []
    for li in li_list:
        title = li.xpath(".//*[@class='title']/a/text()")
        # print(title)
        # 去除空白数据
        if not title:
            continue
        # print(title)
        title = title[0]
        # 从列表提取字符串
        position = li.xpath(".//*[@class='positionInfo']//text()")
        # print(position)
        position = "".join(position).strip().replace(" ", "")
        # print(position)
        house_info = li.xpath(".//*[@class='houseInfo']//text()")
        # print(house_info)
        house_info = house_info[0].replace(" ", "").split("|")
        # print(house_info)
        total_price = li.xpath(".//*[@class='priceInfo']/div[1]//text()")
        total_price = "".join(total_price)
        unit_price = li.xpath(".//*[@class='priceInfo']/div[2]//text()")
        unit_price = unit_price[0]
        # print(total_price, unit_price)
        dic = {
            "title": title,
            "position": position,
            "house_info": house_info,
            "total_price": total_price,
            "unit_price": unit_price,
        }
        result.append(dic)
    return result


# 存入mongodb
def sava_data(data):
    conn = pymongo.MongoClient(
        host="localhost",
        port=27017
    )
    db = conn['lianjia_ershoufang']
    db.chengmai.insert_many(data)
    conn.close()


def main():
    url = "https://cm.lianjia.com/ershoufang/"
    page_source = get_page_source(url)
    data = parse_data(page_source)
    # print(data)
    sava_data(data)


if __name__ == "__main__":
    main()
