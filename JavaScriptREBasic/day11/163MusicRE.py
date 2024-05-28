# 从网易云音乐歌曲详情页下载歌曲
# 歌曲详情页https://music.163.com/#/song?id=64988=>Network=>v1?csrf_token= =>Preview=>url 歌曲下载地址
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import requests


# url = '/api/song/enhance/player/url/v1'


# 在Initiator中选择最后一个调用的js文件，在"i.apply(this, arguments)"添加断点后点击播放,在Scope中发现arguments中params已经被加密了
# 一层一层向上挨个检查每个js中的params的加密情况
# 在b9i.bkh8z中设置断点，会发现params被加密，并且还有另外两个参数。X9O是请求的url,d9g是headers和request,i9b是加密后的params
# 在断点所在函数声明处的下一行添加断点，会发现params被加密
# 在t9k.be9V中的cxT6N(X9O, e9f)添加断点，会发现疑似加密内容encSecKey和encText，在断点所在函数t9k.be9V声明处的下一行添加断点，会发现没有加密内容
# 检查参数X9O和e9f,X9O是个url（weblog），e9f是logs
# 所以断定t9k.be9V是加密函数
# 多次释放断点后，X9O的内容变为"/api/song/enhance/player/url/v1"，与network中的url基本一致，
# e9f的内容变为query: {ids: '[64988]', level: 'standard', encodeType: 'aac'}, id值与当前页面url中song?id=的值一致
# 所以，query应为加密前的参数
# data = {
#     "ids": [64988],
#     "level": 'standard',
#     "encodeType": 'aac',
#     "csrf_token": ""
# }
# 点击t9k.be9V的call stack的上一层函数b9i.bzu0x，第一个参数是url，第二个参数类似$.ajax。从而确定query为加密前的参数

# url = url.replace('api', 'weapi')
# 替换后的url与抓包中获取的url相同

# 把data转换成字符串
# r = json.dumps(data)
# print(r)


# {"ids": [64988], "level": "standard", "encodeType": "aac", "csrf_token": ""}

# 怀疑asrsea是加密函数，找到它的位置，可以发现它使用了AES CBC加密

# 参考修改后的bVi3x.js编写加密函数
def b(data, key):
    key = key.encode("utf-8")
    data = data.encode("utf-8")
    data = pad(data, 16)
    aes = AES.new(key=key, iv=b"0102030405060708", mode=AES.MODE_CBC)
    bs = aes.encrypt(data)
    return base64.b64encode(bs).decode()


def c(i, e, f):
    return 'e05a268242d0b50fbac6d20041bfab53e0e163f18a4ffc9805aece65bf37adc046ef70e1e8a44de3cfd780a9204c60bc289a864fd2e1dc4c22d91a948f9f9abf15ecdd6151ec5feed1624381a7c27f49a2945dcd1d321f5507d8a6477ed83f75584c802c3e638412d26a4db4203a05c332f56d30e8a33856c3ebf927b31af933'


def asrsea(data, e, f, g):
    i = 'N7BrTCq7VltLi9ez'
    first = b(data, g)
    second = b(first, i)
    encSecKey = c(i, e, f)
    return second, encSecKey


def main():
    # input("请输入想要下载的网易云音乐歌曲链接：")
    data = {
        "ids": [64988],
        # "ids": [64988, 64288],
        "level": 'standard',
        "encodeType": 'aac',
        "csrf_token": ""
    }
    url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
    data = json.dumps(data)
    encText, encSecKey = asrsea(data, '010001',
                                '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7',
                                '0CoJUm6Qyw8W8jud')

    dic = {
        "params": encText,
        "encSecKey": encSecKey,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    }

    resp = requests.post(url, data=dic, headers=headers)
    # print(resp.text)
    # 含有"url":xxx.m4a说明逆向成功
    resp_dict = resp.json()
    resp_list = resp_dict['data']
    for item in resp_list:
        # print(item.get('url'))
        song_url = item.get('url')
        song_id = item.get('id')
        print(song_id, song_url)
        with open(f"{song_id}.m4a", 'wb') as f:
            song_resp = requests.get(song_url, headers=headers)
            f.write(song_resp.content)


if __name__ == '__main__':
    main()
