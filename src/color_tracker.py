import cv2
import numpy as np

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)

# Define the HSV ranges for different colors
# Format: ([lower H, lower S, lower V], [upper H, upper S, upper V])
color_ranges = {
    'red': ([0, 100, 100], [10, 255, 255]),         # Red
    'green': ([40, 50, 50], [90, 255, 255]),       # Green
    'blue': ([100, 100, 100], [130, 255, 255]),    # Blue
    'yellow': ([20, 100, 100], [30, 255, 255]),    # Yellow
    'orange': ([10, 100, 100], [20, 255, 255]),    # Orange
    'pink': ([145, 50, 50], [175, 255, 255]),      # Pink
    'white': ([0, 0, 200], [180, 20, 255]),        # White
    'black': ([0, 0, 0], [180, 255, 30]),          # Black
    'grey': ([0, 0, 40], [180, 30, 200]),          # Grey
    'brown': ([0, 50, 50], [30, 255, 150]),        # Brown
}


def detect_color(frame, color_name, lower_range, upper_range):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert frame to HSV color space
    mask = cv2.inRange(hsv, lower_range, upper_range)  # Create a mask for the color
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)  # Threshold the mask

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Adjust the minimum contour area threshold as needed
            x, y, w, h = cv2.boundingRect(contour)  # Get the bounding box coordinates
            
            # Convert HSV color to RGB and then to tuple of integers
            color_bgr = cv2.cvtColor(np.uint8([[color_ranges[color_name][0]]]), cv2.COLOR_HSV2BGR)[0][0]
            color_rgb = tuple(map(int, color_bgr[::-1]))  # Convert BGR to RGB and make tuple of integers
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), color_rgb, 3)  # Draw a colored border
            cv2.putText(frame, color_name.capitalize(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color_rgb, 2)  # Display color name

# Main loop to capture frames from the webcam
while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        break  # If frame not read correctly, exit the loop

    frame = cv2.resize(frame, (640, 480))  # Resize the frame to 640x480 pixels

    # Detect each color based on its HSV range
    for color_name, (lower, upper) in color_ranges.items():
        detect_color(frame, color_name, np.array(lower), np.array(upper))

    cv2.imshow("Color Tracking", frame)  # Display the frame with detected colors

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Exit if the 'Esc' key is pressed
        break

cap.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows


