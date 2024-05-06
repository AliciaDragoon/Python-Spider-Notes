// function fn(a, b) {
//     console.log("我是fn")
// }
//
// // js函数不强制实参和形参相等
// fn(1, 2, 3, 4, 5);
// fn(1, 2);
// fn();

// function gn(a, b) {
//     console.log(a);
//     console.log(b);
// }
// gn(1, 2, 3, 4, 5);
// gn(1, 2);
// gn();

function hn(a, b) {
    console.log(a)
    console.log(b)
    // 每个函数自带arguments，装载所有的参数
    console.log(arguments)
}

hn(1, 2, 3, 4, 5)
hn(1, 2)