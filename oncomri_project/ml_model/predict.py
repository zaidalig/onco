import cv2
import numpy as np
import pickle
import os

# Load model + label map once
MODEL_PATH = os.path.join(os.path.dirname(__file__), "sklearn_model.pkl")
with open(MODEL_PATH, "rb") as f:
    model, label_map = pickle.load(f)

# Reverse label_map for ID → Name lookup
label_reverse = {v: k for k, v in label_map.items()}

def predict(image_path):
    IMG_SIZE = 64  # Must match your training size
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        return "Invalid Image", 0.0

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    flat = img.flatten().reshape(1, -1)

    pred_id = model.predict(flat)[0]
    class_name = label_reverse[pred_id]

    # Optional: confidence from predict_proba (if supported)
    if hasattr(model, "predict_proba"):
        conf = model.predict_proba(flat)[0][pred_id]
    else:
        conf = 1.0  # fallback

    return class_name, round(conf * 100, 2)
