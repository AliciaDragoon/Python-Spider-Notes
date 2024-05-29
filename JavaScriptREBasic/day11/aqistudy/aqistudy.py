# 无限debugger
# 使用抓包工具来抓取页面源代码
url = "https://www.aqistudy.cn/html/city_realtime.php?v=2.3"

# 抓包js文件发现在jquery.min.js中有个疑似加密函数（// encrypt），在浏览器控制台中运行该函数，得到一个新的js代码
# 检查之后发现该函数作用是初始化加密信息，没有发现加密函数
# 检查（// respond）函数，没有发现加密函数
# 检查第一个（// debug detect）函数，发现它的作用是阻止你正常使用f12
# 检查第二个（// debug detect）函数，发现txsdefwsw()在index.html中调用过，发现它的作用是无限debugger