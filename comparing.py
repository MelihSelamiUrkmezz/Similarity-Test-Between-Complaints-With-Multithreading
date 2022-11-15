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

    return result

def compareOfCol(indexArea, sayi, divison, *selectedCol):
    process = True
    start_time = time.time()
    selectedCol = list(selectedCol)[0]

    print('Secilen Colonlar ', selectedCol)

    
    # tek stun gonderildiyse
    # stunun benzerlik oranı kontrol edilemli

    for item in selectedCol:
        if type(item) == int:
            process = False
            for i in range(indexArea-divison, indexArea):
                print('*'*100)
                # mesele productı aynı olanlar diyor ya

                # ordaki şarttaki kontrol degeri

                # Performans acısında basta maine aldım her seyi parcalama islemini onun uzerinde yaptım
                mainData = allData.iloc[i]
                ifForRootData = mainData[selectedCol[0]]
                rootData = mainData[selectedCol[2]]
                pieceOfRooData = rootData.strip().split(' ')

                # ise idsi esit degilse
                
                if ifForRootData != selectedCol[1]:
                    continue
                
                # str

                for j in range(len(allData)):

                    # burada aynı urun icin bakmasın diye
                    if i != j:
                        
                        testData = allData.iloc[j]
                        
                        
                        # algoritma gelecek
                        targetData = testData[selectedCol[2]]
                        pieceOfTargetData = targetData.strip().split(' ')
                        valueTargetData = testData[selectedCol[2]]

                        rate = compareAlgorithm(pieceRoot=pieceOfRooData, pieceTarget=pieceOfTargetData)
                        
                        print(f'Ben {sayi} numaralı Thredim --- Root Data = {rootData}  Target Data = {targetData}  Rate = %{rate}  Company = {valueTargetData}')

                        # karsılastırma algoritmas


    
        print(f"--- {(time.time() - start_time)} seconds --- Ben {sayi} numaralı thredim")

            
    
    # 1.seneryo
    if len(selectedCol) == 1 and process:
        process = False
        for i in range(indexArea-divison, indexArea):
            print('*'*100)
            rootData = allData[selectedCol[0]].iloc[i]
            pieceOfRooData = rootData.strip().split(' ')
            
            # str

            for j in range(len(allData)):

                # burada aynı urun icin bakmasın diye
                if i != j:
                    # algoritma gelecek
                    targetData = allData[selectedCol[0]].iloc[j]
                    pieceOfTargetData = targetData.strip().split(' ')

                    rate = compareAlgorithm(pieceRoot=pieceOfRooData, pieceTarget=pieceOfTargetData)

                    print(f'Ben {sayi} numaralı Thredim --- Root Data = {rootData}  Target Data = {targetData}  Rate = %{rate}')

                    # karsılastırma algoritmas

    # 2.seneryo
    elif len(selectedCol) ==3 and process:
        process = False
        for i in range(indexArea-divison, indexArea):
            print('*'*100)
            # mesele productı aynı olanlar diyor ya

            # ordaki şarttaki kontrol degeri

            # Performans acısında basta maine aldım her seyi parcalama islemini onun uzerinde yaptım
            mainData = allData.iloc[i]
            ifForRootData = mainData[selectedCol[0]]
            rootData = mainData[selectedCol[1]]
            pieceOfRooData = rootData.strip().split(' ')
            
            # str

            for j in range(len(allData)):

                # burada aynı urun icin bakmasın diye
                if i != j:
                    testData = allData.iloc[j]
                    ifForTargetData = testData[selectedCol[0]]
                    if ifForTargetData == ifForRootData:
                        # algoritma gelecek
                        targetData = testData[selectedCol[1]]
                        pieceOfTargetData = targetData.strip().split(' ')
                        valueTargetData = testData[selectedCol[2]]

                        rate = compareAlgorithm(pieceRoot=pieceOfRooData, pieceTarget=pieceOfTargetData)

                        print(f'Ben {sayi} numaralı Thredim --- Root Data = {rootData}  Target Data = {targetData}  Rate = %{rate}  Company = {valueTargetData}')

                    # karsılastırma algoritmas


    
        print(f"--- {(time.time() - start_time)} seconds --- Ben {sayi} numaralı thredim")
                      
def setProcessIndex(threadCount, *params):

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
    processes = []
    
   

    for i in range(threadCount):
        processes.append(mp.Process(target=compareOfCol, args=(pieceValues[i], i, divison, params,)))
    
    for process in processes:
        
        process.start()
        
        
        

if __name__ == "__main__": 
    setProcessIndex(1, "Complaint ID",3238275,"Issue")  




        






