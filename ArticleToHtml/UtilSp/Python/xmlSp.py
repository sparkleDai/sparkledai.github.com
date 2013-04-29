#-*- coding:utf-8 -*-

from xml.etree import ElementTree
from xml.etree.ElementTree import Element 

_exception = None

import os
class xmlSp:   
    def addNode(self,parentNode,childNode):       
            parentNode.append(childNode)      
    
    def createChildNode(self,key,value,propertyMap={}):
        element = Element(key,propertyMap)  
        element.text = value 
        return element

    def fetchXmlNodeTree(self,xmlPathOrXmlStr):#Load xml has 2 ways.First:load xml string.Second:load xml file.  
        if(xmlPathOrXmlStr == ""):
          return None
        elif(os.path.isfile(xmlPathOrXmlStr)):#is xmlPath
          return  ElementTree.parse(xmlPathOrXmlStr)
        else:#is xmlStr
          return ElementTree.fromstring(xmlPathOrXmlStr)      

    def fetchSingleNode(self,nodeTree,xpathOrKey):#If the node that is same name is more,return first node. 
        if xpathOrKey == None or xpathOrKey == "":
            return None
        elif len(xpathOrKey.split('/')) > 1:#is xpath        
            return nodeTree.find(xpathOrKey)#find is faster than findall then return first
        else:#is key
            nodeList = nodeTree.getiterator(xpathOrKey)
            if nodeList == None or len(nodeList) <= 0:
                return nodeList
            else:
                return nodeList[0]

    def fetchSingleNodeValue(self,nodeTree,xpathOrKey):#If the node that is same name is more,return first node.   
        node = self.fetchSingleNode(nodeTree,xpathOrKey)
        if node == None or len(node) <= 0 or node == "":
            return ""
        else:
            return node.text

    def fetchNodeList(self,nodeTree,xpathOrKey):
        if xpathOrKey == None or xpathOrKey == "":
            return None
        elif len(xpathOrKey.split('/')) > 1:#is xpath
            return nodeTree.findall(xpathOrKey)
        else:#is key
            return  nodeTree.getiterator(xpathOrKey)

    def fetchNodeValueList(self,nodeTree,xpathOrKey,key=""):#If xpathOrKey is xpath,key must be not empty.Otherwise return empty set    
        if xpathOrKey == None or xpathOrKey == "":
            return None
        else:
            nodeValueList = []                                  
            nodeList = self.fetchNodeList(nodeTree,xpathOrKey)
            for node in nodeList:
                    if node.tag == xpathOrKey:
                        nodeValueList.append(node.text)
            return nodeValueList 

    def format(self,sourceXmlPath,destXmlPath,charset='UTF-8'):    
            global _exception  
            _exception = None
            if os.path.exists(sourceXmlPath):
                try:
                    fileRead = open(sourceXmlPath,'r',encoding=charset)
                    fileWrite = open(destXmlPath,'w',encoding=charset)                  
                    lines = fileRead.read()    
                    nodeList=[]                
                    self.__writeXmlStruct(lines,nodeList,fileWrite)                    
                    fileRead.close()
                    fileWrite.close()                   
                    return True
                except BaseException as error:
                    _exception = error
                    return False
            else:
                _exception = BaseException('File not exist!')
                return False
    def __writeXmlStruct(self,xmlStr,nodeList,fileWrite): 
        xmlStr=xmlStr.replace('\n','') 
        xmlStruct1=self.__analyNodeFlag(xmlStr)       
        if xmlStruct1!=None:
            xmlNode1=xmlStruct1[0]
            xmlRestStr1=xmlStruct1[1]
            xmlStruct2=self.__analyNodeFlag(xmlRestStr1)
            xmlNode2=xmlStruct2[0]
            xmlRestStr2=xmlStruct2[1]
            xmlInnerTextEnd=xmlRestStr1.find(xmlNode2)
            xmlInnerText=xmlRestStr1[:xmlInnerTextEnd]
            isPair=self.__checkNodeFlagIsPair(xmlNode1,xmlNode2)
            nodeName1=self.__fetchNodeNameFromStr(xmlNode1)
            nodeName2=self.__fetchNodeNameFromStr(xmlNode2)
            if not (nodeName1 in nodeList):
                nodeList.append(nodeName1)
            if not (nodeName2 in nodeList):
                nodeList.append(nodeName2)
            nodeName1Floor=nodeList.index(nodeName1,0)
            nodeName2Floor=nodeList.index(nodeName2,0)            
            space=''
            if len(xmlNode1)>0:    
                if isPair:
                    for  index in range(nodeName1Floor):
                        xmlNode1=space+xmlNode1           
                fileWrite.write(xmlNode1+'\n')   
                if len(xmlInnerText)>0:
                    if isPair:
                        for  index in range(nodeName1Floor+1):
                            xmlInnerText=space+xmlInnerText
                    fileWrite.write(xmlInnerText+'\n')
                if len(xmlNode2)>0:                     
                    for  index in range(nodeName2Floor):
                        xmlNode2=space+xmlNode2
                    fileWrite.write(xmlNode2+'\n')        
                self.__writeXmlStruct(xmlRestStr2,nodeList,fileWrite)           
    def __analyNodeFlag(self,sourceStr): 
        global _exception
        _exception=None
        try:           
            nodeBegin = sourceStr.find('<')           
            nodeEnd = str(sourceStr).find('>')                        
            if nodeBegin >= 0 and nodeEnd > 0:
                node =sourceStr[nodeBegin:nodeEnd+1]       
                nodeInnerText=sourceStr[nodeEnd+1:]
                return [node,nodeInnerText]
            else:
                return ["",sourceStr]
        except BaseException as error:
            _exception=error
            return None
    def __checkNodeFlagIsPair(self,nodeFlag1,nodeFlag2):
        if len(nodeFlag1)>0 and len(nodeFlag2)>0:
            nodeFlag1=nodeFlag1[1:(len(nodeFlag1)-2)]
            nodeFlag2=nodeFlag2[1:(len(nodeFlag2)-2)]
            nodeFlag1=nodeFlag1.replace('/','')
            nodeFlag2=nodeFlag2.replace('/','')
            if nodeFlag1==nodeFlag2:
                return True               
        return False

    def __fetchNodeNameFromStr(self,str):
            str=str[1:(len(str)-1)]
            nodeName=str.replace('/','')
            return nodeName
  
    def modifyNodeValue(self,node,newValue, isAppend=False):
            if(node == None):
                return False
            else:
                try:
                    if isAppend:  
                        node.text += newValue 
                    else:  
                        node.text = newValue 
                    return True 
                except:
                    return False

    def writeXml(self,nodeTree, outPath,charset="utf-8"): 
        global _exception
        _exception=None
        try:
            nodeTree.write(outPath, encoding=charset)
            return True
        except BaseException as error:
            _exception=error
            return False

