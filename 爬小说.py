# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

'''
爬小说1.1
爬取笔趣阁小说网的特定小说
'''
# 将URL页面下的小说追加到f指向的文件中
def reptile(url,f):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read())
    # 获取本章名
    booknameList = bsObj.findAll("h1")
    # 获取本章内容
    fictionList = bsObj.findAll("div", id="content")
    for bookname in booknameList:
        f.write(bookname.get_text()+"\n\n")
    for fiction in fictionList:
        f.write(fiction.__str__().replace('<br/>','\n').replace('<div id="content">', '').replace('</div>', ''))


# 返回传入URL的下一页的URL
def getNextUrl(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, 'html.parser')
    nextUrl = bsObj.findAll("div", {"class": "bottem1"})[0].findAll("a")[3]
    return nextUrl.__str__().replace('<a href=\"', '').replace('\">下一章</a>', '')


if __name__ == "__main__":
    #定义起始时间
    startTime = time.time()
    # 定义起始URL
    url = "https://www.biquge.info/0_383/9154805.html"
    # 定义结束URL
    endUrl = "https://www.biquge.info/0_383/14305530.html"
    # 定义文件URL
    fileUrl = "C://Users/Catchen/Desktop/元尊.txt"
    # 初始化计数器
    counter = 1
    # 打开文件
    f = open(fileUrl, "a", encoding='utf-8')
    while url != endUrl:
        # 将当前URL的小说追加到文件中
        reptile(url, f)
        # 获取下一个URL
        url = getNextUrl(url)
        print("已经保存"+str(counter)+ "章，已用时：" + str(int(time.time()-startTime))+"S")
        counter += 1
    f.close()
    input("程序结束，请按任意键退出。")