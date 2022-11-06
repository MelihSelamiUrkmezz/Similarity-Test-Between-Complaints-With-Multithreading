import pandas as pd
import threading

# kodun yazılacagı yer


# get Data
allData = pd.read_csv(r"C:\Users\ASUS Pc\Desktop\VSCodeProject\yazlab12\deneme.csv", encoding='latin1')

def compareOfCol(indexArea, selectedData, i, divison):

   
    
    print(f"Merhba ben {i} 'inci threadim ve yazdıklarım bu sekild...")

    for index in range(indexArea-divison, indexArea):
        print("indexin degeri ",index)
        print(selectedData.iloc[index])
    
    print('--------------------------------------------------')

    
     




    
def getParas(threadCount, col):
    # Meregava
    
    selectedData = allData[col]
    divison = int(len(selectedData) / threadCount)
    pieceValues = []
    temp = divison
    while True:
        if temp > len(selectedData):
            break
        
        pieceValues.append(int(temp))
        temp += divison

    print(pieceValues)

    # gerekli threadler buraya yuklenecek
    threads = []
    
   

    for i in range(threadCount):
        threads.append(threading.Thread(target=compareOfCol, args=(pieceValues[i], selectedData, i, divison)))
    
    for thread in threads:
        thread.start()
        

        
    

        
    
    

    

    



getParas(2,"Product")





