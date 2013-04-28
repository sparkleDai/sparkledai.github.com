_exception=None
def getException():
    global _exception
    return _exception


def twoListToDict(list1,list2):
    global _exception
    _exception=None
    try:
        if len(list1)==len(list2):
            dict={}
            for index in range(len(list1)):
                dict[str(list1[index])]=list2[index]
            return dict
        elif len(list1)!=len(list2):        
            _exception=BaseException("Length is not equal")           
            return None
        else:
            _exception=BaseException("Unknown error")  
            return None
    except BaseException as error:
        _exception=error
        return None

#import os
#if __name__=='__main__':
#    list1=['a','b','c','d','e','f','e']  
#    list2=[1,2,3,4,5,6,7]
#    #list1=sorted(list1)
#    #list2=sorted(list2)
#    dict=twoListToDict(list1,list2)
#    if dict==None:
#        exception=getException()
#        print(str(exception))
#    else:
#        print(dict)
#        dict2=sorted(dict.items(),key=lambda item:item[0],reverse=False)
#        print(dict2)
#    os.system('pause')