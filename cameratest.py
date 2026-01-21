import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    # capute the frame
    _, frame = cap.read()
    hsv_frame =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    # find center of the frame

    cx = int(width / 2)
    cy = int(height / 2)

    # pick pixel value
    pixel_center = hsv_frame[cx, cy]
    hue_value = pixel_center[0]
    print(pixel_center)

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.circle(frame, (cx, cy), 5, (b, g, r), 3)

    # show image 
    frame = cv2.flip(frame, 1)
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)

    # breake image
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()