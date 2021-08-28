# How to use Webcam  Cap.set  3 width
import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 500)
cap.set(4, 400)
# cap.set(10,30)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    success, frame = cap.read()
    cv2.imshow("Webcam image", frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
