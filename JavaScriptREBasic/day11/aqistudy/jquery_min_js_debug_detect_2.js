function txsdefwsw() {
    var r = "V", n = "5", e = "8";

    function o(r) {
        if (!r) return "";
        for (var t = "", n = 44106, e = 0; e < r.length; e++) {
            var o = r.charCodeAt(e) ^ n;
            n = n * e % 256 + 2333, t += String.fromCharCode(o)
        }
        return t
    }

    try {
        // var a = ["r", o("갯"), "g", o("갭"), function (t) {
        // 把function o(r)复制到浏览器控制台后，输入o("갯")，结果返回'e'，输入o("갭")，结果返回'g'
        // var a = ["r", 'e', "g", 'g',
        //     // function (t) {
        //     // if (!t) return "";
        //     // for (var o = "", a = r + n + e + "7", c = 45860, f = 0; f < t.length; f++) {
        //     //     var i = t.charCodeAt(f);
        //     //     c = (c + 1) % a.length, i ^= a.charCodeAt(c), o += String.fromCharCode(i)
        //     // }
        //     // return o}("@") // 把该自运行函数复制到控制台后，结果返回'u'
        //     'u'
        //     , "b", "e", "d"].reverse().join(""); // a = 'debugger'
        var a = 'debugger';

        !function c(r) {
            (1 !== ("" + r / r).length || 0 === r) // 复制到浏览器控制台后,结果返回true
            && function () {
            }.constructor(a)(), c(++r) // 函数无限运行，r无限自增，直至报错
        }(0)
    } catch (a) {
        setTimeout(txsdefwsw, 100)
    } // 如果出错，设置定时器，100ms后再运行txsdefwsw函数
}