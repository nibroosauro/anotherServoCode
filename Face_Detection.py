import cv2 as cv
import serial 

defAngleX = 90
defAngleY = 90

ser = serial.Serial('COM3', '9600', timeout=5)

capture = cv.VideoCapture(0)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
pretrained_model = cv.CascadeClassifier("face_detector.xml")

while True:
    boolean, frame = capture.read()
    if boolean == True:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        coordinate_list = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        #rectangle and dot in frame
        for (x, y, w, h) in coordinate_list:
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            centerX = x + w//2
            centerY = y + h//2
            cv.circle(frame, (centerX, centerY), 3, (255, 0, 0), -1)
            errorX = centerX-width/2
            errorY = centerY-height/2

            if errorX > 0:
                defAngleX = defAngleX - 1
            if errorX < 0:
                defAngleX = defAngleX + 1
            if errorY > 0:
                defAngleY = defAngleY - 1
            if errorY < 0:
                defAngleY = defAngleY + 1

            x = int(defAngleX)
            y = int(defAngleY)
            data = f"{x},{y}\n"
            ser.write(data.encode('utf-8'))

        #display detected face
        cv.imshow("Face Detection", frame)

        #close the program
        if cv.waitKey(20) == ord('x'):
            break

capture.release()
cv.destroyAllWindows()