function GetNodeList(xmlDocOrNode, tagName) {
    var nodeList = null;
    try {
        if (xmlDocOrNode !== null) {
            nodeList = xmlDocOrNode.getElementsByTagName(tagName);
        }

    } catch (e) {
        nodeList = null;
    }
    return nodeList;
}

function GetNodeValue(node, nodeIndex) {
    var nodeValue = null;
    try {
        nodeValue = node.childNodes[nodeIndex].nodeValue;
    } catch (e) {
        nodeValue = null;
    }
    return nodeValue;
}


function loadXMLDoc(xmlFile) {
    var xmlDoc = null;
    try //Internet Explorer
    {
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
    }
    catch (e) {

    }
    try //Firefox, Mozilla, Opera, etc.
        {
        xmlDoc = document.implementation.createDocument("", "", null);
        xmlDoc.async = false;
        xmlDoc.load(xmlFile);
    }
    catch (e) { //Chrome
        var xmlhttp = new window.XMLHttpRequest();
        xmlhttp.open("GET", xmlFile, false);
        //xmlhttp.open("POST", xmlFile, false
        xmlhttp.send(null);
        xmlDoc = xmlhttp.responseXML.documentElement; //一定要有根节点(否则google浏览器读取不了)
        //alert(e.Message);
    }
    return xmlDoc;
}

function LoadXmlString(xmlString) {
    var xmlDoc = null;
    try //Internet Explorer
    {
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async = "false";
        xmlDoc.loadXML(xmlString);
    }
    catch (e) {
        try //Firefox, Mozilla, Opera, etc.
        {
            parser = new DOMParser();
            xmlDoc = parser.parseFromString(xmlString, "text/xml");
        }
        catch (e) {
            alert(e.message);
        }
    }
    return xmlDoc;
}

////检测系统支持的XMLDom方式
//function E_getControlPrefix() {
//    var prefixes = ["MSXML2", "Microsoft", "MSXML", "MSXML3"];
//    var o, o2;
//    for (var i = 0; i < prefixes.length; i++) {
//        try {
//            // try to create the objects
//            o = new ActiveXObject(prefixes[i] + ".XmlHttp");
//            o2 = new ActiveXObject(prefixes[i] + ".XmlDom");
//            return E_getControlPrefix.prefix = prefixes[i];
//        }
//        catch (ex) { };
//    }
//}
////创建xmldom对象
//function loadXMLDoc(xmlFile) {
//    var xmlDom = null;
//    if (window.ActiveXObject) {       //支持IE浏览器，可跨域
//        xmlDom = new ActiveXObject(E_getControlPrefix() + ".XMLDOM");
//        //xmlDom.loadXML(xmlFile);//如果用的是XML字符串
//        xmlDom.load(xmlFile); //如果用的是xml文件。
//    } else if (document.implementation && document.implementation.createDocument) {   //支持火狐浏览器，可跨域
//        xmlDom = document.implementation.createDocument("", "", null);
//        xmlDom.load(xmlFile);
//    } else if (window.XMLHttpRequest) {       //xmlhttp方式，支持火狐、chrome、oprea等浏览器，但不可跨域
//        var xmlhttp = new window.XMLHttpRequest();
//        xmlhttp.open("GET", xmlFile, false);
//        xmlhttp.send(null);
//        if (xmlhttp.status === 200) {
//            xmlDom = xmlhttp.responseXML;
//        }
//    } else {
//        xmlDom = null;
//    }
//    return xmlDom;
//}

function ReadTxtFile(url,charset) {
    var xmlHttp;
    var rs;
    var isie = false;
    var content = "";
    if (window.ActiveXObject) {
        xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
        isie = true;
    } else if (window.XMLHttpRequest) {
        xmlHttp = new XMLHttpRequest();
    }
    try {
        if (isie === false) {
            xmlHttp.open("GET", url, false);
            if (charset === undefined || charset === null) {
                charset = "utf-8";
            }
            xmlHttp.overrideMimeType("text/html;charset="+charset);
            xmlHttp.send(null);
            content = xmlHttp.responseText;
        } else {
            xmlHttp.open("GET", url, false);
            xmlHttp.send(null);
            if (xmlHttp.readyState === 4) {
                if (xmlHttp.status === 200 || xmlHttp.status === 0) {
                    content = Recenspace(xmlHttp.responseBody);
                }
            }
        }
    } catch (exception) {
        //document.write('exception:' + exception.message);
        content = exception.message
    }
    //alert(content);
    return content;
}
function Recenspace(Html) {
    rs = new ActiveXObject("ADODB.RecordSet");
    rs.fields.append("a", 201, 1);
    rs.open();
    rs.addNew();
    rs(0).appendChunk(Html);
    rs.update();
    return rs(0).value;
    rs.close();
}