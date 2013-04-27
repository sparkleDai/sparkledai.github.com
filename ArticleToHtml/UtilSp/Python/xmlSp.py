#-*- coding:utf-8 -*-

from xml.etree import ElementTree
from xml.etree.ElementTree import Element 

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
          return  ElementTree.parse(xmlPathOrXmlStr)#is xmlStr
        else:
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
  
    def modifyNodeValue(self,node,newValue, isAppend=False):
            if(node==None):
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
        try:
            nodeTree.write(outPath, encoding=charset)
            return True
        except:
            return False
    
#if __name__ == '__main__':  
#    myxml = xmlSp()   
#    xmlPath= "..\\article\\articleList.xml";
#    nodeTree = myxml.fetchXmlNodeTree(xmlPath)
#    #nodeTree=
#    #myxml.fetchXmlNodeTree("<artilceList><article><id>aaaa</id></article></artilceList>")
#    #node=myxml.fetchSingleNode(nodeTree,'article/id')
#    #if len(node)<=0:
#    #    print("empty")
#    #print(node)
#    #nodeList = myxml.fetchNodeList(nodeTree,'id')
#    #myxml.modifyNodeValue(nodeList[0],'bbbb')
#    #myxml.writeXml(nodeTree,xmlPath)
#    #rootNode=myxml.fetchSingleNode(nodeTree,'articleList')
#    #idNode=myxml.createChildNode('id','aaabbbb')
#    #nameNode=myxml.createChildNode('name','aaabbbb')
#    #parentNode=myxml.createChildNode('article','')
#    #myxml.addNode(parentNode,idNode)
#    #myxml.addNode(parentNode,nameNode)
#    #myxml.addNode(rootNode,parentNode)
#    #myxml.writeXml(nodeTree,'aaa.xml')
#    #for node in nodeList:
#    #    print("node:%s" %node)
#    #nodeValueSet=fetchNodeValueSet(nodeTree,'article/id')
#    #for nodeValue in nodeValueSet:
#    #    print ("nodeValue:%s" %nodeValue)
#import os
#os.system("PAUSE")
