# data = {
#     "imageCaptchaCode": "aaaa",
#     "password": "P9grE4r7HUhLYMLiHTrVe+PU0YWndexEaiRPst+aMTI2n+ZGg9D9RcmpW6Ne8A9IxnLrzj5UHMa4vLohSmhxs4AbCgbgyzyALqLxM2KQn2zrLIJ3y/lqhduJOQsyf1zvX3vO+dKMGkYmwDAunN4ZgRset4NgON14GNXa/SE9eMw=",
#     "userName": "18053465528"
# }
# 只有password被加密了

# 找到password的方案
# 搜索参数
# 根据url从后向前依次搜索
# 在Initiator一层一层搜索（此处采用该方案）

# 参数整体都被加密时，加密有可能会在jQuery.js之后；只有password被加密，加密有可能会在jQuery.js之前
# 检查window.zdAjax
# 发现window.zdAjax = function(e, o, n){}函数，对该函数进行分析,
# 在$.ajax()设置断点，注意检查e.url是否为加密函数所在的url，不是的话按F8释放断点检查下一个url
# 在控制台检查i的值，发现数据已经被加密了
# 在e = Object.assign()设置断点
# 在控制台检查e的值，发现数据已经被加密了，如果发现数据已经被加密了，说明加密位置在当前函数的外层
# 通过call stack查找上一层函数，发现是zdAjax(param, (res)=> {})函数所调用
# 检查param的值，发现数据已经被加密了
# 向上搜索param，发现param()是加密password的函数
# 找到加密函数encryptFn()的位置，获取公钥

# 在依次访问多个url，在最后一个url才能获取到数据的情况下，需要保持cookies
# session只能处理response头的cookies，js处理的cookies需要手工处理
# 使用session.get(登录页面)加载第一个cookies
import requests
import base64
import json
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

session = requests.session()
session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
}
login_page_url = "https://user.wangxiao.cn/login?url=https%3A%2F%2Fwww.wangxiao.cn%2F"
session.get(login_page_url)
# print(session.cookies)
# <RequestsCookieJar[<Cookie sessionId=1716630623580 for user.wangxiao.cn/>]>

# 获取验证码
v_code_url = "https://user.wangxiao.cn/apis//common/getImageCaptcha"
# v_code_resp = session.post(v_code_url)
# print(v_code_resp.text)
# 返回的是HTML

# 给获取验证码这次请求单独添加Referer
# v_code_resp = session.post(v_code_url, headers={
#     "Referer": "https://user.wangxiao.cn/login?url=https%3A%2F%2Fwww.wangxiao.cn%2F"
# })
# print(v_code_resp.text)
# 返回的是HTML

# 给获取验证码这次请求单独添加Content-Type
v_code_resp = session.post(v_code_url, headers={
    "Content-Type": "application/json;charset=UTF-8"
})
# print(v_code_resp.text)
# 返回的是JSON。挨个尝试添加headers参数，直到获取json
# print(v_code_resp.json())

# 提取图片
img_base64_data = v_code_resp.json()['data'].split(",")[1]


# print(img_base64_data)
# 把验证码图片保存到本地
# with open("img_base64.jpg", "wb") as f:
#     f.write(base64.b64decode(img_base64_data))

# 使用图鉴识别验证码
def base64_api(img):
    data = {"username": "q6035945", "password": "q6035945", "typeid": 3, "image": img}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


v_code = base64_api(img_base64_data)
# print(v_code)

# 加密密码
password = "q6035945"
get_time_url = "https://user.wangxiao.cn/apis//common/getTime"
get_time_resp = session.post(get_time_url, headers={"Content-Type": "application/json;charset=UTF-8"})
time_data = get_time_resp.json()['data']
cipher_password_str = password + time_data
public_key_str = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB"
public_key_bytes = base64.b64decode(public_key_str)
public_key = RSA.importKey(public_key_bytes)
cipher = PKCS1_v1_5.new(public_key)
ciphertext = cipher.encrypt(cipher_password_str.encode('utf-8'))
cipher_password = base64.b64encode(ciphertext).decode()

login_data = {
    "imageCaptchaCode": v_code,
    "password": cipher_password,
    "userName": "18614075987",
}

login_url = "https://user.wangxiao.cn/apis//login/passwordLogin"
login_resp = session.post(login_url, data=json.dumps(login_data),
                          headers={"Content-Type": "application/json;charset=UTF-8"})
print(login_resp.json())
# 登录成功
login_info = login_resp.json()

# listQuestions_url = "http://ks.wangxiao.cn/practice/listQuestions"
# listQuestions_data = {
#     "examPointType": "",
#     "practiceType": "2",
#     "questionType": "",
#     "sign": "jz1",
#     "subsign": "8cc80ffb9a4a5c114953",
#     "top": "30",
# }
# listQuestions_resp = session.post(listQuestions_url, data=json.dumps(listQuestions_data),
#                                   headers={"Content-Type": "application/json;charset=UTF-8"})
# print(listQuestions_resp.text)
# # 登录失败,session未能保持cookies

# 将zdAjax(param, (res))中自动登录的参数加载到session中
session.cookies['autoLogin'] = "true"
session.cookies['userInfo'] = json.dumps(login_info['data'])
session.cookies['token'] = login_info['data']['token']
"""
# e即login_info['data']
$.cookie("UserCookieName", e.userName, n),
$.cookie("OldUsername2", e.userNameCookies, n),
$.cookie("OldUsername", e.userNameCookies, n),
$.cookie("OldPassword", e.passwordCookies, n),
$.cookie("UserCookieName_", e.userName, n),
$.cookie("OldUsername2_", e.userNameCookies, n),
$.cookie("OldUsername_", e.userNameCookies, n),
$.cookie("OldPassword_", e.passwordCookies, n),
$.cookie(e.userName + "_exam", e.sign, n))
"""
session.cookies['UserCookieName'] = login_info['data']['userName']
session.cookies['OldUsername2'] = login_info['data']['userNameCookies']
session.cookies['OldUsername'] = login_info['data']['userNameCookies']
session.cookies['OldPassword'] = login_info['data']['passwordCookies']
session.cookies['UserCookieName_'] = login_info['data']['userName']
session.cookies['OldUsername2_'] = login_info['data']['userNameCookies']
session.cookies['OldUsername_'] = login_info['data']['userNameCookies']
session.cookies['OldPassword_'] = login_info['data']['passwordCookies']
session.cookies[login_info['data']['userName'] + "_exam"] = login_info['data']['sign']

listQuestions_url = "http://ks.wangxiao.cn/practice/listQuestions"
listQuestions_data = {
    "examPointType": "",
    "practiceType": "2",
    "questionType": "",
    "sign": "jz1",
    "subsign": "8cc80ffb9a4a5c114953",
    "top": "30",
}
listQuestions_resp = session.post(listQuestions_url, data=json.dumps(listQuestions_data),
                                  headers={"Content-Type": "application/json;charset=UTF-8"})
print(listQuestions_resp.text)