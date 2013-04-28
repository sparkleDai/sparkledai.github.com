def fetchFileName(filePath,withExtension=True):
    if filePath!="":
        splitArrayFileName=filePath.split('\\')
        if len(splitArrayFileName)<=0:
            return ""
        else:
            fileName=splitArrayFileName[len(splitArrayFileName)-1]
            if  withExtension:
                return fileName
            else:
                splitArrayExtension=fileName.split('.');
                if len(splitArrayExtension)<=1:
                    return ""
                else:    
                    extension=fetchFileExtension(fileName)
                    fileNameNoExt=fileName.split('.'+extension)[0]   
                    return  fileNameNoExt        
                   
def fetchFileExtension(filePath):
    if filePath!="":
        splitArray=filePath.split('.');
        if len(splitArray)<=1:
            return ""
        else:
            return splitArray[len(splitArray)-1]
