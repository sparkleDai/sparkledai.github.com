# -*- coding: UTF-8 -*-
articleOriginPath_ = "..\\article\\origin\\"
articleListPath_="..\\article\\articleList.xml"
htmlDir_ = "..\\article\\html\\"

import sys
sys.path.append("UtilSp\Python")

import os
from fileSp import *
from xmlSp import *
from listSp import *

def calculateConverArticleList(articleIdNameDict,articleOriginList):    
    if  articleIdNameDict!=None:
        waitConvertArticleList=[] 
        for articleOrigin in articleOriginList:
            articleOriginName=fetchFileName(articleOrigin,False)
            hasExistInList=False
            id=10001 
            while str(id) in articleIdNameDict.keys():
                articleName=articleIdNameDict[str(id)] 
                if articleName==articleOriginName:                    
                    hasExistInList=True                    
                    break;               
                id+=1
            if hasExistInList:
                continue
            else:
                if not (articleOrigin in waitConvertArticleList):
                    waitConvertArticleList.append(articleOriginName)   
        lastArticleId=10001+len(articleIdNameDict)-1         
        return [lastArticleId,waitConvertArticleList]
    else:
        return None

def fetchArticleOriginList(articleOriginPath):
    filenameList=os.listdir(articleOriginPath)
    return filenameList

def fetchArticleIdList(artilceListPath):
    articleListXml=xmlSp()   
    xmlTree=articleListXml.fetchXmlNodeTree(artilceListPath)
    idList=articleListXml.fetchNodeValueList(xmlTree,'id')
    return idList

def fetchArticleIdNameDict(artilceListPath):
    articleListXml=xmlSp()   
    xmlTree=articleListXml.fetchXmlNodeTree(artilceListPath)
    idList=articleListXml.fetchNodeValueList(xmlTree,'id')
    nameList=articleListXml.fetchNodeValueList(xmlTree,'name')
    idNameDict=twoListToDict(idList,nameList)
    return idNameDict

def fetchLastArticleId(artilceListPath):
    articleIdList=fetchArticleIdList(artilceListPath)
    if articleIdList==None or len(articleIdList)<=0 or articleIdList=="":
        return 10001
    else:
       idCount=len(articleIdList)     
       lastId=int(articleIdList[idCount-1])
       return lastId

def outHtml(newId,convertArticleName):    
    #lastId=fetchLastArticleId(articleListPath_)
    #newId=lastId+1;   
    htmlName=str(newId)+'.txt'
    htmlPath=htmlDir_+htmlName
    articleOriginPath=articleOriginPath_+convertArticleName
    if not os.path.isfile(articleOriginPath):
        print(convertArticleName+' is not file')
        return
    articleFile = open(articleOriginPath,"r")
    htmlFile = open(htmlPath,"w")
    htmlFile.write("<h3>")
    htmlFile.write(convertArticleName)
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
    outParam['articldName']=convertArticleName
    return outParam

def outHtmlBatch():   
    articleIdNameDict=fetchArticleIdNameDict(articleListPath_)
    articleOriginList=fetchArticleOriginList(articleOriginPath_) 
    waitConvert=calculateConverArticleList(articleIdNameDict,articleOriginList)
    if waitConvert!=None:
        lastId=waitConvert[0]
        convertArticleList=waitConvert[1]
        #print(convertArticleList)
        if  len(convertArticleList)>0:
            newId=lastId+1
            newArticleIdList=[]
            for articleName in convertArticleList:                
                outHtml(newId,articleName+".txt")
                newArticleIdList.append(newId)                
                newId+=1
            updateArticleList(newArticleIdList,convertArticleList)                


def updateArticleList(articleIdList,articleNameList):
    articleListXml = xmlSp()  
    nodeTree = articleListXml.fetchXmlNodeTree(articleListPath_)
    rootNode=articleListXml.fetchSingleNode(nodeTree,'articleList')
    for index in range(len(articleIdList)):
        articleId=articleIdList[index]
        articleName=articleNameList[index]
        idNode=articleListXml.createChildNode('id',str(articleId))
        nameNode=articleListXml.createChildNode('name',str(articleName))
        parentNode=articleListXml.createChildNode('article','')
        articleListXml.addNode(parentNode,idNode)
        articleListXml.addNode(parentNode,nameNode)
        articleListXml.addNode(rootNode,parentNode)
        articleListXml.writeXml(nodeTree,articleListPath_)
    #tempPath="temp.xml"
    #formatResult=articleListXml.format(articleListPath_,tempPath)    
    #if not formatResult:
    #    print(str(articleListXml._exception))
    #else:
    #    os.remove(articleListPath_)
    #    os.rename(tempPath,articleListPath_)


if __name__ == '__main__': 
    try:
        #convertArticleName=input("Please input article name that want to convert...\n")
        outHtmlBatch()  
        #print(articleOriginPath_+" convert to "+outParam['htmlPath']+" OK!")
        #updateArticleList(outParam['articldId'],outParam['articldName'])
    except BaseException as error:
        print(str(error))
    finally:
        os.system("PAUSE")

