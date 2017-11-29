#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chris
#
# Created:     27-11-2017
# Copyright:   (c) chris 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    #print test_getMissingKeys()
    #print test_GetMissingKeysWithCount()
    #print test_getUnique()
    print test_flattenList()
def getMissingKeys(dictRef,dictToCompare):
    missing_keys=[]
    for key in dictRef.keys():
        if dictToCompare.has_key(key)==False:
            missing_keys.append(key)
    return missing_keys

def getMissingKeysWithCount(dictRef,dictToCompare):
    count=0
    missing_keys=[]
    for key in dictRef.keys():
        if dictToCompare.has_key(key)==False:
            missing_keys.append(key)
            count+=1
    final_tuple=(count,missing_keys)
    return final_tuple

def getUnique(inList):
    uniquelist=[]
    for item in inList:
        if inList.count(item)>1:
            while inList.count(item)>1:
                inList.remove(item)
            uniquelist.append(item)
        else:
            uniquelist.append(item)
    return uniquelist

def flattenList(inList):
    flat_list=[]
    for item in inList:
        if type(item)==list:
            for inner_list_item in item:
                flat_list.append(inner_list_item)
        if type(item)==tuple:
            for item_in_tuple in item:
                flat_list.append(item_in_tuple)
        if type(item)!=list and type(item)!=tuple:
            flat_list.append(item)
    return flat_list
def test_getMissingKeys():
    test_dict_good={1:1,2:2,3:3}
    test_dict_false={'help':1,'python':2,'is':3,'difficult':3}
    return getMissingKeys(test_dict_good,test_dict_good)
    return getMissingKeys(test_dict_good,test_dict_false)
def test_GetMissingKeysWithCount():
    test_dict_good={1:1,2:2,3:3}
    test_dict_false={'help':1,'python':2,'is':3,'difficult':3}
    return getMissingKeysWithCount(test_dict_good,test_dict_false)
    return getMissingKeysWithCount(test_dict_false,test_dict_false)
def test_getUnique():
    t=[1,1,2,3,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
    return getUnique(t)
def test_flattenList():
    t=[1,[2,3],4,(5,6)]
    return flattenList(t)
if __name__ == '__main__':
    main()
