import pandas as pd
import threading

# kodun yazılacagı yer


# get Data
allData = pd.read_csv(r"C:\Users\ASUS Pc\Desktop\VSCodeProject\yazlab12\deneme.csv", encoding='utf8')

def compareOfCol(indexArea, i, divison, *selectedCol):
    
    selectedCol = list(selectedCol)

    print('Secilen Colonlar ', selectedCol)

    
        
    for index in range(indexArea-divison, indexArea):
        
        print(allData.iloc[index])

    # Karsilasitmra islemi kaldı Su an tek islem yapıyor
    
    

    
     

    
def setThreadIndex(threadCount, *params):

    params = list(params)
    
    selectedData = allData
        

    divison = int(len(selectedData) / threadCount)
    print('Divison : ',divison)
    pieceValues = []
    temp = divison
    print('Temp. ',temp)
    while True:
        if temp > len(selectedData):
            break
        
        pieceValues.append(int(temp))
        temp += divison
        print('Temp :', temp)

    
    print(pieceValues)
    # gerekli threadler buraya yuklenecek
    threads = []
    
   

    for i in range(threadCount):
        threads.append(threading.Thread(target=compareOfCol, args=(pieceValues[i], i, divison, params,)))
    
    for thread in threads:
        thread.start()
        

        
setThreadIndex(4, "Product","Company")  




        






