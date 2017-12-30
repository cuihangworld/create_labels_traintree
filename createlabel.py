f = open('/Users/niecui/Desktop/label/label.txt','w')
index = 0
label = 1
for i in range(800):
    if 40 == index and 1 == label:
        label = 0
        index = 0
    elif 40 == index and 0 == label:
        label = 1
        index = 0
    labels = str(label)+'\n'
    f.write(labels)
    index = index+1

f.close()
