# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re
import os


# 目标URL
# <a href="//ww4.sinaimg.cn/large/6cca1403jw1fbatipmvi3j20ev0guq3s.jpg" target="_blank" class="view_img_link">[查看原图]</a>


class Spider:
    def __init__(self):
        self.siteURL = "http://jandan.net/ooxx/"

    # 获取Response
    def getPage(self, pageIndex):
        url = self.siteURL + "page-" + str(pageIndex) + "#comments, pages"
        print(url)
        head = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        request = urllib.request.Request(url, headers=head)
        response = urllib.request.urlopen(request)
        return response.read().decode('utf-8')

    # 获取匹配图片地址
    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile(
            '<a.*?href="(.*?)".*?>.*?',
            re.S)
        items = re.findall(pattern, page)
        print(items)
        contents = []
        for i in items:
            contents.append(i)
        print(contents)
        self.saveImgs(contents)
        return contents

    # 保存多个图片
    def saveImgs(self, images):
        number = 1
        print(u"共有", len(images), u"张照片")

        for imageURL in images:
            if ".jpg" in imageURL:
                splitPath = imageURL.split('.')
                fTail = splitPath.pop()
                if len(fTail) > 3:
                    fTail = "jpg"
                fileName = str(number) + "." + fTail
                self.saveImg(imageURL, fileName)
                number += 1
            elif ".gif" in imageURL:
                splitPath = imageURL.split('.')
                fTail = splitPath.pop()
                if len(fTail) > 3:
                    fTail = "gif"
                fileName = str(number) + "." + fTail
                self.saveImg(imageURL, fileName)
                number += 1
            else:
                continue

    # 保存单张图片
    def saveImg(self, imageURL, fileName):
        imageURL = "http:" + imageURL
        head = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        request = urllib.request.Request(imageURL, headers=head)
        u = urllib.request.urlopen(request)
        data = u.read()
        if not os.path.exists("d:/tempPic"):
            os.makedirs("d:/tempPic")
        f = open("d:/tempPic/" + fileName, 'wb')
        f.write(data)
        print(u"正在保存图片", fileName, u"", imageURL)
        f.close()

spider = Spider()
spider.getContents(341)