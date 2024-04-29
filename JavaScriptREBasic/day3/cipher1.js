// md5
// var encrypt = function(data) {
//     console.log("md5数据加密"+ data)
// }

// 闭包函数
// (function (w) {
//     var encrypt = function (data) {
//         console.log("md5数据加密" + data);
//     };
//     w.encrypt = encrypt;
//     // 通过window向外传递
// })(window);

// var key = "md5_key";
// window.md5 = function (){
//     console.log("开始md5加密");
//     console.log(key);
//     return "md5加密结果";
// }

(function () {
    var key = "md5_key";
    // 局部变量，不受其他js文件的影响
    window.md5 = function () {
        console.log("开始md5加密");
        console.log(key);
        return "md5加密结果";
    }
    // 提供给外界的接口，外界可使用该变量来访问闭包中的功能
})()