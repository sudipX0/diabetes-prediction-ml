import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from dpred.config import settings


def train():
    df = pd.read_csv(settings.dataset_path)

    feature_cols = ["Pregnancies", "Glucose", "BMI", "DiabetesPedigreeFunction", "Age"]
    X = df[feature_cols]
    y = df["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)

    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test accuracy: {acc:.4f}")

    settings.model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, settings.model_path)
    print(f"Model saved to: {settings.model_path}")


if __name__ == "__main__":
    train()
