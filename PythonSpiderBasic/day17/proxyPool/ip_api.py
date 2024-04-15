# 提供给用户的api接口
# http://127.0.0.1:5800/get_proxy
from sanic import Sanic, json
from sanic_cors import CORS
from proxy_redis import ProxyRedis

# 创建app
app = Sanic("ip")

# 解决跨域问题
CORS(app)

red = ProxyRedis()


@app.route("/get_proxy")
# 处理http请求
def sanic_http_request(request):
    ip = red.get_keyong_proxy()
    # 返回给客户端
    return json({"ip": ip})


def run():
    app.run(host="127.0.0.1", port=5800)


if __name__ == '__main__':
    run()
