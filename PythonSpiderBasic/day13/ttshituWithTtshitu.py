import base64
import json
import requests


def base64_api(uname, pwd, img, typeid):
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": img}
    # 直接放入base64格式的img
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
# 一、图片文字类型(默认 3 数英混合)：
# 1 : 纯数字
# 1001：纯数字2
# 2 : 纯英文
# 1002：纯英文2
# 3 : 数英混合
# 1003：数英混合2
#  4 : 闪动GIF
# 7 : 无感学习(独家)
# 11 : 计算题
# 1005:  快速计算题
# 16 : 汉字
# 32 : 通用文字识别(证件、单据)
# 66:  问答题
# 49 :recaptcha图片识别
# 二、图片旋转角度类型：
# 29 :  旋转类型
#
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型
#
# 四、缺口识别
# 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
# 33 : 单缺口识别（返回X轴坐标 只需要1张图）
# 五、拼图识别
# 53：拼图识别

# 一般地，使用验证码时，要用cookies保持会话，防止验证码失败不成功

session = requests.session()
# 设置头信息
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
                  "Safari/537.36 Edg/122.0.0.0"
}

# 加载一个原始的cookies
session.get("http://www.ttshitu.com/login.html")

# 发送请求获取验证码
verify_url = "https://admin.ttshitu.com/captcha_v2?_=1710827189247"
# 域名里的"_","t","n"等常用于时间戳，防止浏览器缓存
resp = session.get(verify_url)
# 获取图片和图片id
img = resp.json()['img']
imgId = resp.json()['imgId']
# print(img, imgId)
# img是base64格式

username = "q6035945"
password = "q6035945"
# 识别验证码
verify_code = base64_api(username, password, img, 1)

# 登录
login_url = "https://admin.ttshitu.com/common/api/login/user"
# Request Payload
# 发出json
# 请求post
# 请求头里有contenttype:application/json
data = {
    "captcha": verify_code,
    "developerFlag": False,
    "imgId": imgId,
    "needCheck": True,
    "password": password,
    "userName": username,
}
# resp = session.post(login_url, data=json.dumps(data),headers={"Content-Type":"application/json; charset=UTF-8"})
resp = session.post(login_url, json=data)
# 给json参数，可以自动转化和处理
# print(resp.text)
