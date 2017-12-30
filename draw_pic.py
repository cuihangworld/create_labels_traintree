import matplotlib.pyplot as plt
import os
from numpy import *
def read_loss(path):
    f = open(path, 'r')
    loss = []
    for line in f.readlines():
        loss.append(line[:-1])
    print loss
    f.close()
    return loss

def draw_pic(path,path_save,file):
    num = read_loss(path)
    j = 0
    num.append(1)
    for i in num:
        j = j + 1
    # print j
    plt.ylim(0, 256)
    x = arange(0, j, 1)
    y = num
    plt.plot(x, y)
    #    plt.show()
    #    x = arange(0,j,1)
    #    y = num
    #plt.xlabel("num of loss")
    #plt.ylabel("rate of loss")
    #    plt.plot(x,y,'ro')
    #plt.show()
    paths = path_save+file[:-3]+'png'
    #print paths
    plt.savefig(paths)
    plt.close()


if __name__ == '__main__':
    path1 = '/Users/niecui/Desktop/labels_yuan/'
    path2 = '/Users/niecui/Desktop/pic/'
    for root, dirs, files in os.walk(path1):
        pass
    #print files
    for file in files:
        path = path1+file
        draw_pic(path,path2,file)
    '''num = read_loss(path)
    j = 0
    num.append(1)
    for i in num:
        j = j+1
    #print j
    plt.ylim(0,256)
    x = arange(0,j,1)
    y = num
    plt.plot(x,y)
#    plt.show()
#    x = arange(0,j,1)
#    y = num
    plt.xlabel("num of loss")
    plt.ylabel("rate of loss")
#    plt.plot(x,y,'ro')
    plt.show()'''
