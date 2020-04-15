import cv2
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal as D
value = 0
rows = []
cols = []
getLines = []
def Input():
    img =  cv2.imread(url,0)
    cells=[np.hsplit(row,20) for row in np.vsplit(img, 20)]
    global rows
    global cols
    global value
    for i in range (0,20):
        for j in range (0,20):
            if (cells[i][j] != 0):
                rows.append(i) 
                cols.append(j)
                value+=1    
    print(value)
def learn():
    print("please teach me that what is this number: ")
    gets = input()
    file = open('data.txt','a+')
    for i in range (0,value):
        file.write(str(rows[i]))
        file.write('\n')
        file.write(str(cols[i]))
        file.write('\n')
        file.write(str(gets))
        file.write('\n')
    print("Okay! I got it!")
    
def test():
    global rows
    global cols
    global value
    global getLines
    def knnf(a,b):
        data = open('data.txt','r')
        getLines = data.readlines()
        countda = 0
        countdb = 1
        countdc = 2
        da = [0]
        db = [1]
        dc = [2]
        global countLine
        countLine = 0
        for i in getLines:
            countLine+=1
            ml = int(countLine/3-1)
        for i in range(0,ml):
            countda+=3
            da.append(countda)
            countdb+=3
            db.append(countdb)
            countdc+=3
            dc.append(countdc)
        ka = []
        kb = []
        kc = []
        global mmm
        mmm = 0
        for i in da:
            ka.append(int(getLines[i]))
            mmm+=1
        for i in db:
            kb.append(int(getLines[i]))
        for i in dc:
            kc.append(int(getLines[i]))
        data = []
        kkq = []
        for i in range(0,mmm-1):
            data.append([ka[i],kb[i]])
            kkq.append(kc[i])           
        trainData = np.array(data, dtype='float32')
        ketqua = np.array(kkq, dtype='float32')               
        k=[[a, b]]                 
        newMember = np.array(k,dtype='float32')
        knn = cv2.ml.KNearest_create()
        knn.train(trainData, 0, ketqua)
        temp, result, nearest, distance = knn.findNearest(newMember, 5)
        global check
        check = result
        print(result)
    global q0
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    q0 = 0
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    q5 = 0
    q6 = 0
    q7 = 0
    q8 = 0
    q9 = 0
    for i in range (0, value-1):
        knnf(rows[i],cols[i])
        if check==[[0.]]:
            q0+=1
        if check==[[1.]]:
            q1+=1
        if check==[[2.]]:
            q2+=1
        if check==[[3.]]:
            q3+=1
        if check==[[4.]]:
            q4+=1
        if check==[[5.]]:
            q5+=1
        if check==[[6.]]:
            q6+=1
        if check==[[7.]]:
            q7+=1
        if check==[[8.]]:
            q8+=1
        if check==[[9.]]:
            q9+=1

    Max = max(q0,q1,q2,q3,q4,q5,q6,q7,q8,q9)
    print(q0,"\n",q1,"\n",q2,"\n",q3,"\n",q4,"\n",q5,"\n",q6,"\n",q7,"\n",q8,"\n",q9)
    print("Max = ",Max)
    if Max == q0:
        print("This number is 0")
    elif Max == q1:
        print("This number is 1")
    elif Max == q2:
        print("This number is 2")
    elif Max == q3:
        print("This number is 3")
    elif Max == q4:
        print("This number is 4")
    elif Max == q5:
        print("This number is 5")
    elif Max == q6:
        print("This number is 6")
    elif Max == q7:
        print("This number is 7")
    elif Max == q8:
        print("This number is 8")
    elif Max == q9:
        print("This number is 9")
    else:
        print("Loading...")
#main control
print("\t\t\tWelcome to ours project: \nBuild a solution that computer can learn and identify numbers and letters by Python")
print("Input start to run program or exit to exit the program")
cin = input()
while cin !="exit":
    print ("Input url of your img (plese select a image having size 20*20 pixel): ")
    url = input()
    Input()
    # mo dau
    print("Hi there! Plesse write down 'learn' or 'test'")
    print("if you write down 'learn' i will learn  and if you write down 'test' i will define that you ask me")
    yourChoice = input()
    if yourChoice == "learn":
        learn()
    elif yourChoice == "test":
        test()
    else:
        print("Invalid Syntax")
    print("Input continue to continue program or exit to exit the program")
    cin = input()

print("Exited!")








    
