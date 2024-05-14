# 逆向ob混淆
# 方案： 手动；补环境（jsdom）；AST
# 在Network-Initiator-PostAPI中找到$.ajax()中的success()中的data,即Preview中接收到的数据
# 在data（混淆为了e）设置断点，刷新后控制台输入e，得到了Preview中接收到的数据
# 控制台输入webInstace.shell(e)，得到了解密后的数据，说明webInstace.shell()就是要找的解密算法
# 找到该函数，即function(_0xa0c834){}，在内部设置断点后，恢复脚本执行
# 选中_0x2246('0x257', 'nArV')后显示'shell'，说明该函数实为this['shell']

# JS伪代码
# var webDES = function(){
#     ...
#     this["shell"] = function(e){
#           // 断点
#           ...
#     }
#     ...
# },webInstace = new webDES();
#
# webInstance.shell(e)

# 选中其他的_0x2246()，可得该函数的功能为混淆字符串
# 使用控制台依次计算_0x2246()混淆的字符串，并将endataDecrypt.js中混淆的字符串还原为正常字符串
# 还原_0x51eedc()混淆的字符
# 使用浏览器控制台还原看不懂的东西
# 删除不需要的代码
# IDE中_0x51eedc变灰了，表明花指令还原完毕
# 把变量和函数全局替换为a, b ,func

# 前端加密解密伪代码
# xxx.AES.encrypt({
#   text:xxx //数据
#   }, key //密钥, {
#   iv:xxx,
#   mode: xxx.mode.ECB,
#   padding:xxx //加密参数
#   });
# xxx.AES.decrypt({数据}, 密钥, {加密参数});
# 简化剩余的函数名和变量
# 将混肴后的js加密算法还原后，转换为py代码
import binascii
import json
from Crypto.Cipher import DES
import requests


def func(a, b, c):
    if b == 0:
        return a[c:]
    r = a[:b] + a[b + c:]
    return r


def shell(data):
    a = int(data[-1], 16) + 9
    b = int(data[a], 16)
    data = func(data, a, 1)
    a = data[b:b + 8]
    data = func(data, b, 8)
    # 把data从16进制转换为字节
    bs = binascii.a2b_hex(data)
    key = a.encode('utf-8')
    bs = des_encrypt(bs, key)
    s = bs.decode("utf-8")
    # print(s)
    # json
    s = s[:s.rindex("}") + 1]
    dic = json.loads(s)
    # print(dic)
    return dic


def des_encrypt(data, key):
    des = DES.new(key, DES.MODE_ECB)
    bs = des.decrypt(data)
    return bs


