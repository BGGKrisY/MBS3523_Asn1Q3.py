import cv2
x = 100
y = 100
vx = 5
vy = 7
frame_width = 640
frame_height = 480
theta = 45
theta_rad = theta * (3.14159 / 180)
Frame = cv2.VideoCapture(0)
while True:
   ret, frame = Frame.read()
   cv2.rectangle(frame, (int(x), int(y)), (int(x) + 80, int(y) + 80), (0, 255, 0), 2)
   cv2.putText(frame, 'MBS3523 Assignment 1 – Q3 Name: YEUNG YAT', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (125, 0, 125), 2)
   x += vx
   y += vy
   if x < 0 or x + 80 > frame_width:
       vx = -vx
   if y < 0 or y + 80 > frame_height:
       vy = -vy
   cv2.imshow('MBS3523 Assignment 1 – Q3 Name: YEUNG YAT', frame)
   if cv2.waitKey(1) & 0xFF == ord('o'):
       break
Frame.release()
cv2.destroyAllWindows()
