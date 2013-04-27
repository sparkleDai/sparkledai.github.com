# -*- coding: GBK -*-
articlePath_ = "..\\article\\origin\\UbuntuKylin下安装配置LAMP.txt"
articleListPath_="..\\article\\articleList.xml"
htmlDir_ = "..\\article\\html\\"

import sys
sys.path.append("UtilSp\Python")

import os
from fileSp import *
from xmlSp import *

def fetchArticleIdList(artilceListPath):
    articleListXml=xmlSp()   
    xmlTree=articleListXml.fetchXmlNodeTree(artilceListPath)
    idList=articleListXml.fetchNodeValueList(xmlTree,'id')
    return idList

def fetchLastArticleId(artilceListPath):
    articleIdList=fetchArticleIdList(artilceListPath)
    if articleIdList==None or len(articleIdList)<=0 or articleIdList=="":
        return 10001
    else:
       idCount=len(articleIdList)     
       lastId=int(articleIdList[idCount-1])
       return lastId

def outHtml():
    articleName=fetchFileName(articlePath_,False)
    lastId=fetchLastArticleId(articleListPath_)
    newId=lastId+1;
    htmlName=str(newId)+'.txt'
    htmlPath=htmlDir_+htmlName
    articleFile = open(articlePath_,"r")
    htmlFile = open(htmlPath,"w")
    htmlFile.write("<h3>")
    htmlFile.write(articleName)
    htmlFile.write("</h3>\n")
    for line in articleFile:    
        htmlFile.write("<div>\n")
        htmlFile.write("\t<p>\n")  
        line=line.strip('\n')#Remove charater of line break
        htmlFile.write("\t" + line+"\n")  
        htmlFile.write("\t</p>\n")
        htmlFile.write("</div>\n")
    articleFile.close()
    htmlFile.close();
    outParam={}
    outParam['htmlPath']=htmlPath
    outParam['articldId']=newId
    outParam['articldName']=articleName
    return outParam

def updateArticleList(articleId,articleName):
    articleListXml = xmlSp()  
    nodeTree = articleListXml.fetchXmlNodeTree(articleListPath_)
    rootNode=articleListXml.fetchSingleNode(nodeTree,'articleList')
    idNode=articleListXml.createChildNode('id',str(articleId))
    nameNode=articleListXml.createChildNode('name',str(articleName))
    parentNode=articleListXml.createChildNode('article','')
    articleListXml.addNode(parentNode,idNode)
    articleListXml.addNode(parentNode,nameNode)
    articleListXml.addNode(rootNode,parentNode)
    articleListXml.writeXml(nodeTree,articleListPath_)

if __name__ == '__main__': 
    outParam=outHtml()
    print(articlePath_+" convert to "+outParam['htmlPath']+" OK!")
    updateArticleList(outParam['articldId'],outParam['articldName'])
    os.system("PAUSE")

