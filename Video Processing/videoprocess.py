# read Video
import cv2

cap = cv2.VideoCapture("C:/Users/shubham singh/Downloads/Face Recognition/tutorial.mp4")

print(cap.isOpened())

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

print(cap.get(cv2.CAP_PROP_FRAME_COUNT))

cnt = 0

while(cap.isOpened()):

# while True:
    success, frame = cap.read()
    # print(success)

    if success == False:
        break
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Wireframe Tutorial", frame)
    cnt = cnt + 1
    # print("success", success)

    if cv2.waitKey(1) == 13:
        # if cv2.waitKey(1) == ord('q'):
        break

print(cnt)
cap.release()
cv2.destroyAllWindows()
