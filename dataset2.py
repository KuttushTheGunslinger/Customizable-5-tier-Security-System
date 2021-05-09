import csv
import cv2

p = []
e = []

with open('500_picts_satz.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        p.append(row[1])

print(p)

with open('500_picts_satz.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        e.append(row[2])

print(e)

for i in range(500):
    img = cv2.imread('D:/security/images/' + p[i])
    img = cv2.resize(img, (48, 48))

    if e[i] == 'fear':
        cv2.imwrite('D:/security/data/train/fearful/pic' + str(i) + '.png', img)
    elif e[i] == 'anger':
        cv2.imwrite('D:/security/data/train/angry/pic' + str(i) + '.png', img)
    elif e[i] == 'happiness':
        cv2.imwrite('D:/security/data/train/happy/pic' + str(i) + '.png', img)
    elif e[i] == 'sad':
        cv2.imwrite('D:/security/data/train/sad/pic' + str(i) + '.png', img)
    elif e[i] == 'neutral':
        cv2.imwrite('D:/security/data/train/neutral/pic' + str(i) + '.png', img)

