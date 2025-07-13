import os
import cv2
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# ===== Settings =====
IMG_SIZE = 64  # Resize all images to 64x64
DATASET_DIR = "dataset/Training"
MODEL_OUTPUT = "ml_model/sklearn_model.pkl"

# ===== Prepare Data =====
X = []
y = []
labels = sorted(os.listdir(DATASET_DIR))  # Assumes each folder = a class
label_map = {label: idx for idx, label in enumerate(labels)}

print("📂 Reading images from dataset...")
for label in labels:
    class_folder = os.path.join(DATASET_DIR, label)
    for file in os.listdir(class_folder):
        img_path = os.path.join(class_folder, file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
            X.append(img.flatten())
            y.append(label_map[label])

X = np.array(X)
y = np.array(y)

print(f"✅ Loaded {len(X)} images across {len(labels)} classes")

# ===== Split Data =====
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ===== Train Model =====
print("🧠 Training RandomForestClassifier...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ===== Evaluate =====
print("\n📊 Evaluation on test set:")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=labels))

# ===== Save Model =====
os.makedirs("ml_model", exist_ok=True)
with open(MODEL_OUTPUT, "wb") as f:
    pickle.dump((model, label_map), f)

print(f"\n✅ Model saved to {MODEL_OUTPUT}")
