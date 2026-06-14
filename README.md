# Lane Line Detection Streamlit App

This is a Streamlit web application that performs real-time lane line detection on uploaded video files. It utilizes OpenCV for image processing and MoviePy for video handling.

## Features

*   **Upload Video**: Users can upload MP4 video files.
*   **Lane Detection Pipeline**: The app processes each frame of the video to detect and highlight lane lines using a pipeline that includes:
    *   Color masking (for white and yellow lines)
    *   Grayscale conversion
    *   Gaussian blurring
    *   Canny edge detection
    *   Region of interest masking
    *   Hough transform for line detection
    *   Line extrapolation and smoothing
*   **Processed Video Output**: Displays the video with detected lane lines overlaid.
*   **Robust File Handling**: Uses `tempfile` to securely handle uploaded video files, making it suitable for cloud deployment.

## How to Run Locally

1.  **Clone the repository** (once you have these files in a GitHub repo):
    ```bash
    git clone <your-repo-url>
    cd <your-repo-name>
    ```
2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app**:
    ```bash
    streamlit run streamlit_app.py
    ```

    This will open the application in your web browser.

## Deployment to Streamlit Community Cloud

1.  **Push your project to GitHub**: Ensure all necessary files (`streamlit_app.py`, `requirements.txt`, `README.md`, `.gitignore`) are in a GitHub repository.
2.  **Go to Streamlit Community Cloud**: Visit [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
3.  **Deploy a new app**: Click "New app" and select your repository, branch, and `streamlit_app.py` as the main file path. Click "Deploy!"

Your app will be built and deployed, and you'll get a URL to access it.

## File Structure for Deployment

Your GitHub repository should have a structure similar to this:

```
your-repo-name/
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

Make sure `streamlit_app.py` is in the root directory or adjust the "Main file path" setting during deployment accordingly.
