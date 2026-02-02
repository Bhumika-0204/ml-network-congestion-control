import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# -------------------- LOAD DATA --------------------
data = pd.read_csv("../data/network_data.csv")

features = [
    "incoming_rate",
    "queue_length",
    "sent_packets",
    "dropped_packets"
]

X = data[features]
y = data["congestion"]

# -------------------- SPLIT --------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# -------------------- MODEL (LIGHTWEIGHT) --------------------
model = LogisticRegression(
    max_iter=200,
    n_jobs=1  # keep CPU usage low
)

# -------------------- TRAIN --------------------
model.fit(X_train, y_train)

# -------------------- EVALUATE --------------------
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print("Accuracy:", acc)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -------------------- SAVE MODEL --------------------
joblib.dump(model, "congestion_model.pkl")
print("\nModel saved as congestion_model.pkl")
