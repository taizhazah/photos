import requests
import os
# 进行数据爬取
def getPages(kw,num):
    # 循环页码数和请求参数
    params = []
    for i in range(30,30*num+30,30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': ' rj',
            'ct': '201326592',
            'is': ' ',
            'fp': 'result',
            #关键词
            'queryWord': kw,
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': ' ',
            'st': '-1',
            'z': ' ',
            'ic': ' ',
            'hd': ' ',
            'latest': ' ',
            'copyright': ' ',
            #关键词
            'word': kw,
            's': ' ',
            'se': ' ',
            'tab': ' ',
            'width': ' ',
            'height': ' ',
            'face': ' ',
            'istype': '2',
            'qc': ' ',
            'nc': '1',
            'fr': ' ',
            'expermode': ' ',
            'force': ' ',
            'cg': 'girl',
            # i的
            'pn': i,
            'rn': '30',
            'gsm': ' ',
            '1575710003840': ' ',
        })

    # 请求的url
    url = 'https://image.baidu.com/search/acjson'
    #循环请求
    urls = []
    for i in params:
        # 像每个url发起请求
        res = requests.get(url,params=i)
        # 获取请求的数据，加入urls里面
        urls.append(res.json()['data'])
    return urls
# 下载图片到本地
def downloadImg(datalist,dir):
    # 检测文件夹是否存在
    if not os.path.exists(dir):
        os.mkdir(dir)
    # 循环下载图片数据
    x = 0
    for data in datalist:
        for i in data:
            if i.get('thumbURL') != None:
                print(f'下载图片{i.get("thumbURL")}')
                # 像图片地址发起请求
                imgres = requests.get(i.get("thumbURL"))
                open(f'{dir}/{x}.jpg','wb').write(imgres.content)
                x += 1
# 获取用户输入信息
keyword = input('请输入搜索图片的关键字:')
# 调用函数，进行数据的爬取，可以指定关键字和下载页数（这里设定的100页）
datalist = getPages(keyword,100)
# 调用函数，保存数据  ,可以指定要保存的图片路径
downloadImg(datalist,'./mao')