 
import cv2

im=input(r'enter path:')
name=input("enter file name: ")
upper_cascade=cv2.CascadeClassifier(r"C:\Users\PASKAL\Downloads\haarcascade_upperbody.xml")
face_cascade=cv2.CascadeClassifier(r"C:\Users\PASKAL\Desktop\python_aaradhya\haarcascade_frontalface_default (1).xml")
eye_cascade=cv2.CascadeClassifier(r"C:\Users\PASKAL\Desktop\python_aaradhya\haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier(r"C:\Users\PASKAL\Desktop\python_aaradhya\haarcascade_smile.xml")


img = cv2.imread(im)
if img is None:
    print("not loading image...")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    upper = upper_cascade.detectMultiScale(gray, 1.05, 5)
    for (x, y, w, h) in upper:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img, "upper_body detected!", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.2, (0, 255, 0), 2)
    
     
    face=face_cascade.detectMultiScale(gray,1.1,5)
      
    for (fx,fy,wx,hy) in face:    

        roi=gray[fy:fy+hy,fx:fx+wx]
        eye=eye_cascade.detectMultiScale(roi,1.2,10)
        smile=smile_cascade.detectMultiScale(roi,1.5,20)

        if len(face)>0:
            cv2.rectangle(img,(fx,fy),(fx+wx,fy+hy),(0,255,0),2)
            cv2.putText(img,"face detected!",(fx,fy-40),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(0,255,0),1)

        if len(eye)>0:
            cv2.putText(img,"eye detected!",(fx,fy-20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(0,255,0),1)

        if len(smile)>0:
             cv2.putText(img,"smile detected!",(fx,fy-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.2,(0,255,0),1)

cv2.imshow('detecting....',img)
cv2.imwrite(f"{name}.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()