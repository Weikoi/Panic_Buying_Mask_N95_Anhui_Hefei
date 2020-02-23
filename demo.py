from urllib.request import quote, unquote

## 注意不要去掉引号
name = "你的名字填在这里"
cardNo = "你的身份证号码填在这里"
phone = "你的电话号码填在这里"

name = quote(name, safe=";/?:@&=+$,", encoding="utf-8")  # 编码

url = "http://kzgm.bbshjz.cn:8000/ncms/mask/book-view?pharmacyCode=5717&pharmacyName=%E9%82%BB%E5%8A%A0%E5%8C%BB%E5%BA%B7%E5%A4%8D%E6%95%A3%E5%85%B5%E5%BA%97&name=" + name + "&cardNo=" + cardNo + "&phone=" + phone + "&reservationNumber=5&pharmacyPhase=&from=groupmessage"

print(url)

# res2 = unquote(res1, encoding='utf-8')  # 解码


# 实验提交Post，验证码无法绕过
# url = "http://xxxxxxxx"
#
# params = {"phone":phone,"name":name}
# params = urllib.urlencode(params)
#
# req_header = {"User-Agent":"Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255"}
# req = urllib2.Request(url,params,req_header)
# res = urllib2.urlopen(req)
# res = res.read()