if __name__ == '__main__':
    # shell("94696E8CE4FBF6E0EE02BF3C5E206FD277EF6D0260ECB719B9234BD0719822561BAAA3739E5DB18F499B310E875DF2DF2C5033E3B7088D4C490AAD731460E4A3DE06344EE85664870D1CF223047EA15A0CB828777F6A5A9EA1B67D1D78C4EA2E0D45D318AE7F41E23540CEE9066431376F3AF2DFF882B7AE83DC9A1C8706751EA2C12D5E615986A0F523CC5E0E9CB64A60E68A8734C8BC00E884D0ACC23B2A031EDA8BACD2BC1765CB5318453AA342C1610DD717D3D8786B0080C64E85186B10F7D6F24841A1B7CC653FDD1A7F1D3A3D8C6A24E5F7C9794E735FEDA8027B5FD6D56D2B02FDFD6A67EF0E748F4606196CE5AAD8071D595DCDB11F3FFA358F1386B0B464EEA3105CF6D60AA8AF9720FAE60AB9FD3BAD153FDD20208F782A03472192F71646D9D16426D1FF3617AC459485B0BF4ABDECFC8B5AF72924CCBFB643C79BA6878AAC15E29E2412DFC47F65C5B90A1FB49A1B53BDC7418EDAA81C6D586861A996DAE1D54BE7EE7D8BB34D52E6190291DD4BD845EF9A8B91F9CC2996FD0F43BDC4DCD9647F45DF5333E841D16F22BF78497783B6394F7A9E26573C88C7D0A725A83EE3B3B7886C2859B961758E892C8BD827E2FC80E466E965B51D11045D0DE21BE70D64102FFBFF8711820FE7FBDAE4FD18C1546FDAEFD61259CF64D1075ADEDD9D4DDE861E9B686B2A9D73146FF96A144491AD45E63120156BDD45BB7E038084E815F87C854B6C5D0F13E8A9E0A3C80D3435F4A61CC09BC389D432558DC7177918067E1B70652234EDBA26827ADD250785ACA2600C4C85042593D0DCBFF4F9A8AE44C758AD58223385B56581D3A8C85FE44E8598EAE893C78CB6562816C17CCECE5D408FB32B660905DFBC08FA6D948EA7EFC27A2264BB0EECABD06265F96725FB45FDC6CB0EB425396E51EC9F92DBC075C4094DD2908F6D7D8D269A7ED1C637D2D7FA748664C00FA27F87D25BBB692E8CB7123BD8E724A6ECCA3B7A19A0EBA502E02A3E09B278D1CBDD2055EFFF3E00D5F3E191664908A93042D876C84F356E998643C9E45059D7CDE72C1EB41E43C3FD68560A9D691350DC9B7336CA8B67FF7803CA3D31B0569929A9D0D8B66684A92D0A473F429209571DD1F936AF8CE45A5DE5A3F19AECACA0E090B6E93B9A87E9265D900C8C701A8CAFC6913D64700199BAA039597BB8486E7C75EC511C2EADB6DC275DF2DF2C5033E3B4A2FD7FC9F18774A460E4A3DE06344EE39B164E9F0311913E016B74A5EFB7D01CDB485A5F114BE505FDC6CB0EB4253964BEF458C9B7402D54094DD2908F6D7D8A65F2E3BF7E6C204460E7F2CB4DF2A4B33894DBDF1A79BE17123BD8E724A6ECC3B85F2C648A7AC2202A3E09B278D1CBD920223882BC26AFE3E191664908A93042D876C84F356E9980C7C702012973808DE00C5F9401396988560A9D691350DC9B7336CA8B67FF7803CA3D31B0569929A9D0D8B66684A92D0A473F429209571DD1F936AF8CE45A5DE37F85689B11797F30B6E93B9A87E9265D2462DFD801663616EBB6F9122C5ACEF9473B70E139DB1AD5EC511C2EADB6DC275DF2DF2C5033E3B76C1C59F6FC9F200460E4A3DE06344EE7E21E24388938B4641941CF782CFD00CCE08D27DD03B84222F74915580C54A2E59DA33C536270DCF4BE73D6DDAF825981A498249A1598CAB2040439423A72FD7B70DA35B626BE95515986A0F523CC5E0E9CB64A60E68A8734C8BC00E884D0ACC3B9E536E9372B18D2BC1765CB53184530A64E5BCB50B49A9788AE1C33C97DB0836CF0EF256C273F78BB447B6836D89EBDE339166DB0C6FB5CD2FAA50707CE31BBD7C0E7192646C4CDE66114319C33CC64352080B2704785446C62F19FE3F8EB00A450ACE52B6AD5FBA3BE10E46C6ABBB0CFD866D41F4A63D0C73B2C0AEF6A4ACD1D45F12D514374B37354F162BDDAF9E0A3A44AB60031E661730ABB7F13E3A42112DA7168DAC0763AE3002AC90643B133E9AEDB1B401A84044FFC68F146E4DD859DA33C536270DCF280D9156FA4F00C6CE198AA0100E25532040439423A72FD7F4CEFE1E6723FF6D15986A0F523CC5E007C89BB81A3704A64C8BC00E884D0ACC1CB5360AF89689032BC1765CB5318453AA342C1610DD717D3D8786B0080C64E85186B10F7D6F24841A1B7CC653FDD1A7E8DA2BD2153A35A9726D97F41B4A70C027B5FD6D56D2B02FDFD6A67EF0E748F4606196CE5AAD8071D595DCDB11F3FFA358F1386B0B464EEA331F908B6D24C958929CEDA97721FF3194E9EEA59FFB25F89443E8B55CAB919A8736A5FBDEE1DEA00B850F651707F783CFC8B5AF72924CCBFB643C79BA6878AA5D837971FE90FF68F65C5B90A1FB49A130739867672DEE00851493E7B1B4C052F7CBD8A4FE7C7E2759DA33C536270DCF2DFBBE744EFFDD771BE56BFFCAFCBF962040439423A72FD742E0A9BA7B4B9F8E15986A0F523CC5E033765C35AE2A69B74C8BC00E884D0ACC1B51E73F1EC7BD362BC1765CB5318453AA342C1610DD717D3D8786B0080C64E85186B10F7D6F24841A1B7CC653FDD1A7F1D3A3D8C6A24E5F4B1D71A43739F9EB27B5FD6D56D2B02FDFD6A67EF0E748F4606196CE5AAD8071D595DCDB11F3FFA358F1386B0B464EEA3105CF6D60AA8AF9609D507B6704E03F505593AF02A0973D28AAD248D120D31E015ECF630A3FCCF63E125A5A4A245A28CFC8B5AF72924CCBFB643C79BA6878AA9F1976F8CCD324FCF65C5B90A1FB49A1E1859B323F84A55528A43833BD4BC0023F4399E24C6C34722792F532F88291F2EE664886352C7388FF485C2AD1D3F76F974862E3B55C7A1340EC82DD46671FD4BF9B322E8959728846EDFC2683D7BB77C7C53225732AC8FFE684296EF86B29B9F0E31E45F443773ADA61968CFD7AB71E96F0104308451D1F4EFE4C0C573F0684051C33541A8F83B67C8B7FED7293C85DC2F675EB4E840AF9EC86D1E6B54CC8C23650207CF42B3EB1A2EDAF0351D21C77D2330B56DF07085B992DDBDE016A7F2CE5CCE444C0FAFE1921B0804824B35A86265CA9D0DD99FC54C7165C309BC5863C5919A239BC15BF52264B4F85BE79DEACEC2E3C885C280E0B78D45AC13251F88955A53489DB769FC51893B1DDF0C65C1046F2BCC9472A8EF365E11E123E774A7106AC6ECEC8095C0559DA33C536270DCFF6553C1C5DC0A4F01BE56BFFCAFCBF962040439423A72FD7AD48F2D5C97E200015986A0F523CC5E033765C35AE2A69B74C8BC00E884D0ACC084A1DCCEA44E62B2BC1765CB53184530A64E5BCB50B49A9788AE1C33C97DB0836CF0EF256C273F72548FD2E997466EADE339166DB0C6FB5CD2FAA50707CE31BBD7C0E7192646C4CDE66114319C33CC64352080B2704785446C62F19FE3F8EB00A450ACE52B6AD5FB9BA98049021098A376D086EF367EAD906E291D78F2ACF75E19B409654E32FF2B0B98EDBA6AC592A0A3A44AB60031E665F6B74DAD55C56DE017A6F2E53EB2C52AE3002AC90643B131177F8B4C4CB1B4D7BEAD5A1877F5EF559DA33C536270DCF5687F19F92FFFB7BAC71D4BD66F745A52040439423A72FD7F6927F7C4B8FFA1215986A0F523CC5E0057F580E2F76902F4C8BC00E884D0ACC3B6EE96806758C86FC754DA639EF219DD9638674C1A73A99788AE1C33C97DB0836CF0EF256C273F75DD9F350DA412D93DE339166DB0C6FB5CD2FAA50707CE31BBD7C0E7192646C4CDE66114319C33CC64352080B2704785446C62F19FE3F8EB042225DE88A6D2293D977A5536D8FC7FF802FBE286F29FBE8DA0363536A9F31EE6868D904B7863768E85B860D9A4EF1820A3A44AB60031E6671561FAD577DF67752A17CAA29F1AA35AE3002AC90643B134AC5D1B960150BEC3EBC9DFD0A2D39A583F790152D1675505FDC6CB0EB4253961E4F8A64136476EC4094DD2908F6D7D8E5BB49D31B95140ABC29C43DD89E5667AF9776CAD518B1F07123BD8E724A6ECC801B519F3D0B049002A3E09B278D1CBD920223882BC26AFE3E191664908A93042D876C84F356E9980C7C70201297380872C1EB41E43C3FD68560A9D691350DC9B7336CA8B67FF7803CA3D31B0569929A9D0D8B66684A92D0A473F429209571DD1F936AF8CE45A5DEBB98068E571D08C60B6E93B9A87E9265A58AC521F83BDA2E1D21CB6C06BCCEF56BD09BFB6900821D5EC511C2EADB6DC275DF2DF2C5033E3B10CA834661A0E9B5460E4A3DE06344EEFA411AF09B23C5D825D06AB042E3F4544BB5CF018EE97C778C4EA2E0D45D318A49E53FF69C725AB2EB29C3E76857501C882B7AE83DC9A1C87D5C2E10172443DC48D32A665A91B349258DB523F55DBF1A864E7626F382A736627F4C186D5B6F56D9728CAD31014FE182DC3603B5878BB85697B1C2509A1ADCCFE4FD12225B45744C0955BC952F36CF7E7A53BAEE35AC1A3D091B6D0469E6DC32EB5563FF5608C73516109FCE8BABB8CE84E0FC93A7DE84FBF8FE7133846737DCF2A3BEA57852AFCB0B0A8F48E0D6F80736274FF0836A69887FFC69176B4BAF6078EEBD01D0D1DEF6251EA921D3CBEE2B1DD561D0185E895C96D3DBE5238986031F0177CC1AA366FCC73B64DBB4369DD17D4554BB242A91C72A844459A49835B17324C77DD7336959DA33C536270DCF4BE73D6DDAF825981A498249A1598CAB2040439423A72FD71E2FA33DBCB715F115986A0F523CC5E0057F580E2F76902F4C8BC00E884D0ACC64CC189785FD1881FC754DA639EF219DD9638674C1A73A99788AE1C33C97DB0836CF0EF256C273F7E62EB8EC316405E7DE339166DB0C6FB5CD2FAA50707CE31BBD7C0E7192646C4CDE66114319C33CC64352080B2704785446C62F19FE3F8EB042225DE88A6D2293D01936413B0327A0ED55964403C5532AB7EA23687D234D28FA45143F8C6A73D3EBEC857F9646448A0A3A44AB60031E661730ABB7F13E3A42BC45105CEDD8633DAE3002AC90643B1332440252EB4F028B8C24E38B52855B7B46F11C8843356EAB09C9F9D9C23D99415FDC6CB0EB4253961E4F8A64136476EC4094DD2908F6D7D880940261836A67F2C5DC29408A1C32ACD7FD944C376C57997123BD8E724A6ECC5BE7ABA32F12A82A02A3E09B278D1CBD64E6AFAEB6B95C790BC3D08B2A9703C2051C33541A8F83B67C8B7FED7293C85D378D7216ACDF4BC5EC86D1E6B54CC8C23650207CF42B3EB1A2EDAF0351D21C77D2330B56DF07085B992DDBDE016A7F2CE5CCE444C0FAFE194EAB6CEA926491516A3101C89C84BEDF6DE4B732E07032E70D63B47D8803E70BA8CD823A6D3B08FB7C7ADDDA60D9311C78D45AC13251F88955A53489DB769FC5CF30F53E8AD0D4E846F2BCC9472A8EF332779387EE8E7508144A85CBFF0E13C540B516610C9DB5C5EDF40F460139A86FEA9251581F4CD9AEFE4918840EB6D0B651B5329537A11C3DE5814FC19FCB3CFAA12C9471C58CA2C41EEE97505D0EDA4CBB6CBF1964A733B6BF9EE5D882902898459175937A519F6722782B2D0C1288FA6CC1DFFEDF604707D64102FFBFF8711820FE7FBDAE4FD18CAB2264958B9707C41ED4DF2DED7B5ABCDDE861E9B686B2A9D73146FF96A144491AD45E63120156BDD45BB7E038084E815F87C854B6C5D0F13E8A9E0A3C80D3438687D3C20108AE78780E32CD502985EE32C41C455951908832590220912CAF8C7EA67110637F75473D0DCBFF4F9A8AE4CE7461AD204CE5C6F1D75F9DED9A0D00E8598EAE893C78CB3111BD5047B544DC8A8E70C938581081EA29CB2330E8761B5D854F595EAD38F03B3A9C178253721A26035D3D532A2A962FE2D630E06F58E078656B9C5E237839D2850B8890E78D475694D801A7D058309EF04235B4C94779C523DCD2BB4051F68FAC9538608F4781B51F88648FCB8A781A1B7CC653FDD1A7F1D3A3D8C6A24E5FF32CE8109713022927B5FD6D56D2B02FDFD6A67EF0E748F4606196CE5AAD8071D595DCDB11F3FFA358F1386B0B464EEA3105CF6D60AA8AF9C0FABF43DDD9E6EE505593AF02A0973D8150B45E39F52C16E343DFAE3A3924E6210B9750BF6F4AF8CFC8B5AF72924CCBFB643C79BA6878AA00D1C00FD77074A2F65C5B90A1FB49A124CAC862DAE7288E5D1B122C1B1998BB7C36CF7B212DCDBE5D854F595EAD38F0462B823292FFD0BE26035D3D532A2A962FE2D630E06F58E0AD9F473AC15E6959D2850B8890E78D472BA93B6053C0C7EA2AC8D8CED1B32F13C523DCD2BB4051F63DD10D305F2E43B5CC8D40FA29B006F6B1720F3556BE3DD3D64102FFBFF8711820FE7FBDAE4FD18CEE683A022A09F298AA1021C6B9E825F1DDE861E9B686B2A9D73146FF96A144491AD45E63120156BDD45BB7E038084E815F87C854B6C5D0F13E8A9E0A3C80D343A638B5800458FE93780E32CD502985EE4438F1688CA4F06A029A3FDA858DAA7926F390015FBFCF623D0DCBFF4F9A8AE488EF88F2E51A5B46939B6DF2208467D7E8598EAE893C78CB35D12F53E2CFC332868AE613B539839B79C11689E81C5FE3EE664886352C73883A73ACF31C5D1961D9C9E757C6BC85CB198BEA6AF0AEADBDF33A02E25A480B8C46EDFC2683D7BB77E35C64FAA50C8CDAE684296EF86B29B94484469CFF52A038DA61968CFD7AB71E96F0104308451D1F4EFE4C0C573F0684051C33541A8F83B67C8B7FED7293C85DBCB7C3A4271AF46420320FC40C2F0A073650207CF42B3EB1A2EDAF0351D21C77D2330B56DF07085B992DDBDE016A7F2CE5CCE444C0FAFE1921B0804824B35A86B5DF5560974C1028C7165C309BC5863C62B40DDDB13FC2A0AE4C0B67BC2129FB56B4231FC586947478D45AC13251F88955A53489DB769FC571E4A2486AE1282246F2BCC9472A8EF3AE99DCCFFD62E0F9BAE55E5ADFAE806E2461C0C075685FA2A403685BA583C70A5D854F595EAD38F0462B823292FFD0BE26035D3D532A2A962FE2D630E06F58E00B245965ECD431E5D2850B8890E78D472BA93B6053C0C7EA5CB73A23171EB38BC523DCD2BB4051F68FAC9538608F4781B51F88648FCB8A781A1B7CC653FDD1A7E8DA2BD2153A35A9AA661E512C58C1BD27B5FD6D56D2B02FDFD6A67EF0E748F4606196CE5AAD8071D595DCDB11F3FFA358F1386B0B464EEA331F908B6D24C958929CEDA97721FF31ACD65FD0E5A7BE03F125D85E2E8F05494B23F8F432D80776B3BD6F6E59BC435CCFC8B5AF72924CCBFB643C79BA6878AABD72C37140F8C885F65C5B90A1FB49A1B59C9E7A58089B88B0025F72421144B5D5070816B5F83FF4BA904632A34BCBAD97C1AFB99BCFA4265D854F595EAD38F0462B823292FFD0BE26035D3D532A2A9691A8F8A51418E358C4BD7F1168F2EB826DCCC5006DD66D52B1E21E54F1F43FB84A9AB02D26BB9805C523DCD2BB4051F68FAC9538608F4781B51F88648FCB8A781A1B7CC653FDD1A7F1D3A3D8C6A24E5F6CB8E08C2ECE2C2B27B5FD6D56D2B02FDFD6A67EF0E748F4606196CE5AAD8071D595DCDB11F3FFA358F1386B0B464EEA3105CF6D60AA8AF9609D507B6704E03F873593B0C96DF9D3303893494E721213AAD2A120A49A9CF85648E20BD67CE022CFC8B5AF72924CCBFB643C79BA6878AAEC3CEDC11847AE9AF65C5B90A1FB49A13601F0FC651FC2E27A35A070F02FD274D02F4B9FCF4944B5DBF9FCE3257429BF3A65BBE724F0DC575D854F595EAD38F0F3E1A7469CFEBF1826035D3D532A2A96E4091203D2E3097B934D17DEBC2138BA6DCCC5006DD66D52045635BD0A64BF1E2AC8D8CED1B32F13C523DCD2BB4051F68FAC9538608F4781B51F88648FCB8A781A1B7CC653FDD1A7F1D3A3D8C6A24E5F931DD931803EC49827B5FD6D56D2B02FDFD6A67EF0E748F4606196CE5AAD8071D595DCDB11F3FFA358F1386B0B464EEA331F908B6D24C958CBDE66005746484798E82A0C2273F7587721253E7F78029A057CB7091699ED0743E99011C8CFF388CFC8B5AF72924CCBFB643C79BA6878AA853B3615AA1005FAF65C5B90A1FB49A11A38A7D6CEFBDED63B39B74A34F015E08C4EA2E0D45D318A7D62FE29EAC6D70B2E5BBE79A05E77F0882B7AE83DC9A1C83F1786DC23E653A748D32A665A91B3492F075CAB1BE8B037864E7626F382A736A7F5D1EEAA9EB3D0A6D227A5E4CEDB9A561C723F0ED9F2B58F2F132C8EF868C53E191664908A93042D876C84F356E998B1AEAAA23AA72F93BAC9BD110E2689538560A9D691350DC9B7336CA8B67FF7803CA3D31B0569929A9D0D8B66684A92D0A473F429209571DD1F936AF8CE45A5DE46FDEEA24C4BE9280B6E93B9A87E92654C52CF5A0621771781C7117B1F11EC4E51FBFFB4E20777CB5EC511C2EADB6DC275DF2DF2C5033E3BD47B725046AE88EA460E4A3DE06344EEDCDD14F69B288F93D7561CF6343779691B2EB1F00137CB3A79464EDF731B1D298C4EA2E0D45D318A7D62FE29EAC6D70B2E5BBE79A05E77F0882B7AE83DC9A1C8B2EFE96F490A553948D32A665A91B3492F075CAB1BE8B037864E7626F382A736D692607EE482D4B0A6D227A5E4CEDB9A561C723F0ED9F2B58F2F132C8EF868C53E191664908A93042D876C84F356E99878CC7B508992BCF5A5001F21B76EC44E8560A9D691350DC9B7336CA8B67FF7803CA3D31B0569929A9D0D8B66684A92D0A473F429209571DD1F936AF8CE45A5DE295521D47EEC3A6E0B6E93B9A87E926509F26775652298759AD69A7014BA267FD30BFBBB1BF67EA55EC511C2EADB6DC275DF2DF2C5033E3BBE81509D9CA57CB5460E4A3DE06344EE543AE412CB027722654511B853FC809BDA5E57737D5A4FC329F9C35EAE1F3CA67B537E4077F8C084355E19CAF1B7DF9AABA3D73966AC1DB2777A04EDDE5E43DAB5C400EEA60F4356592ABB2C5514873254BBC1F0944640F10BB0CF491E925E25C131BC324CD4D1D33F0CF22AC59799F32C92A619F70FAC1EBFB74BB62CBEC559135279AB190495AB098A1BB252DD2B985613DDE9D9E12A00DE696A135C8730F7D8B8E7AF47E6140B72EF9DF58E9D0647A75526E1608B817E67105ED29C230E74CD3349F0F8955098DB87ADDBE24CA5302FF790E888981AC2A5882B85587F49062FB821A6182B063DC26DDFEBB4CB92E76DA8B139F0A65EB3B1F8D934F42AE349DFC6B1D04B7C2BE91CFCE6AE959116E7B583D16BC83A6A6C8D4660080C861FBB9A7240D085D9537805090253D99AE2C1EE664886352C73883A73ACF31C5D1961D9C9E757C6BC85CBFE2F419A066CAAB8E6E1DBB9C634CDC146EDFC2683D7BB775C07D080EF911CE2DD4E7D7D22D90D8DFB4E8E491FB67B00DA61968CFD7AB71E96F0104308451D1F4EFE4C0C573F0684051C33541A8F83B67C8B7FED7293C85D378D7216ACDF4BC5AED125D1618D0A343650207CF42B3EB1A2EDAF0351D21C77D2330B56DF07085B992DDBDE016A7F2CE5CCE444C0FAFE194EAB6CEA926491512EF49BAC61601D3A6908EDFEFC6ECBC7D413E7656985985F47653D791BEFFE9B77E1997FC0BAFCAF0543E3FEB0CEDF953C2010DCB36970CDF360208BDD1C661A90D151F13DBC9C25")
    url = "https://www.endata.com.cn/API/GetData.ashx"
    data = {
        "year": "2013",
        "MethodName": "BoxOffice_GetYearInfoData"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
    }
    res = requests.post(url, data=data, headers=headers)
    dic = shell(res.text)
    print(dic)
