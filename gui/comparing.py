import pandas as pd
import threading
import time
import multiprocessing as mp

# kodun yazılacagı yer

# get Data
allData = pd.read_csv(r"C:\Users\ASUS Pc\Desktop\VSCodeProject\yazlab12\clean_data.csv", encoding='latin1')

allData=allData.head(50)
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

def compareOfCol(indexArea, sayi, divison, list1,list2,list3,rate_score):
    karsilatirma = 0
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

                

                for j in range(len(allData)):
                    
                    rate_list=[]
                    rootList = []
                    targetList = []
                    flag = False
                    for item in rootCompareDatas:
                        rootData = mainData[item]
                        pieceOfRootData = rootData.strip().split(' ')
                    
                        if i!=j:
                            testData = allData.iloc[j]
                            targetData = testData[item]
                            pieceOfTargetData = targetData.strip().split(' ')
                            
                            rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)
                            rate_list.append(rate)
                            flag = True
                            targetList.append(targetData)
                            rootList.append(rootData)

                    if(flag):
                        for show in showingCompareDatas:
                            showData = testData[show]
                            boolean_value=True
                            for x in rate_list:
                                if(x<rate_score):
                                    boolean_value=False
                                    break
                            if(boolean_value):
                                for index in range(len(rootCompareDatas)):
                                    print(f"Karsilatirma nesnesi : {rootCompareDatas[index]} | RootData : {rootList[index]} | TargetData: {targetList[index]} | Rate:{rate_list[index]} | ShowData {showData}")
                                    
                                print('-'*100)

    # genel Durum
    else:
        for i in range(indexArea-divison, indexArea):
            karsilatirma = karsilatirma +1
            mainData = allData.iloc[i]

            for j in range(len(allData)):
                rate_list=[]
                rootList = []
                targetList = []
                flag = False
                for item in rootCompareDatas:
                    rootData = mainData[item]
                    pieceOfRootData = rootData.strip().split(' ')

                    if j!=i:
                        testData = allData.iloc[j]

                        if len(spesifik)>0:
                            if mainData[spesifik].strip() == testData[spesifik].strip():
                                targetData = testData[item]
                                pieceOfTargetData = targetData.strip().split(' ')
                                rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)
                                rate_list.append(rate)
                                flag = True
                                targetList.append(targetData)
                                rootList.append(rootData)
                        else:
                            targetData = testData[item]
                            pieceOfTargetData = targetData.strip().split(' ')
                            rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)
                            rate_list.append(rate)
                            flag = True
                            targetList.append(targetData)
                            rootList.append(rootData)

                            
                            
                            
                if(flag):
                        for show in showingCompareDatas:
                            showData = testData[show]
                            boolean_value=True
                            for x in rate_list:
                                if(x<rate_score):
                                    boolean_value=False
                                    break
                            if(boolean_value):
                                for index in range(len(rootCompareDatas)):
                                    print(f"{karsilatirma}-) Karsilatirma nesnesi : {rootCompareDatas[index]} | RootData : {rootList[index]} | TargetData: {targetList[index]} | Rate:{rate_list[index]} | ShowData {showData}")
                                    
                                print('-'*100)
                     
def setProcessIndex(threadCount, list1, list2, list3,rate):
    
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
        processes.append(mp.Process(target=compareOfCol, args=(pieceValues[i], i, divison, list1,list2,list3,rate,)))
    
    for process in processes:
        
        process.start()
        
def setThreadIndex(threadCount, list1, list2, list3, rate):
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
    threads = []
    

    for i in range(threadCount):
        threads.append(threading.Thread(target=compareOfCol, args=(pieceValues[i], i, divison, list1,list2,list3,rate,)))
    
    for thread in threads:
        
        thread.start()

def setUltimateProcessIndex(threadCount, list1, list2, list3, rate):
    selectedData = allData

    processCount = 10
    if threadCount<10:
        processCount = threadCount

    divison = int(len(selectedData) / processCount)
    
    pieceValues = []
    temp = divison
    
    while True:
        
        if temp > len(selectedData):
            break
        
        pieceValues.append(int(temp))
        temp += divison
     
    # 10 tane process olusturulucak icersine de threadler yerlestirilicek
    processes = []
    willCrateThreadCount = int(threadCount/processCount)
    remaningThreadCount = threadCount%processCount

    
    
    for i in range(processCount):
        
        if remaningThreadCount != 0:
            processes.append(mp.Process(target=setUltimateThreadIndex, args=(pieceValues[i], i, divison, list1,list2,list3,rate,willCrateThreadCount+1,threadCount)))
            remaningThreadCount = remaningThreadCount - 1
        else :
            processes.append(mp.Process(target=setUltimateThreadIndex, args=(pieceValues[i], i, divison, list1,list2,list3,rate,willCrateThreadCount,threadCount)))

    for process in processes:
        
        process.start()

