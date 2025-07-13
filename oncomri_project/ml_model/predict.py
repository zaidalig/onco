import random

def predict(image_path):
    # Dummy logic – replace with real CNN model later
    labels = ["Cancer Detected", "No Cancer Detected"]
    prediction = random.choice(labels)
    confidence = round(random.uniform(0.80, 0.99), 2)
    return prediction, confidence
