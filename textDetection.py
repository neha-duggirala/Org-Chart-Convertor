import cv2
from shapeDetection import ShapeDetector
from textRecognition import img2text
import dataFrameCreation
# text detection
def contours_text(orig):
    contours, _ = cv2.findContours(orig,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    # Draw all contours
    cv2.drawContours(orig, contours, -1, (0,255,0), 3)
    cv2.imshow('ALL',orig)
    cv2.waitKey()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for c in contours:
        try:
            M = cv2.moments(c)
            # print(M)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            shape = sd.detect(c)
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            
            x, y, w, h = cv2.boundingRect(c)
            # print(y,y + h, x,x + w)
            
            cropped = resized[y:y + h, x:x + w]
            cv2.imshow("cropped img", cropped)
            cv2.waitKey()
            text = img2text(cropped)
            # print(text)
            recognizedText.append(" ".join(text))
            cv2.drawContours(hsv, [c], -1, (0, 255, 0), 2)
            cv2.circle(hsv, (cX,cY), 7, (255, 255, 255), -1)
            cv2.putText(hsv, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2)
            cv2.imshow("hsv", hsv)
            cv2.waitKey()
        except Exception as inst:
            print(inst)
    
    print(recognizedText)


path = 'Samples/input1-middle.jpg'
recognizedText=[]
resizeShape=600
img = cv2.imread(path)
print(img.shape)
img =  cv2.resize(img, (resizeShape,resizeShape))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
resized = cv2.resize(gray, (resizeShape,resizeShape))
ratio = img.shape[0] / float(resized.shape[0])
# ratio = 1
sd = ShapeDetector()
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred,200, 255, cv2.THRESH_BINARY)[1] # try tweaking these parameters  (if the pixel is greater than 120 then fill that pixel with white-255)
cv2.imshow('img',img)
cv2.waitKey()
cv2.imshow('blurred',blurred)
cv2.waitKey()
cv2.imshow('thresh',thresh)
cv2.waitKey()
contours_text(thresh)

dataFrameCreation.writeToExcel(recognizedText)
