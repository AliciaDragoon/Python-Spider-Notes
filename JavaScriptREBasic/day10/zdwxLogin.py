data = {
    "imageCaptchaCode": "aaaa",
    "password": "P9grE4r7HUhLYMLiHTrVe+PU0YWndexEaiRPst+aMTI2n+ZGg9D9RcmpW6Ne8A9IxnLrzj5UHMa4vLohSmhxs4AbCgbgyzyALqLxM2KQn2zrLIJ3y/lqhduJOQsyf1zvX3vO+dKMGkYmwDAunN4ZgRset4NgON14GNXa/SE9eMw=",
    "userName": "18053465528"
}
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

