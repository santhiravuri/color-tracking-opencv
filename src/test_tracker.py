import cv2  # Import OpenCV library for computer vision tasks
import numpy as np  # Import NumPy library for numerical operations

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)

# Define the lower and upper range for the color to be tracked
# These values should be adjusted to match the color you want to track
lower_range = np.array([30, 150, 50])  # Example: lower bound for a green color
upper_range = np.array([85, 255, 255])  # Example: upper bound for a green color

while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        break  # If frame not read correctly, exit the loop

    frame = cv2.resize(frame, (640, 480))  # Resize the frame to 640x480 pixels
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame from BGR to HSV color space

    mask = cv2.inRange(hsv, lower_range, upper_range)  # Create a mask for the specified color range
    _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)  # Threshold the mask to get binary image

    cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # Find contours in the mask
    for c in cnts:
        # Filter out small contours based on the contour area
        if cv2.contourArea(c) > 600:
            x, y, w, h = cv2.boundingRect(c)  # Get bounding box for the contour
            # Draw the bounding box on the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Put text "DETECT" on the frame
            cv2.putText(frame, "DETECT", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("FRAME", frame)  # Show the frame with bounding boxes

    if cv2.waitKey(1) & 0xFF == 27:  # Exit if the 'Esc' key is pressed
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
