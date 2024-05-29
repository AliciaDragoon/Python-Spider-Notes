const askiZExYII01 = "aPnyDR5Ca6FMIfdw";//AESkey，可自定义
const asideGdRY692 = "bNpeyqJl34VlZ7ng";//密钥偏移量IV，可自定义

const ackK9cbiA0YB = "dX1N15fjv5KdeCyi";//AESkey，可自定义
const acimrLO29gRI = "f3v35CzxuYjqwizp";//密钥偏移量IV，可自定义

const dsk9EbiUpi5W = "hIFclTxH0JalYZiu";//DESkey，可自定义
const dsi3gJ2aZe1f = "xMFHANC8X1TunaGs";//密钥偏移量IV，可自定义

const dckE15Yk15AF = "oHLKvpN54hwpLWjt";//DESkey，可自定义
const dcik4kPiOWjo = "pdgLk9FGBd5kXbm0";//密钥偏移量IV，可自定义

const aes_local_key = 'emhlbnFpcGFsbWtleQ==';
const aes_local_iv = 'emhlbnFpcGFsbWl2';

var BASE64 = {
    encrypt: function (text) {
        var b = new Base64();
        return b.encode(text);
    },
    decrypt: function (text) {
        var b = new Base64();
        return b.decode(text);
    }
};

var DES = {
    encrypt: function (text, key, iv) {
        var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
        var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.DES.encrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString();
    },
    decrypt: function (text, key, iv) {
        var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
        var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.DES.decrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString(CryptoJS.enc.Utf8);
    }
};

var AES = {
    encrypt: function (text, key, iv) {
        var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
        var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
        // console.log('real key:', secretkey);
        // console.log('real iv:', secretiv);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.AES.encrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString();
    },
    decrypt: function (text, key, iv) {
        var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
        var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
        secretkey = CryptoJS.enc.Utf8.parse(secretkey);
        secretiv = CryptoJS.enc.Utf8.parse(secretiv);
        var result = CryptoJS.AES.decrypt(text, secretkey, {
            iv: secretiv,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        });
        return result.toString(CryptoJS.enc.Utf8);
    }
};

var localStorageUtil = {
    save: function (name, value) {
        var text = JSON.stringify(value);
        text = BASE64.encrypt(text);
        text = AES.encrypt(text, aes_local_key, aes_local_iv);
        try {
            localStorage.setItem(name, text);
        } catch (oException) {
            if (oException.name === 'QuotaExceededError') {
                // console.log('超出本地存储限额！');
                localStorage.clear();
                localStorage.setItem(name, text);
            }
        }
    },
    check: function (name) {
        return localStorage.getItem(name);
    },
    getValue: function (name) {
        var text = localStorage.getItem(name);
        var result = null;
        if (text) {
            text = AES.decrypt(text, aes_local_key, aes_local_iv);
            text = BASE64.decrypt(text);
            result = JSON.parse(text);
        }
        return result;
    },
    remove: function (name) {
        localStorage.removeItem(name);
    }
};

// console.log('base64', BASE64.encrypt('key'));

function dp68JtHoJJZ(phqbwou) {
    phqbwou = DES.decrypt(phqbwou, dsk9EbiUpi5W, dsi3gJ2aZe1f);
    return phqbwou;
}

function d2EFOt36ua(phqbwou) {
    phqbwou = AES.decrypt(phqbwou, askiZExYII01, asideGdRY692);
    return phqbwou;
}

function gAmw9oKGCka50hFH(key, period) {
    if (typeof period === 'undefined') {
        period = 0;
    }
    var d = DES.encrypt(key);
    d = BASE64.encrypt(key);
    var data = localStorageUtil.getValue(key);
    if (data) { // 判断是否过期
        const time = data.time;
        const current = new Date().getTime();
        if (new Date().getHours() >= 0 && new Date().getHours() < 5 && period > 1) {
            period = 1;
        }
        if (current - (period * 60 * 60 * 1000) > time) { // 更新
            data = null;
        }
        // 防止1-5点用户不打开页面，跨天的情况
        if (new Date().getHours() >= 5 && new Date(time).getDate() !== new Date().getDate() && period === 24) {
            data = null;
        }
    }
    return data;
}

function ObjectSort(obj) {
    var newObject = {};
    Object.keys(obj).sort().map(function (key) {
        newObject[key] = obj[key];
    });
    return newObject;
}

function deIZLF7oahc0DLiXbqt(data) {
    data = AES.decrypt(data, askiZExYII01, asideGdRY692);
    data = DES.decrypt(data, dsk9EbiUpi5W, dsi3gJ2aZe1f);
    data = BASE64.decrypt(data);
    return data;
}

var pov0M2gfR = (function () {

    function ObjectSort(obj) {
        var newObject = {};
        Object.keys(obj).sort().map(function (key) {
            newObject[key] = obj[key];
        });
        return newObject;
    }

    return function (method, obj) {
        var appId = '271c2aab7dd615dacbadcb41d3c77fa4';
        var clienttype = 'WEB';
        var timestamp = new Date().getTime();
        // console.log(method, obj,ObjectSort(obj),appId + method + timestamp + 'WEIXIN' + JSON.stringify(ObjectSort(obj)));
        var param = {
            appId: appId,
            method: method,
            timestamp: timestamp,
            clienttype: clienttype,
            object: obj,
            secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
        };
        param = BASE64.encrypt(JSON.stringify(param));
        param = DES.encrypt(param, dckE15Yk15AF, dcik4kPiOWjo);
        return param;
    };
})();

function sW7FumD53pAq3ysvobb(m4Sq1jVkq, ogFjn1FgMP, cFaUNrMEF, prBNGk5) {

    const ktsu = hex_md5(m4Sq1jVkq + JSON.stringify(ogFjn1FgMP));

    const dgytI = gAmw9oKGCka50hFH(ktsu, prBNGk5);
    if (!dgytI) {
        var phqbwou = pov0M2gfR(m4Sq1jVkq, ogFjn1FgMP);
        $.ajax({
            url: '../apinew/aqistudyapi.php',
            data: {hXhY1B2Kd: phqbwou},
            type: "post",
            success: function (dgytI) {
                dgytI = deIZLF7oahc0DLiXbqt(dgytI);
                ouK2tR = JSON.parse(dgytI);
                if (ouK2tR.success) {
                    if (prBNGk5 > 0) {
                        ouK2tR.result.time = new Date().getTime(); // 添加当前时间
                        localStorageUtil.save(ktsu, ouK2tR.result);
                    }
                    cFaUNrMEF(ouK2tR.result);
                } else {
                    console.log(ouK2tR.errcode, ouK2tR.errmsg);
                }
            }
        });
    } else {
        cFaUNrMEF(dgytI);
    }
}