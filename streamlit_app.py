import streamlit as st
import cv2
import numpy as np
from moviepy.editor import VideoFileClip
import os
import tempfile
import math

# Global variable to smooth lines over time
previous_lines = [0, 0, 0, 0]

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def draw_lines(img, lines, color=[255, 0, 0], thickness=10):
    global previous_lines # Must declare global to modify
    if lines is None:
        return

    imshape = img.shape
    left_lines = []
    right_lines = []
    left_lines_aligned = []
    right_lines_aligned = []

    for line in lines:
        for x1, y1, x2, y2 in line:
            if (x2 - x1) == 0:
                continue

            m = (y2 - y1) / (x2 - x1)
            b = y1 - (m * x1)
            if m < 0:
                left_lines.append((m, b))
            elif m > 0:
                right_lines.append((m, b))

    ml, bl, mr, br = 0, 0, 0, 0

    if len(left_lines) > 0:
        left_m = [line[0] for line in left_lines]
        left_m_avg = np.mean(left_m)
        left_m_std = np.std(left_m)
        if left_m_std != 0:
            for line in left_lines:
                if abs(line[0] - left_m_avg) < left_m_std:
                    left_lines_aligned.append(line)
        else:
            left_lines_aligned = left_lines
        if len(left_lines_aligned) > 0:
            ml = np.mean([line[0] for line in left_lines_aligned])
            bl = np.mean([line[1] for line in left_lines_aligned])

    if len(right_lines) > 0:
        right_m = [line[0] for line in right_lines]
        right_m_avg = np.mean(right_m)
        right_m_std = np.std(right_m)
        if right_m_std != 0:
            for line in right_lines:
                if abs(line[0] - right_m_avg) < right_m_std:
                    right_lines_aligned.append(line)
        else:
            right_lines_aligned = right_lines
        if len(right_lines_aligned) > 0:
            mr = np.mean([line[0] for line in right_lines_aligned])
            br = np.mean([line[1] for line in right_lines_aligned])

    smooth_fact = 0.8
    if ml != 0 and abs(ml) < 1000:
        if previous_lines[0] != 0:
            ml = previous_lines[0] * smooth_fact + ml * (1 - smooth_fact)
            bl = previous_lines[1] * smooth_fact + bl * (1 - smooth_fact)
    elif previous_lines[0] != 0:
        ml = previous_lines[0]
        bl = previous_lines[1]

    if mr != 0 and abs(mr) < 1000:
        if previous_lines[2] != 0:
            mr = previous_lines[2] * smooth_fact + mr * (1 - smooth_fact)
            br = previous_lines[3] * smooth_fact + br * (1 - smooth_fact)
    elif previous_lines[2] != 0:
        mr = previous_lines[2]
        br = previous_lines[3]

    x1l, y1l, x2l, y2l = 0, imshape[0], 0, int(6 * imshape[0] / 10)
    if ml != 0:
        x1l = int((bl - imshape[0]) / (-1 * ml))
        x2l = int((bl - 6 * imshape[0] / 10) / (-1 * ml))

    x1r, y1r, x2r, y2r = 0, int(6 * imshape[0] / 10), 0, imshape[0]
    if mr != 0:
        x1r = int((br - 6 * imshape[0] / 10) / (-1 * mr))
        x2r = int((br - imshape[0]) / (-1 * mr))

    if ml != 0 and mr != 0 and x2l < x1r:
        cv2.line(img, (x1l, y1l), (x2l, y2l), [0, 255, 0], thickness)
        cv2.line(img, (x1r, y1r), (x2r, y2r), [0, 0, 255], thickness)

    previous_lines[0] = ml
    previous_lines[1] = bl
    previous_lines[2] = mr
    previous_lines[3] = br

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def weighted_img(img, initial_img, alpha=0.8, beta=0.6, gamma=0.):
    return cv2.addWeighted(initial_img, alpha, img, beta, gamma)

def lane_finding_pipeline(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask_white = cv2.inRange(img, (200,200,200), (255, 255, 255))
    mask_yellow = cv2.inRange(hsv_img, (15,60,20), (25, 255, 255))
    color_mask = cv2.bitwise_or(mask_white, mask_yellow)
    masked_img = np.copy(img)
    masked_img[color_mask == 0] = [0,0,0]

    gray_img = grayscale(masked_img)
    kernel_size = 5
    blurred_gray_img = gaussian_blur(gray_img, kernel_size)

    low_threshold = 50
    high_threshold = 150
    edges_from_img = canny(blurred_gray_img, low_threshold, high_threshold)

    imshape = img.shape
    vertices = np.array([[(0,imshape[0]),(4*imshape[1]/9, 6*imshape[0]/10), (5*imshape[1]/9, 6*imshape[0]/10), (imshape[1],imshape[0])]], dtype=np.int32)
    masked_edges = region_of_interest(edges_from_img, vertices)

    rho = 2
    theta = np.pi/180
    threshold = 15
    min_line_len = 10
    max_line_gap = 5
    line_img = hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)

    overlay_img = weighted_img(line_img, img)
    return overlay_img

def process_image(image):
    result = lane_finding_pipeline(image)
    return result

st.set_page_config(page_title="Lane Line Detection", page_icon=":car:", layout="wide")

st.title("Lane Line Detection using MoviePy and OpenCV")
st.markdown("Upload a video to see the lane line detection in action! This application processes video frames to detect and highlight lane lines.")

uploaded_file = st.file_uploader("Choose a video file (.mp4)", type=["mp4"])

if uploaded_file is not None:
    st.video(uploaded_file)

    # Use tempfile to create a temporary file for the uploaded video
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
        tmp_file.write(uploaded_file.read())
        video_path = tmp_file.name

    st.write("Processing video... This might take a while depending on video length and size.")
    st.info("Please wait, the processed video will appear below.")

    try:
        # Load the video clip
        clip = VideoFileClip(video_path)

        # Process the video
        processed_clip = clip.fl_image(process_image)

        # Save the processed video to another temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as processed_tmp_file:
            processed_output_path = processed_tmp_file.name
            processed_clip.write_videofile(processed_output_path, audio=False, codec='libx264')

        st.success("Video processing complete!")
        st.video(processed_output_path)

    except Exception as e:
        st.error(f"An error occurred during video processing: {e}")
        st.warning("Please ensure the uploaded video is a valid MP4 and try again.")

    finally:
        # Clean up temporary files
        if 'video_path' in locals() and os.path.exists(video_path):
            os.remove(video_path)
        if 'processed_output_path' in locals() and os.path.exists(processed_output_path):
            os.remove(processed_output_path)

    st.markdown("--- ")
    st.write("Upload another video or explore the code! ")
