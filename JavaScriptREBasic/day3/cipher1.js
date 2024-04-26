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

var key = "md5_key";
window.md5 = function (){
    console.log("开始md5加密");
    console.log(key);
    return "md5加密结果";
}