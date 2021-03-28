from PIL import Image
import numpy as np
import random as rd

def takeAvg(valueList):
    n = len(valueList)
    if n == 0:
        return
    sum = [0] * len(valueList[0])
    for rgb in valueList:
        for i in range(len(sum)):
            sum[i] += rgb[i]

    for i in range(len(sum)):
        sum[i] /= n
    return sum

image = Image.open(r"\\ad.tuni.fi\home\gxcung\StudentDocuments\Desktop\bece7c9ebcd7cfd6b43840b37c104c1e.jpg")
rd.seed()
randomNums = []

data = np.array(image)
# print(type(data))

# print(data.shape)
height, width = data.shape[0], data.shape[1]


# Select 1/100 of pixels randomly and set them to black
maxNum = int(height * width / 20)
"""
for _ in range(maxNum):
    i = rd.randint(0, height - 1)
    k = rd.randint(0, width - 2)
    randomNums.append([i, k])
    data[i][k] = [0, 0, 0]

solvedData = data.copy()
# ------------------------------------------- METHOD 1
# Solve the lost in sampling by taking the RGB value of neighbour pixels
# in this case, take the value of right-hand neighbour
for pair in randomNums:
    i,k = pair[0],pair[1]
    solvedData[i][k] = data[i][k + 1]"""


# ------------------------------------------- METHOD 2
# Taking the average value of four nearest neighours: above, to the left, to the right, below
for _ in range(maxNum):
    i = rd.randint(1, height - 2)
    k = rd.randint(1, width - 2)
    randomNums.append([i, k])
    data[i][k] = [0, 0, 0]

# Solve the lost in sampling
solvedData = data.copy()
for pair in randomNums:
    h = pair[0]
    w = pair[1]
    rgbList = []
    rgbList.append(data[h + 1][w])
    rgbList.append(data[h - 1][w])
    rgbList.append(data[h][w + 1])
    rgbList.append(data[h][w - 1])
    data[h][w] = takeAvg(rgbList)

modifiedImage = Image.fromarray(data)
modifiedImage.show()
solvedImage = Image.fromarray(solvedData)
solvedImage.show()
image.show()