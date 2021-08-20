import configparser
from configparser import ConfigParser, NoOptionError
import os
fileList = os.listdir('./TestData')
print("文件列表:",fileList)

# ini文件中主要由节，键，值组成，如下
# [Service]
# _meta.type=VP.Parallax.IVisualParityManifestService
# ServiceName=DesktopNewsAnswerCarousel
# PictModelFileName=VisualSystem.VisualParityContext.Chrome.en-us.txt
# 带方括号的[Service]就是节
# 下面的XXX=XXX如ServiceName=DesktopNewsAnswerCarousel就是键=值，ServiceName即键，DesktopNewsAnswerCarousel即值，要靠键来获取值

UrlList = []
BagList = []
Disabled = []

# 实例化一个ConfigParser对象,选择RawConfigParser()是因为读取ini文件的时候以原始字符的形式读,可避免ini中有特殊字符如%的时候抛出configparser.InterpolationSyntaxError异常
target = configparser.RawConfigParser()

for f in fileList:
    print("---------------现在开始读取%s文件---------------------" % f)
    fPath = './'+"TestData/"+f
    print("fPath为:",fPath)
    target.read(fPath,encoding='utf-8')
    # print("读取文件的结果:",target.read(fPath, encoding='utf-8'))
    # 获取ini文件中的所有节，每次循环section的内容没有被清空，而是直接把后一次循环的内容追加到list后面。。。
    sections = target.sections()
    print("%s 中的所有节为:" % f,sections)
    for i in sections:
        if i != "Service":
            try:
                target.get(i, 'UrlParams')
                UrlList.append(target.get(i, 'UrlParams'))
            except NoOptionError:
                UrlList.append("None")
            try:
                target.get(i,'IsDisabled')
                Disabled.append("Disabled")
            except NoOptionError:
                Disabled.append("None")

            BagList.append(target.get(i, 'Bags'))


print("for循环外的sections：",sections)


print("Url数据：",UrlList)
print("Bag数据：",BagList)
print("Disabled数据：",Disabled)
