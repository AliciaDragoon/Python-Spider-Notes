!function () {
    function a(a) { // d函数中a=16
        a = 16;
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        // for (d = 0; a > d; d += 1)
        for (d = 0; d < 16; d += 1) {
            e = Math.random() * b.length; // Math.random()得到的是0-1的随机值，b.length=62
            e = Math.floor(e); // 取整
            c += b.charAt(e); // b.charAt(e)是b里的第e个字符
        } // 从b中随机抽16个字符拼接成字符串
        return c
    }

    function b(data, b) {
        var c = CryptoJS.enc.Utf8.parse(b) // key
            , d = CryptoJS.enc.Utf8.parse("0102030405060708") // iv
            , e = CryptoJS.enc.Utf8.parse(data) // 数据
            , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }

    function c(a, b, c) {
        setMaxDigits(131);
        var d = new RSAKeyPair(b, "", c); // d是公钥
        var e = encryptedString(d, a); //网易云音乐在 encryptedString函数中对标准RSA算法做了修改
        return e
    }


    // function d(d, e, f, g) { // asrsea函数的位置
    //     var h = {}
    //         , i = a(16);
    //     return h.encText = b(d, g),
    //         h.encText = b(h.encText, i),
    //         h.encSecKey = c(i, e, f),
    //         h
    // }
    function d(data, e, f, g) {
        var h = {}
        // , i = a(16); // i是一个16位随机字符串
        var i = 'N7BrTCq7VltLi9ez'; // 用控制台生成一个
        h.encText = b(data, g); // 对data进行加密,密钥是g，iv是0102030405060708
        // h=>{encText:xxx}
        h.encText = b(h.encText, i); //再次调用b函数加密，内容是上次的加密内容，密钥是i，iv是0102030405060708
        // h.encSecKey = c(i, e, f); // 对密钥i进行rsa加密，密钥是e和f，然后传给服务器
        // 可以用控制台生成一个encSecKey（推荐），或者用python计算一个
        h.encSecKey = 'e05a268242d0b50fbac6d20041bfab53e0e163f18a4ffc9805aece65bf37adc046ef70e1e8a44de3cfd780a9204c60bc289a864fd2e1dc4c22d91a948f9f9abf15ecdd6151ec5feed1624381a7c27f49a2945dcd1d321f5507d8a6477ed83f75584c802c3e638412d26a4db4203a05c332f56d30e8a33856c3ebf927b31af933'
        return h
        // h=>{encText:xxx, encSecKey:xxx}
    }

    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
            f
    }

    window.asrsea = d,
        window.ecnonasr = e
}();