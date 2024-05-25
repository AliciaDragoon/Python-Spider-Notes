var webDES = function () {
    // var _0x4da59e = {
    //     'bUIIa': function _0x2a2af9(_0x779387, _0x4a4fec) {
    //         return _0x779387 + _0x4a4fec;
    //     }
    // };
    var func = function (a, b, c) {
        if (0 == b)
            return a['substr'](c);
        var r;
        r = '' + a['substr'](0, b);
        r += a['substr'](b+ c);
        return r
    }; // 计算密钥和iv
    this['shell'] = function (data) { // data就是data，或者叫e，或者叫密文
        // var _0x51eedc = { // 断点
        //     // 花指令：_0x51eedc()函数把+-*/><==符号混淆为了字符串
        //     'pKENi': function _0x2f627(_0x5b6f5a, _0x440924) {
        //         return _0x5b6f5a === _0x440924;
        //     }, // 'pKENi'函数用于判断两个参数是否相等
        //     'wnfPa': 'ZGz',
        //     'VMmle': '7|1|8|9|5|2|3|6|0|4',
        //     'GKWFf': function _0x1a4e13(_0x40cfde, _0x16f3c2) {
        //         return _0x40cfde == _0x16f3c2;
        //     },
        //     'MUPgQ': function _0x342f0d(_0x19038b, _0x4004d6) {
        //         return _0x19038b >= _0x4004d6;
        //     },
        //     'hLXma': function _0x55adaf(_0x45a871, _0x161bdf) {
        //         return _0x45a871 + _0x161bdf;
        //     },
        //     'JdOlO': function _0x13e00a(_0x5899a9, _0x4bb34d) {
        //         return _0x5899a9 + _0x4bb34d;
        //     },
        //     'qrTpg': function _0x1198fb(_0x55b317, _0x22e1db, _0x1b091a) {
        //         return _0x55b317(_0x22e1db, _0x1b091a);
        //     },
        //     'pdmMk': function _0xe2b022(_0x4af286, _0x4c2fd4) {
        //         return _0x4af286 - _0x4c2fd4;
        //     },
        //     'xVKWW': function _0x1094a3(_0x5f3627, _0x2a0ac5, _0x3ad2e5) {
        //         return _0x5f3627(_0x2a0ac5, _0x3ad2e5);
        //     }
        // };
        // if ('tgg' === 'ZGz') { // if (False) {
        //     this['_append'](a);
        //     return this['_process']();
        // } else {
        // 下列代码混淆了原代码的运行顺序
        // var _0x492a62 = ['7', '1', '8', '9', '5', '2', '3', '6', '0', '4']
        //   , _0x356b01 = 0;
        // while (true) {
        //     switch (_0x492a62[_0x356b01++]) { // 每次循环从_0x492a62这个数组取一个值
        //     case '0':
        //         a = _grsa_JS['DES']['decrypt']({
        //             'ciphertext': _grsa_JS['enc']['Hex']['parse'](data)
        //         }, b, {
        //             'iv': a,
        //             'mode': _grsa_JS['mode']['ECB'],
        //             'padding': _grsa_JS['pad']['Pkcs7']
        //         })['toString'](_grsa_JS['enc']['Utf8']);
        //         continue;
        //     case '1': // 第二次运行1
        //         if (_0x51eedc['GKWFf'](null, data) || _0x51eedc['MUPgQ'](16, data['length']))
        //             return data;
        //         continue;
        //     case '2':
        //         data = func(data, b, 8);
        //         continue;
        //     case '3':
        //         b = _grsa_JS['enc']['Utf8']['parse'](a);
        //         continue;
        //     case '4':
        //         return a['substring'](0, _0x51eedc['hLXma'](a['lastIndexOf']('}'), 1));
        //     case '5':
        //         a = data['substr'](b, 8);
        //         continue;
        //     case '6':
        //         a = _grsa_JS['enc']['Utf8']['parse'](a);
        //         continue;
        //     case '7': // 第一次运行7
        //         if (!navigator || !navigator['userAgent'])
        //             return '';
        //         continue;
        //     case '8': // 第三次运行8
        //         var a = _0x51eedc['JdOlO'](_0x51eedc['qrTpg'](parseInt, data[_0x51eedc['pdmMk'](data['length'], 1)], 16), 9)
        //           , b = _0x51eedc['xVKWW'](parseInt, data[a], 16);
        //         continue;
        //     case '9':
        //         data = func(data, a, 1);
        //         continue;
        //     }
        //     break;
        // }

        // 下列为正确顺序的代码（控制流平坦化后的代码）
        // if (!navigator || !navigator['userAgent'])
        //             return '';
        // if ((null == data) || (16 >= data['length']))
        //             return data;
        var a = parseInt(data[(data['length'] - 1)], 16) + 9; // 获取最后一个字符，转换为10进制，加上9
        var b = parseInt(data[a], 16); // 获取data[a]处的字符，转换为10进制
        data = func(data, a, 1);
        a = data['substr'](b, 8); // 从b位置开始截字符，截8个字符
        data = func(data, b, 8);

        // 把a, b处理成utf-8字节
        b = _grsa_JS['enc']['Utf8']['parse'](a);
        a = _grsa_JS['enc']['Utf8']['parse'](a);
        // DES解密
        a = _grsa_JS['DES']['decrypt']({
            'ciphertext': _grsa_JS['enc']['Hex']['parse'](data) // 猜测对data进行了16进制处理
        }, b, { // b是密钥
            'iv': a, // 偏移量
            'mode': _grsa_JS['mode']['ECB'], // 模式是ECB
            'padding': _grsa_JS['pad']['Pkcs7'] // 填充
        })['toString'](_grsa_JS['enc']['Utf8']); // 解密完成
        return a['substring'](0, (a['lastIndexOf']('}')+ 1)); // 保留开头到最后一个}位置的字符
    }
    // }
    ;
}