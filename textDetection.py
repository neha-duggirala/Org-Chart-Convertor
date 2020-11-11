import cv2
from shapeDetection import ShapeDetector
# text detection
def contours_text(orig):
    contours, _ = cv2.findContours(orig,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    # Draw all contours
    cv2.drawContours(orig, contours, -1, (0,255,0), 3)
    cv2.imshow('ALL',orig)
    cv2.waitKey()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for c in contours:
        # compute the center of the contour, then detect the name of the
        # shape using only the contour
        try:
            M = cv2.moments(c)
            print(M)
            cX = int((M["m10"] / M["m00"]))
            cY = int((M["m01"] / M["m00"]))
            shape = sd.detect(c)
            # multiply the contour (x, y)-coordinates by the resize ratio,
            # then draw the contours and the name of the shape on the image
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            x, y, w, h = cv2.boundingRect(c)
            print(y,y + h, x,x + w)
            cropped = resized[y:y + h, x:x + w]
            cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
            cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(img, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 2)
            cv2.imshow("img", img)
            cv2.waitKey(0)
            cv2.imshow("cropped img", cropped)
            cv2.waitKey(0)
        except:
            print("exception")

path = 'Samples/input2.jpg'
resizeShape=500
img = cv2.imread(path)
print(img.shape)
img =  cv2.resize(img, (resizeShape,resizeShape))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
resized = cv2.resize(gray, (resizeShape,resizeShape))
ratio = img.shape[0] / float(resized.shape[0])
sd = ShapeDetector()
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
thresh = cv2.threshold(blurred,120, 255, cv2.THRESH_BINARY)[1] # try tweaking these parameters  (if the pixel is greater than 120 then fill that pixel with white-255)
# cv2.imshow('resized',resized)
# cv2.waitKey()
# cv2.imshow('blurred',blurred)
# cv2.waitKey()
# cv2.imshow('thresh',thresh)
# cv2.waitKey()
contours_text(thresh)

