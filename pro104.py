import cv2

img = cv2.imread("solar-system.jpg")
sun="Sun"
m="Mercury"
v="Venus"
e="Earth"
M="Mars"
j="Jupiter"
s="Saturn"
n="Neptune"
u="Uranis"
cv2.putText(img,sun,(100,100),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,225))
cv2.putText(img,m,(120,190),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,v,(190,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,e,(270,170),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,M,(380,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,j,(580,50),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,s,(780,120),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,u,(960,140),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,225))
cv2.putText(img,n,(1120,150),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(225,225,225))
cv2.imshow("solar-system",img)
cv2.waitKey(0)