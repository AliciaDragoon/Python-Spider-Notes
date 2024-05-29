# 无限debugger
# 使用抓包工具来抓取页面源代码
url = "https://www.aqistudy.cn/html/city_realtime.php?v=2.3"

# 抓包js文件发现在jquery.min.js中有个疑似加密函数（// encrypt），在浏览器控制台中运行该函数，得到一个新的js代码
# 检查之后发现该函数作用是初始化加密信息，没有发现加密函数
# 检查（// respond）函数，没有发现加密函数
# 检查第一个（// debug detect）函数，发现它的作用是阻止你正常使用f12
# 检查第二个（// debug detect）函数，发现txsdefwsw()在index.html中调用过，发现它的作用是无限debugger

# 使用hook拦截debugger

# 检查（// decode）函数,发现它的作用是base64转换
# 对eval_encrypt中的eval含参函数的参数进行b64解码，获取了一个新的js文件，也就是要找的加密逻辑
# 检查该文件，可以找到city_realtime.html中两个eval函数的加密逻辑

# 替换setInterval
# 打开控制台，程序中断在debugger，在callback中选择上一层函数，可以看到setInterval(){} ,设置断点然后刷新，
# 在当前断点状态下，在console中把setInterval替换为空函数，再放开，就不会输出'检测到非法调试, 请关闭调试终端后刷新本页面重试!<br/>'了
# 接下来即可进行浏览器抓包工作