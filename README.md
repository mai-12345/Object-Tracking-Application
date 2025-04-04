# Object Tracking Application

This is a Streamlit-based object tracking application using background subtraction and contour detection techniques. The application allows you to upload a video, and it processes the video to highlight moving objects in the frames.

## Features

- Upload a video in `.mp4`, `.mov`, or `.avi` format.
- Object tracking is performed using background subtraction and contour detection.
- Moving objects in the video are highlighted with bounding boxes.
- The processed frames are displayed in real-time using Streamlit.

## Requirements

To run the Object Tracking Application, you'll need Python 3.x and the following libraries:

1. **Streamlit**: For creating the web interface.
2. **OpenCV**: For video processing and object tracking.
3. **NumPy**: For handling arrays and image data.
4. **Matplotlib**: For displaying images and visualizations.
5. **Pillow (PIL)**: For image processing.

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run Object_Tracking.py
    ```

4. The application will open in your web browser. You can upload a video for object tracking.

## How It Works

1. **Video Upload**: Users can upload videos via the Streamlit interface.
2. **Object Tracking**: The video is processed to track moving objects using background subtraction and contour detection.
3. **Visualization**: The detected objects are highlighted with bounding boxes on each frame.

## Acknowledgments

This project uses OpenCV for video processing and object tracking. Special thanks to the authors of these libraries for their contributions.

