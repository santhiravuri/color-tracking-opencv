

### Project Name: Color Tracking with OpenCV

#### Description:
A Python application using OpenCV to detect and track objects based on their colors using HSV color ranges. It highlights detected objects with colored borders and displays their color names in the detected color itself.

#### Project Structure:
```
color-tracking/
│
├── README.md
├── requirements.txt
└── src/
    ├── color_tracker.py
    └── ...
```

### Setup Instructions:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/santhiravuri/color-tracking-opencv.git
   cd color-tracking
   ```

2. **Set Up Virtual Environment (recommended):**
   ```bash
   # Create virtual environment (venv)
   python -m venv venv_name
   
   # Activate virtual environment
   source venv_name/bin/activate   # for Linux/Mac
   venv_name\Scripts\activate      # for Windows
   
   # Install required libraries
   pip install -r requirements.txt
   ```

3. **Install Dependencies:**
   Ensure `opencv-python` and other required libraries are installed. If not installed globally, use the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

### Usage:
1. **Run the Application:**
   ```bash
   python src/color_tracker.py
   ```

2. **Adjust HSV Color Ranges:**
   - If the object you want to track is not detected properly, adjust the HSV color ranges in `src/color_tracker.py`:
     ```python
     color_ranges = {
         'red': ([0, 100, 100], [10, 255, 255]),       # Red
         'green': ([40, 50, 50], [90, 255, 255]),     # Green
         ...
     }
     ```

3. **Interaction:**
   - Use the Trackbars window to adjust HSV ranges interactively for better detection.

### Additional Notes:
- Ensure proper lighting conditions for accurate color detection.
- Adjust contour area threshold (`area > 1000`) and border thickness (`cv2.rectangle(frame, (x, y), (x + w, y + h), color_rgb, 3)`) in `src/color_tracker.py` as needed.
- Press `Esc` key to exit the application.

### Example Output:
- The application will display a live webcam feed with colored borders around detected objects and their respective color names displayed in the detected color.

### Dependencies:
- `opencv-python`: 4.10.0
- `numpy`: 1.22.1
- Other dependencies specified in `requirements.txt`
