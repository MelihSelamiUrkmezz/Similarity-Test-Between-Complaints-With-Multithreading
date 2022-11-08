import pandas as pd
import threading
import time

# kodun yazılacagı yer


# get Data
allData = pd.read_csv(r"C:\Users\ASUS Pc\Desktop\VSCodeProject\yazlab12\deneme.csv", encoding='utf8')

def compareAlgorithm(pieceRoot, pieceTarget):

    maxLength = len(pieceRoot)

    if len(pieceTarget) > len(pieceRoot):
        maxLength = len(pieceTarget)
    
    sameCount = 0

    for rootItem in pieceRoot:

        for targetItem in pieceTarget:
            
            if rootItem == targetItem:
                sameCount = sameCount + 1 
    
    result = (sameCount / maxLength) * 100

    return result

def compareOfCol(indexArea, sayi, divison, *selectedCol):
    start_time = time.time()
    selectedCol = list(selectedCol)[0]

    print('Secilen Colonlar ', selectedCol)

    
    # tek stun gonderildiyse
    # stunun benzerlik oranı kontrol edilemli
    
    if len(selectedCol) == 1:
        
        for i in range(indexArea-divison, indexArea):
            print('*'*100)
            rootData = allData[selectedCol[0]].iloc[i]
            pieceOfRooData = rootData.split(' ')
            
            # str

            for j in range(len(allData)):

                # burada aynı urun icin bakmasın diye
                if i != j:
                    # algoritma gelecek
                    targetData = allData[selectedCol[0]].iloc[j]
                    pieceOfTargetData = targetData.split(' ')

                    rate = compareAlgorithm(pieceRoot=pieceOfRooData, pieceTarget=pieceOfTargetData)

                    print(f'Ben {sayi} numaralı Thredim --- Root Data = {rootData}  Target Data = {targetData}  Rate = %{rate}')

                    # karsılastırma algoritmas
    
    print(f"--- {(time.time() - start_time)} seconds --- Ben {sayi} numaralı thredim")
                    





    
        
    # for index in range(indexArea-divison, indexArea):
        
    #     print(allData.iloc[index])

    # Karsilasitmra islemi kaldı Su an tek islem yapıyor
    
    

    
     

    
def setThreadIndex(threadCount, *params):

    params = list(params)
    
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
        threads.append(threading.Thread(target=compareOfCol, args=(pieceValues[i], i, divison, params,)))
    
    for thread in threads:
        
        thread.start()
        
        
        

   
setThreadIndex(3, "Product")  




        