def setUltimateThreadIndex(indexArea, sayi, divison, list1,list2,list3,rate_score,threadCount, realThreadCount):
    # burası subthread olusturma mantıgını tasıyor
    
    
    # subThreadlere gelecek parcalamalar
    newDivison = int((divison) / threadCount)
    
    pieceValues = []
    temp = newDivison
    
    while True:
        if temp == divison:
            pieceValues.append(int(temp)+(sayi*divison))  
            break

        if temp > divison:
            temp -= newDivison
            pieceValues[-1]+=divison-temp
            break
        
        pieceValues.append(int(temp)+(sayi*divison))
        temp += newDivison
    
    print(f"index area {indexArea} sayi: {sayi} divison {divison} threadCount {threadCount} ")
    print(pieceValues)
    print('*'*100)
    # print(f"index area {indexArea} sayi: {sayi} divison {divison} threadCount {threadCount} ")
    # print('*'*100)
    
    # threadler olustrucam

    threads = []

    for i in range(threadCount):
        threads.append(threading.Thread(target=compareOfCol2, args=(pieceValues[i], i, divison, list1,list2,list3,rate_score,sayi,newDivison)))
    
    for thread in threads:
        thread.start()
    
def compareOfCol2(indexArea, sayi, divison, list1,list2,list3,rate_score, process, newDivison):
    kacinci = 0
    complaintId = ""
    spesifik = ""
    if list1[0] != "nothing":
        if len(list1)>1:
            complaintId = list1[1].strip()
        spesifik = list1[0].strip().split(' ')[1:]
    
    rootCompareDatas = list2
    showingCompareDatas = list3
    
    # baslangic hesabi
    baslangic = (process*divison)+(sayi*newDivison)
    # complaint Id olan özel Durum
    if len(complaintId)!=0:

          
        for i in range(baslangic, indexArea):
            kacinci=kacinci+1
            mainData = allData.iloc[i]
            
            if mainData["Complaint ID"].strip() == complaintId.strip():

                

                for j in range(len(allData)):
                    
                    rate_list=[]
                    rootList = []
                    targetList = []
                    flag = False
                    for item in rootCompareDatas:
                        rootData = mainData[item]
                        pieceOfRootData = rootData.strip().split(' ')
                    
                        if i!=j:
                            testData = allData.iloc[j]
                            targetData = testData[item]
                            pieceOfTargetData = targetData.strip().split(' ')
                            
                            rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)
                            rate_list.append(rate)
                            flag = True
                            targetList.append(targetData)
                            rootList.append(rootData)

                    if(flag):
                        showData = []
                        
                        for show in showingCompareDatas:
                            showData.append(f'{show} = {testData[show]}')
                        boolean_value=True
                        for x in rate_list:
                            if(x<rate_score):
                                boolean_value=False
                                break
                        if(boolean_value):
                            

                            print(f"{kacinci}-) Karsilatirma nesnesi : {rootCompareDatas} | RootData : {rootList} | TargetData: {targetList} | Rate:{rate_list} | ShowData {showData}")
                                
                            print('-'*100)

    # genel Durum
    else:
        for i in range(baslangic, indexArea):
            kacinci=kacinci+1
            mainData = allData.iloc[i]

            for j in range(len(allData)):
                rate_list=[]
                rootList = []
                targetList = []
                flag = False
                for item in rootCompareDatas:
                    rootData = mainData[item]
                    pieceOfRootData = rootData.strip().split(' ')

                    if j!=i:
                        testData = allData.iloc[j]

                        if len(spesifik)>0:
                            if mainData[spesifik].strip() == testData[spesifik].strip():
                                targetData = testData[item]
                                pieceOfTargetData = targetData.strip().split(' ')
                                rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)
                                rate_list.append(rate)
                                flag = True
                                targetList.append(targetData)
                                rootList.append(rootData)
                        else:
                            targetData = testData[item]
                            pieceOfTargetData = targetData.strip().split(' ')
                            rate = compareAlgorithm(pieceRoot=pieceOfRootData, pieceTarget=pieceOfTargetData)
                            rate_list.append(rate)
                            flag = True
                            targetList.append(targetData)
                            rootList.append(rootData)

                            
                       
                            
                if(flag):
                        showData = []
                        
                        for show in showingCompareDatas:
                            showData.append(f'{show} = {testData[show]}')
                        boolean_value=True
                        for x in rate_list:
                            if(x<rate_score):
                                boolean_value=False
                                break
                        if(boolean_value):
                            

                            print(f"{kacinci}-) Karsilatirma nesnesi : {rootCompareDatas} | RootData : {rootList} | TargetData: {targetList} | Rate:{rate_list} | ShowData {showData}")
                                
                            print('-'*100)





    # Bu Kod bana calisma araligini vericek
    # for i in range(indexArea-divison, indexArea):


# setThreadIndex(1, ['Aynı Product'],['Issue'],['Company'],20) 


if __name__ == "__main__": 
    # setProcessIndex(1, ['Aynı Product'],['Issue'],['Company'],20)
    setUltimateProcessIndex(10, ['Aynı Company'],['Issue','Product'],['Company','Product'],0)
    




        











