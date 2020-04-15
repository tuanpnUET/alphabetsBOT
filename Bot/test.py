import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
#read img
print("url|_img")
url_img = input()
img =  cv2.imread(url_img,0)
cells=[np.hsplit(row,20) for row in np.vsplit(img, 20)]
ox = []
m = 0
for i in range (0,20):
    for x in range (0,20):
        if (cells[i][x] != 0):
            ox.append([i,x])
            m+=1
#tạo 1 số biến để kiểm tra điều kiệu của điểm
global d
d = []
n1 = 0
n2 = 0
n3 = 0
n4 = 0

# kiểm tra từng điểm và tìm vị trí của nó với điểm đầu tiên
# điểm thứ nhất sẽ là 1 mảng lưu vị trí của điểm thứ 2 theo quy tắc sau
# [phải,trái,trên,dưới,khoảng cách trên trục ox, khoảng cách trên trục oy]
#ví dụ điểm sau [0,1,1,0,3,4] nghĩa là điểm tiếp theo nằm bên trái, và bên trên khoảng cách với điểm tiếp theo trên trục 0x là 3, và oy là 4
# 4 giá trị đầu tiên của mảng này chỉ có thể là 0 hoặc 1 và không thể có 3 số 1 trong 4 giá trị đó dk vì k thể có vị trí nào là vừa trên lạ vừa dưới hoặc cả trái lẫn phải
# và còn giá trị thứ 5 là trọn số của điểm đó , nếu nó được knn nhận dạng 1 lần thì +1
global coundD
coundD = 0
for i in range(0,m):
    n2 = 0
    n3 = 0
    n5 = 0
    n6 = 0
    dox = 0
    doy = 0
    # chung ox
    if(ox[1][0] == ox[i][0]):
        dox += 0
    #tiep tuc la ben phai
    if(ox[1][0] < ox[i][0]):
        n2 +=1
        dox =ox[i][0] - ox[1][0]
    # tiep tuc ben trai
    if (ox[1][0] > ox[i][0]):
        n3+=1
        dox = ox[1][0] - ox[i][0] 
    #chung oy
    if(ox[1][1] == ox[i][1]):
        doy +=0
    # tiep tuc ben tren
    if(ox[1][1] < ox[i][1]):
        n5+=1
        doy = ox[i][1] - ox[1][1]
    #tiep tuc ben duoi
    if(ox[1][1] > ox[i][1]):
        n6+=1
        doy = ox[1][1] - ox[i][1]
    n1 = 0
    n7 = 0
    n8 = 0
    d.append([n1,n2,n3,n5,n6,dox,doy,n8,n7])
    coundD+=1
#saving 
print("saving?????????")
test_save= input()
if (test_save == 'yes'):
    print("urlsaving")
    url_saving= input()
    
    file = open(url_saving,'a+')
    for i in range(0,coundD):
        file.write(str(d[i]))
        file.write('\n')
    file.close()
    print("saving secced")
    

#read
if(test_save == 'test'):
        
#number
# hàm genfromtxt trả về mảng từ file mà nó đọc
# url là url file lưu dữ liệu muốn đọc covn cái delimiter thì mặc định phải có

    def read(url,array,sln):
        kk = np.genfromtxt(url,delimiter=',')
        cound = 0
        for i in kk:
            cound+=1
        for i in range(0,cound):
            array.append([int(kk[i][1]),int(kk[i][2]),int(kk[i][3]),int(kk[i][4]),int(kk[i][5]),int(kk[i][6])])
            sln.append(int(kk[i][7]))
# sln là mảng chứa trọng số của từng điểm
    nub_1 = []
    sln_1 = []
    read('nub_1.txt',nub_1,sln_1)   
    nub_2 = []
    sln_2 = []
    read('nub_2.txt',nub_2,sln_2)
    nub_3 = []
    sln_3 = []
    read('nub_3.txt',nub_3,sln_3)
    cound_1 = 0
    cound_2 = 0
    cound_3 = 0
    for i in nub_1:
        cound_1+=1
    for i in nub_2:
        cound_2+=1
    for i in nub_3:
        cound_3+=1
    #knn
    def knnf(a,b,c,d,e,f):
        trainData = np.array(data, dtype='float32')
        ketqua = np.array(kq, dtype='float32')               
        k=[[a,b,c,d,e,f]]                 
        newMember = np.array(k,dtype='float32')

        knn = cv2.ml.KNearest_create()
        knn.train(trainData, 0, ketqua)
        temp, result, nearest, distance = knn.findNearest(newMember, 1)
        global ioo
        ioo = result
    print(cound_1,cound_2,cound_3,coundD)
    #test
    #những biến với mảng này là để lưu mảng với trọng số mới sau khi nhận dạng giá trị thay đổi là cái trọng số thôiu
    
    nb3 = 0
    nb1 = 0
    nb2 = 0
    nub_11 = []
    nub_22 = []
    nub_33 = []
    nub_44 = []
