function txsdefwsw() {
    // var r = "V", n = "5", e = "8";
    //
    // function o(r) {
    //     if (!r) return "";
    //     for (var t = "", n = 44106, e = 0; e < r.length; e++) {
    //         var o = r.charCodeAt(e) ^ n;
    //         n = n * e % 256 + 2333, t += String.fromCharCode(o)
    //     }
    //     return t
    // }

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
            &&
            function () {
            }.constructor(a)(), // 输出'debugger'
            c(++r) // 函数无限运行，r无限自增，直至报错
        }(0) // r初始化为0
    } catch (a) {
        setTimeout(txsdefwsw, 100)
    } // 如果出错，设置定时器，100ms后再运行txsdefwsw函数
}

// 遇到无限debugger
// 先记录一下constructor
Function.prototype._constructor = Function.prototype.constructor
// 拦截debugger
Function.prototype._constructor = function () {
    // 为了防止其他调用的干扰，不能在函数中接收参数
    if (arguments[0] === "debugger"){
        console.log("禁止debugger")
        return function(){}; // 拦截异常的constructor
    } else{
        return Function.prototype._constructor.apply(this, arguments) // 正常的constructor不会受到影响
    }
}
// 该hook对于无限debugger不是一定有效(经测试，确实无效)