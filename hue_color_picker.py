import cv2
import numpy as np

WINDOW = "HSV Color Picker"

def nothing(x):
    pass

# Create window
cv2.namedWindow(WINDOW)

# Trackbars
cv2.createTrackbar("Hue", WINDOW, 0, 179, nothing)
cv2.createTrackbar("Sat", WINDOW, 255, 255, nothing)
cv2.createTrackbar("Val", WINDOW, 255, 255, nothing)

# Preview image
preview = np.zeros((200, 400, 3), dtype=np.uint8)

while True:
    # Read HSV values
    h = cv2.getTrackbarPos("Hue", WINDOW)
    s = cv2.getTrackbarPos("Sat", WINDOW)
    v = cv2.getTrackbarPos("Val", WINDOW)

    # HSV → BGR (OpenCV uses H: 0–179)
    hsv_color = np.uint8([[[h, s, v]]])
    bgr_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)[0][0]

    # Fill preview
    preview[:] = bgr_color

    # Text overlay
    text = f"HSV({h}, {s}, {v})  BGR({bgr_color[0]}, {bgr_color[1]}, {bgr_color[2]})"
    cv2.putText(
        preview,
        text,
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255) if v < 128 else (0, 0, 0),
        2
    )

    cv2.imshow(WINDOW, preview)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):  # ESC or q
        break

cv2.destroyAllWindows()
