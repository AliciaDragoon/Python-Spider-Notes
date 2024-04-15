import requests

# url = "https://www.pearvideo.com/videoStatus.jsp?contId=1713901&mrd=0.9222128598839587"  # mrd是个随机值
# url = "https://www.pearvideo.com/videoStatus.jsp?contId=1713901"
while 1:
    # mainUrl = "https://www.pearvideo.com/video_1713901"
    mainUrl = input("请输入您要下载的梨视频的视频链接：")
    contId = mainUrl.split("_")[-1]
    # print(contId)
    url = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}"
    headers = {
        "Referer": mainUrl,  # 处理防盗链
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
            "Safari/537.36 Edg/120.0.0.0",
    }
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    dic = resp.json()
    # print(dic)
    srcUrl = dic['videoInfo']['videos']['srcUrl']
    # print(srcUrl)
    # "https://video.pearvideo.com/mp4/short/20201229/1703042627677-15551041-hd.mp4" 返回的假地址
    # "https://video.pearvideo.com/mp4/short/20201229/cont-1713901-15551041-hd.mp4" 控制台里的真地址
    systemTime = dic['systemTime']
    # print(systemTime)
    srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
    # print(srcUrl)  # 获取真实的下载地址
    print("正在下载中......")
    resp = requests.get(srcUrl, headers=headers)
    with open(f"{contId}.mp4", mode= "wb") as f:
        f.write(resp.content)
    print("下载成功")
