import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose


def extract_measurements(image):

    pose = mp_pose.Pose(static_image_mode=True)

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    if not results.pose_landmarks:
        return None

    h, w, _ = image.shape
    lm = results.pose_landmarks.landmark

    # Head landmark
    head = lm[0]

    # Ankles
    left_ankle = lm[27]
    right_ankle = lm[28]

    # Estimate body height in pixels
    ankle_y = max(left_ankle.y, right_ankle.y)
    height_px = abs(head.y - ankle_y) * h

    # Assume average human height
    avg_height_cm = 170

    scale = avg_height_cm / height_px

    # Shoulders
    ls = lm[11]
    rs = lm[12]

    ls_x, ls_y = ls.x * w, ls.y * h
    rs_x, rs_y = rs.x * w, rs.y * h

    shoulder_px = math.sqrt((ls_x - rs_x)**2 + (ls_y - rs_y)**2)

    shoulder_cm = shoulder_px * scale

    # Waist using hips
    lh = lm[23]
    rh = lm[24]

    lh_x, lh_y = lh.x * w, lh.y * h
    rh_x, rh_y = rh.x * w, rh.y * h

    waist_px = math.sqrt((lh_x - rh_x)**2 + (lh_y - rh_y)**2)

    waist_cm = waist_px * scale * 1.2

    return {
        "shoulder_cm": round(shoulder_cm, 2),
        "waist_cm": round(waist_cm, 2)
    }