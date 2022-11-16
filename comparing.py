import pandas as pd
import threading
import time
import multiprocessing as mp

# kodun yazılacagı yer


# get Data
allData = pd.read_csv(r"C:\Users\ASUS Pc\Desktop\VSCodeProject\yazlab12\clean_data.csv", encoding='latin1')
allData=allData.head(100)
# allData = pd.read_csv(r"C:\Users\ASUS Pc\Desktop\VSCodeProject\yazlab12\deneme.csv", encoding='utf8')

def compareAlgorithm(pieceRoot, pieceTarget):

    maxLength = len(pieceRoot)

    if len(pieceTarget) > len(pieceRoot):
        maxLength = len(pieceTarget)
    
    sameCount = 0

    for rootItem in pieceRoot:

        for targetItem in pieceTarget:
            
            if rootItem.strip().lower() == targetItem.strip().lower():
                sameCount = sameCount + 1 
    
    result = (sameCount / maxLength) * 100
    if result > 100:
        result = 100
    return result

def compareOfCol(indexArea, sayi, divison, list1,list2,list3):
    complaintId = ""
    spesifik = ""
    if list1[0] != "nothing":
        if len(list1)>1:
            complaintId = list1[1].strip()
        spesifik = list1[0].strip().split(' ')[1]
    
    rootCompareDatas = list2
    showingCompareDatas = list3

    # complaint Id olan özel Durum
    if len(complaintId)!=0:

        for i in range(indexArea-divison, indexArea):

            mainData = allData.iloc[i]
            
            if mainData["Complaint ID"].strip() == complaintId.strip():

                for item in rootCompareDatas:
                    rootData = mainData[item]
                    pieceOfRootData = rootData.strip().split(' ')

                    for j in range(len(allData)):
                        
                        if i!=j:
                            testData = allData.iloc[j]
                            targetData = testData[item]
                            pieceOfTargetData = targetData.strip().split(' ')
                            
                            rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)

                            for show in showingCompareDatas:
                                showData = testData[show]
                                print(f"RootData : {rootData} | TargetData: {targetData} | Rate:{rate} | ShowData {showData}")
                                print('-'*100)

    # genel Durum
    else:
        for i in range(indexArea-divison, indexArea):
            mainData = allData.iloc[i]

            for item in rootCompareDatas:
                rootData = mainData[item]
                pieceOfRootData = rootData.strip().split(' ')

                for j in range(len(allData)):

                    if j!=i:
                        testData = allData.iloc[j]

                        if len(spesifik)>0:
                            if mainData[spesifik].strip() == testData[spesifik].strip():
                                targetData = testData[item]
                                pieceOfTargetData = targetData.strip().split(' ')
                                rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)
                        else:
                            targetData = testData[item]
                            pieceOfTargetData = targetData.strip().split(' ')
                            rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)
                        
                        for show in showingCompareDatas:
                                showData = testData[show]
                                print(f"RootData : {rootData} | TargetData: {targetData} | Rate:{rate} | ShowData: {showData}")
                                print('-'*100)
                     
def setProcessIndex(threadCount, list1, list2, list3):
    
    selectedData = allData
        

    divison = int(len(selectedData) / threadCount)
    
    pieceValues = []
    temp = divison
    
    while True:
        if temp > len(selectedData):
            break
        
        pieceValues.append(int(temp))
        temp += divison
          
    # gerekli threadler buraya yuklenecek
    processes = []
    

    for i in range(threadCount):
        processes.append(mp.Process(target=compareOfCol, args=(pieceValues[i], i, divison, list1,list2,list3,)))
    
    for process in processes:
        
        process.start()
        

        

if __name__ == "__main__": 
    setProcessIndex(4, ['Aynı Product'],['Issue','Product'],['Company'])  




        






