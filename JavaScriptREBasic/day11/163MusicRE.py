# 歌曲详情页https://music.163.com/#/song?id=64988=>Network=>v1?csrf_token= =>Preview=>url 歌曲下载地址
import json

url = '/api/song/enhance/player/url/v1'
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
data = {
    "ids": [64988],
    "level": 'standard',
    "encodeType": 'aac',
    "csrf_token": ""
}
# 点击t9k.be9V的call stack的上一层函数b9i.bzu0x，第一个参数是url，第二个参数类似$.ajax。从而确定query为加密前的参数

url = url.replace('api', 'weapi')
# 替换后的url与抓包中获取的url相同

# 把data转换成字符串
r = json.dumps(data)
print(r)
# {"ids": [64988], "level": "standard", "encodeType": "aac", "csrf_token": ""}

# 怀疑asrsea是加密函数，找到它的位置，可以发现它使用了AES CBC加密

