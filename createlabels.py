import cv2
import numpy as np


def readImage(path):
    img = cv2.imread(path)
    img1 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    
    return img1

def writeOpera(path,img):

    h,w = img.shape[:2]
    for j in range(w):
        #print path+str(j)+'.txt'
        #n = j+num
        #print n
        f = open(path+str(j+781)+'.txt', 'w')
        for i in range(h-1):
            num = str(img[i,j])
            num = num[1:-1]+'\n'
            f.write(num)
        f.close()



#x,y wei label de fanwei, y_min yu y_max wei labels de zuida yu zuixiao
def createLabels(path,x,y_min,y_max):
    img = readImage(path)
    j = 0
    n = 0
    y = y_max - y_min
    a = 0
    b = 0
    imgs = np.zeros((y, 20, 1), np.uint8)
    #print len(imgs)
    for m in range(20):
        n = x+m
        for i in range(1,y):
            j = y_min+i
            imgs[a,b] = img[j,n]
            a = a+1
        b = b+1
        a = 0
    return imgs

if __name__ == '__main__':
    path1 = '/Users/niecui/Desktop/yuantu/000052.jpg'
    path2 = '/Users/niecui/Desktop/labels_yuan/'
    img = createLabels(path1,331,54,317)
    writeOpera(path2,img)
    #print img.shape[:2]
#cv2.imshow("cui",img)
#cv2.waitKey(0)
#j = 0
#n = 0
#for m in range(20):
#    n = 215+m
#    for i in range(323):
#        j = 11+i
#        print img[j,n]