# so sánh điểm đầu tiên của thằng nhận dạng với điểm đầu tiên của những thằng khác
# nên file data phải chứa những điểm đầu tiên của những thằng mà nó đã học
# sau điểm đầu tiên là điểm thứ 2, 3 ,4 ,5 ,... nên file data phải tạo mới nếu tạo file data ngoài for thì nó lưu tất từ điểm đầu đến điểm cuối thì k dk vì ta đang so sánh điểm đầu với điểm đầu , điểm thứ 2 với điểm thứ 2 ,...

    for i in range(0,40):
        global data
        global kq
        data=[]
        kq = []
        data.append(nub_1[i])
        kq.append(1)
        data.append(nub_2[i])
        kq.append(2)
        data.append(nub_3[i])
        kq.append(3)
        knnf(d[i][0],d[i][1],d[i][2],d[i][3],d[i][4],d[i][5])
# vẫn như trc mk chạy từng điểm pixel của đối tượng nhận dạng khác cái là mỗi lần như
# vậy thì mảng data với kq để trainning phải tạo mới
# kết quả ra thì sẽ có 3 cái trên 
        if(ioo==[[1.]]):
# nb1 là đếm số lần xuất hiện của kết quả 1 để tí kiểm tra xem thằng nào lớn nhất
            nb1+=1
#phần bên dưới là append thêm phần tử cho mảng để  lưu lại làm dữ liệu gốc
# vì để thay 1 chỉ số trong file đã lưu cần lấy ra đọc lại và thay đổi chỗ cần đổi rồi lưu lại 
# nếu kết quả là 1 thì trọng số của nub_1 tăng 1 giá trị còn trọng số của nub_  khác phải tăng lên là 0 thì cũng là ban đầu

            sln_11 = sln_1[i]+1
            nub_11.append([0,nub_1[i][0],nub_1[i][1],nub_1[i][2],nub_1[i][3],nub_1[i][4],nub_1[i][5],sln_11,0])
            nub_22.append([0,nub_2[i][0],nub_2[i][1],nub_2[i][2],nub_2[i][3],nub_2[i][4],nub_2[i][5],sln_2[i],0])
            nub_33.append([0,nub_3[i][0],nub_3[i][1],nub_3[i][2],nub_3[i][3],nub_3[i][4],nub_3[i][5],sln_3[i],0])
        if(ioo==[[2.]]):
            nb2+=1
            sln_22 = sln_2[i]+1
            nub_22.append([0,nub_2[i][0],nub_2[i][1],nub_2[i][2],nub_2[i][3],nub_2[i][4],nub_2[i][5],sln_22,0])
            nub_11.append([0,nub_1[i][0],nub_1[i][1],nub_1[i][2],nub_1[i][3],nub_1[i][4],nub_1[i][5],sln_1[i],0])
            nub_33.append([0,nub_3[i][0],nub_3[i][1],nub_3[i][2],nub_3[i][3],nub_3[i][4],nub_3[i][5],sln_3[i],0])
        if(ioo == [[3.]]):
            nb3+=1
            sln_33 = sln_3[i]+1
            nub_33.append([0,nub_3[i][0],nub_3[i][1],nub_3[i][2],nub_3[i][3],nub_3[i][4],nub_3[i][5],sln_33,0])       
            nub_11.append([0,nub_1[i][0],nub_1[i][1],nub_1[i][2],nub_1[i][3],nub_1[i][4],nub_1[i][5],sln_1[i],0])
            nub_22.append([0,nub_2[i][0],nub_2[i][1],nub_2[i][2],nub_2[i][3],nub_2[i][4],nub_2[i][5],sln_2[i],0])    
# lưu các file đã thay đổi trọng số 
    file1 = open('nub_1.txt','w+')
    for i in range(0,40):
        file1.write(str(nub_11[i]))
        file1.write('\n')
    file1.close()
    file2 = open('nub_2.txt','w+')
    for i in range(0,40):
        file2.write(str(nub_22[i]))
        file2.write('\n')
    file2.close()
    file3 = open('nub_3.txt','w+')
    for i in range(0,40):
        file3.write(str(nub_33[i]))
        file3.write('\n')
    file3.close()
    print(nub_33)
    print(nb1,nb2,nb3)    


