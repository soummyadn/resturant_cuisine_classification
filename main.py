# restaurant_cuisine_classifier.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report, confusion_matrix
import os

def load_and_preprocess_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    # Load data
    df = pd.read_csv(filepath)
    print("Initial Data Overview:")
    print(df.head())
    print(df.info())

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Rename target column if needed
    if 'Cuisines' in df.columns:
        df.rename(columns={'Cuisines': 'cuisine'}, inplace=True)
    elif 'cuisine' not in df.columns:
        raise KeyError("Target column 'Cuisines' or 'cuisine' not found in dataset.")

    # Drop irrelevant column if it exists
    if 'restaurant_name' in df.columns:
        df.drop(columns=['restaurant_name'], inplace=True)

    # Identify categorical columns (excluding target)
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if 'cuisine' in categorical_cols:
        categorical_cols.remove('cuisine')

    # One-hot encode categorical columns
    df = pd.get_dummies(df, columns=categorical_cols)

    # Encode target column
    le = LabelEncoder()
    df['cuisine'] = le.fit_transform(df['cuisine'])

    return df, le

def split_data(df):
    X = df.drop(columns=['cuisine'])
    y = df['cuisine']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test, le):
    y_pred = model.predict(X_test)
    print("\nModel Evaluation:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision (macro):", precision_score(y_test, y_pred, average='macro'))
    print("Recall (macro):", recall_score(y_test, y_pred, average='macro'))
    print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=le.classes_))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

def main():
    # Replace with your actual CSV file name
    filepath = "dataset.csv"  # Removed the extra space in the file name

    df, le = load_and_preprocess_data(filepath)
    X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test, le)

if __name__ == "__main__":
    main()