#import os   
#if __name__ == '__main__':  
#    myxml = xmlSp()   
#    formatResult = myxml.format("1.txt","2.txt")
#    if not formatResult:
#        print(_exception)
#    else:
#        os.remove("1.txt")
#        os.rename('2.txt','1.txt')
    
##    xmlPath= "..\\article\\articleList.xml";
##    nodeTree = myxml.fetchXmlNodeTree(xmlPath)
##    #nodeTree=
##    #myxml.fetchXmlNodeTree("<artilceList><article><id>aaaa</id></article></artilceList>")
##    #node=myxml.fetchSingleNode(nodeTree,'article/id')
##    #if len(node)<=0:
##    # print("empty")
##    #print(node)
##    #nodeList = myxml.fetchNodeList(nodeTree,'id')
##    #myxml.modifyNodeValue(nodeList[0],'bbbb')
##    #myxml.writeXml(nodeTree,xmlPath)
##    #rootNode=myxml.fetchSingleNode(nodeTree,'articleList')
##    #idNode=myxml.createChildNode('id','aaabbbb')
##    #nameNode=myxml.createChildNode('name','aaabbbb')
##    #parentNode=myxml.createChildNode('article','')
##    #myxml.addNode(parentNode,idNode)
##    #myxml.addNode(parentNode,nameNode)
##    #myxml.addNode(rootNode,parentNode)
##    #myxml.writeXml(nodeTree,'aaa.xml')
##    #for node in nodeList:
##    # print("node:%s" %node)
##    #nodeValueSet=fetchNodeValueSet(nodeTree,'article/id')
##    #for nodeValue in nodeValueSet:
##    # print ("nodeValue:%s" %nodeValue)
#import os
#os.system("PAUSE")
