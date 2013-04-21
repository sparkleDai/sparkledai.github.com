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
                    return splitArrayExtension[len(splitArrayExtension)-2]
def fetchFileExtension(filePath):
    if filePath!="":
        splitArray=filePath.split('.');
        if len(splitArray)<=1:
            return ""
        else:
            return splitArray[len(splitArray)-1]
