import pandas as pd
import threading

# kodun yazılacagı yer


# get Data
allData = pd.read_csv(r"C:\Users\ASUS Pc\Desktop\VSCodeProject\yazlab12\deneme.csv", encoding='utf8')

def compareOfCol(indexArea, i, divison, *selectedCol):

    selectedCol = list(selectedCol)

    if len(selectedCol) == 1:
        selectedCol = selectedCol[0]
        
    for index in range(indexArea-divison, indexArea):
        print(selectedCol.iloc[index])

    # Karsilasitmra islemi kaldı Su an tek islem yapıyor
    
    

    
     

    
def getParas(threadCount, *col):
    
    col = list(col)

    if len(col) == 1:
        selectedData = allData[col[0]]
        

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
        threads.append(threading.Thread(target=compareOfCol, args=(pieceValues[i], i, divison, selectedData,)))
    
    for thread in threads:
        thread.start()
        

        
getParas(2,"Product")  

        






