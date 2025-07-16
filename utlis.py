import cv2
import numpy as np


def stackImages(imgArray, scale, lables=[]):
    rows = len(imgArray)
    cols = len(imgArray[0]) if isinstance(imgArray[0], list) else len(imgArray)
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)

    else:
        for x in range(0, rows):
            imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        ver = np.hstack(imgArray)

    if len(lables) != 0:
        eachImgWidth = int(ver.shape[1] / cols)
        eachImgHeight = int(ver.shape[0] / rows)

        for d in range(0, rows):
            for c in range(0, cols):
                cv2.rectangle(ver,
                              (c * eachImgWidth, eachImgHeight * d),
                              (c * eachImgWidth + len(lables[d][c]) * 13 + 27, eachImgHeight * d + 30),
                              (255, 255, 255),
                              cv2.FILLED)
                cv2.putText(ver,
                            lables[d][c],
                            (eachImgWidth * c + 10, eachImgHeight * d + 20),
                            cv2.FONT_HERSHEY_COMPLEX,
                            0.7,
                            (0, 0, 0),
                            2)

    return ver


def rectContour(contours):

    rectCon = []

    for i in contours :
        area = cv2.contourArea(i)
        if area>50 :
            peri = cv2.arcLength(i , True)
            approx = cv2.approxPolyDP(i , 0.02*peri , True)
            # print("Corner Points" , len(approx))

            if len(approx) == 4 :
                rectCon.append(i)

    rectCon = sorted(rectCon , key = cv2.contourArea ,reverse=True)

    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
    return approx

def reorder(myPoints):

    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4, 1, 2) , np.int32)
    add = myPoints.sum(1)
    #print(myPoints)
    #print(add)
    myPointsNew[0] = myPoints[np.argmin(add)] # [0,0]
    myPointsNew[3] = myPoints[np.argmax(add)] # [w , h]
    diff = np.diff(myPoints , axis = 1)
    myPointsNew[1] = myPoints[np.argmin(diff)] # [w , 0]
    myPointsNew[2] = myPoints[np.argmax(diff)] # [h , 0]
    #print(diff)

    return myPointsNew

def splitBoxes(img):
    rows = np.vsplit(img , 5)
    boxes = []
    for r in rows :
        cols = np.hsplit(r , 5)
        for box in cols :
            boxes.append(box)
            #cv2.imshow("split" , box)

    return boxes

def showAnswers(img , myIndex , grading , answers , questions , choices):
    secW = int(img.shape[1]/questions)
    secH = int(img.shape[0]/choices)

    for x in range(0 , questions ):
        myAns = myIndex[x]
        cX = (myAns*secW)+secW//2
        cY = (x*secH) + secH//2

        if grading[x] == 1 :
            myColor = (0,255,0)
        else :
            myColor = (0,0,255)
            correctAns = answers[x]
            cv2.circle(img, ((correctAns*secW)+secW//2, cY), 20, (0,255,0), cv2.FILLED)

        cv2.circle(img , (cX , cY) , 50 , myColor , cv2.FILLED)
    return img

