var cxT6N = t9k.be9V;
t9k.be9V = function (X9O, e9f) {
    var i9b = {} // 在这里设置断点，step over next function call两次后，发现e9f的值无变化，说明这里的NEJ.X函数不起作用
        , e9f = NEJ.X({}, e9f)
        , mt1x = X9O.indexOf("?"); // 检查url中有无"?"
    // if (window.GEnc && /(^|\.com)\/api/.test(X9O) && !(e9f.headers && e9f.headers[eu0x.AW4a] == eu0x.Gc5h) && !e9f.noEnc) { // 该判断语句没有赋值，改变数值，调用其他函数，所以它不起作用
        // if (mt1x != -1) { // 控制台step over next function call到这里mt1x = -1，所以该判断语句不起作用
        //     i9b = j9a.gP0x(X9O.substring(mt1x + 1));
        //     X9O = X9O.substring(0, mt1x)
        // }
        if (e9f.query) { // 判断e9f有没有query
            i9b = NEJ.X(i9b, j9a.fQ0x(e9f.query) ? j9a.gP0x(e9f.query) : e9f.query) // 三元表达式
        } // 函数运行到这里，i9b就是需要的data参数
        // if (e9f.data) { // 判断e9f有没有data。没有，所以该判断语句不起作用
        //     i9b = NEJ.X(i9b, j9a.fQ0x(e9f.data) ? j9a.gP0x(e9f.data) : e9f.data)
        // }
        i9b["csrf_token"] = t9k.gO0x("__csrf"); // data增加了一个叫csrf_token的新参数，函数运算到下一行，其值为""
        X9O = X9O.replace("api", "weapi"); // 把url中的api替换为weapi
        e9f.method = "post";
        delete e9f.query; // 删除e9f里的query，但i9b里还有

        var bVi3x = window.asrsea(JSON.stringify(i9b), bse9V(["流泪", "强"]), bse9V(Qu9l.md), bse9V(["爱心", "女孩", "惊恐", "大笑"]));
        // 第一个参数把i9b变成了字符串，bse9V(["流泪", "强"])在console中为'010001'，bse9V(Qu9l.md)和bse9V(["爱心", "女孩", "惊恐", "大笑"])在console中为定值，猜测这几个参数是密钥或者盐，asrsea是加密函数

        e9f.data = j9a.cr9i({
            params: bVi3x.encText,
            encSecKey: bVi3x.encSecKey
        })
    }
    var cdnHost = "y.music.163.com";
    var apiHost = "interface.music.163.com";
    if (location.host === cdnHost) {
        X9O = X9O.replace(cdnHost, apiHost);
        if (X9O.match(/^\/(we)?api/)) {
            X9O = "//" + apiHost + X9O
        }
        e9f.cookie = true
    }
    cxT6N(X9O, e9f)
}
;