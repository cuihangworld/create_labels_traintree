import cv2
import numpy as np
import os
def cut_save(path_pre,path_save):

    img = cv2.imread(path_pre)

    imgs = np.zeros((205, 460, 3), np.uint8)

    for i in range(205):
        for j in range(460):
            imgs[i,j] = img[220+i,100+j]

    cv2.imwrite(path_save,imgs)


if __name__ == '__main__':
    path1 = "/Users/niecui/Desktop/pic/"
    path2 = '/Users/niecui/Desktop/pic_new/'
    #cut_save(path1,path2)
    for root, dirs, files in os.walk(path1):
        pass
    for file in files:
        #print file
        if file == '.DS_Store':
            continue
        path = path1+file
        paths = path2+file
        cut_save(path,paths)
        #print file