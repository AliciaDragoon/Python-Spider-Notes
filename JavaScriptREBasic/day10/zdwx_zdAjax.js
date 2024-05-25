window.zdAjax = function (e, o, n) {
    var t, i;
    e.data && "object" == r()(e.data) && (i = JSON.stringify(e.data)),
    $.ajax({
        // type: e.type || "post",
        // headers: {
        //     source: "pc",
        //     sessionId: $.cookie("sessionId") || "",
        //     token: $.cookie("token") || ""
        // },
        url: "/apis/" + e.url,
        // contentType: e.contentType || "application/json;charset=UTF-8",
        data: i,
        // dataType: e.dataType || "JSON",
        success: function (n) {
            // e.load && layer.close(t),
            // e.checkLogin && 4 == n.code ? window.location.href = "/login" : (e.showError && layer.msg(n.msg),
            o(n); // o(data)函数在返回数据后执行
        },
        // error: function (n) {
        //     o({
        //         code: -1,
        //         msg: "网络异常请稍后再试~"
        //     }),
        //     e.load && layer.close(t),
        //     e.showError && layer.msg("网络异常，请稍后再试！")
        // },
        // complete: function () {
        //     layer.close(t)
        // }
    })
}

// 加密逻辑伪代码
window.zdAjax({url: "", data: {}}, function (data) {
    console.log("接收到数据" + data)
    // e是请求参数，o是回调，n无意义
    window.zdAjax({url: "", data: {}}, function (data) {
        console.log("接收到数据" + data)
    })
})

window.zdAjax({url: '/common/getTime',}, function (data) {
    let t = data.data;
    let pwd = "Password";
    let password = jiami(pwd + "" + t)
    window.zdAjax({
        url: '/login/passwordLogin',
        data: {userName: username, password: password, imageCaptchaCode: imgCode}
    }, function (data) {
        // cookies处理
    })
})

// zdAjax(paramss, (ress) => {
//     var param = {
//         url: '/login/passwordLogin',
//         data: {
//             userName: username,
//             password: encryptFn(pwd + '' + ress.data),
//             imageCaptchaCode: imgCode,
//         },
//     };
//     zdAjax(param, (res) => {
//         if (res.code == 0) {
//             if ($('#auto-login').is(':checked')) {
//                 //自动登录
//                 keepOurCookie12('autoLogin', true, 30)
//                 keepOurCookie12('userInfo', JSON.stringify(res.data), expiresDay)
//                 keepOurCookie12('token', res.data.token, expiresDay)
//                 syncLogin(res.data, expiresDay)
//             } else {
//                 keepOurCookie12('autoLogin', null)
//                 keepOurCookie12('userInfo', JSON.stringify(res.data))
//                 keepOurCookie12('token', res.data.token)
//                 syncLogin(res.data)
//             }
//
//             login.jump(res.data.isBindingMobile)
//         } else if (res.code == '9') {
//             //密码错误达到了两次
//             login.getImgCode($('#nimg-code .img-code-click'))
//             $('#nimg-code').addClass('show')
//             layer.msg(res.msg)
//         } else {
//             layer.msg(res.msg);
//         }
//     });
// });
// window.syncLogin = function (e, o) {
//     var n = {
//         path: "/",
//         domain: "wangxiao.cn"
//     };
//     o && (n.expires = o),
//         $.cookie("UserCookieName", e.userName, n),
//         $.cookie("OldUsername2", e.userNameCookies, n),
//         $.cookie("OldUsername", e.userNameCookies, n),
//         $.cookie("OldPassword", e.passwordCookies, n),
//         $.cookie("UserCookieName_", e.userName, n),
//         $.cookie("OldUsername2_", e.userNameCookies, n),
//         $.cookie("OldUsername_", e.userNameCookies, n),
//         $.cookie("OldPassword_", e.passwordCookies, n),
//         e.sign && (n.expires = 365,
//         $.cookie(e.userName + "_exam", e.sign, n))
// }