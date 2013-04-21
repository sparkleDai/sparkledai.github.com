import os

sourcePath_ = "test.txt"
null=""

def intToStr(str):
    try:
        i = int(str)
        return i
    except ValueError:
        return null
    except:
        return null


def fetchLineNo(str):    
        lineNo = intToStr(str[0])
        if lineNo != null:
            if lineNo > 0:
                return lineNo
        else:
            return null

def removeLineNo(sourcePath):
        if os.path.isfile(sourcePath):
           fileRead = open(sourcePath,"r")
           content = []
           for line in fileRead:            
               lineNo=fetchLineNo(line)
               print(lineNo)
               outputLine=line
               if lineNo != null:
                   if lineNo > 0:                       
                       outputLine=line[len(str(lineNo)):]                       
               content.append(outputLine)
           fileRead.close()
           fileWrite = open(sourcePath,"w")
           try:
               for output in content:                
                   fileWrite.write(output)
           finally:
               fileWrite.close()
removeLineNo(sourcePath_)

os.system("PAUSE")
       
