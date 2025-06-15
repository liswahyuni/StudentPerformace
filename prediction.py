import pickle
import numpy as np
import pandas as pd
from xgboost import XGBClassifier

# Load all preprocessing objects
with open('model/standard_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)
with open('model/onehot_encoder.pkl', 'rb') as f:
    onehot = pickle.load(f)
with open('model/ordinal_encoder.pkl', 'rb') as f:
    ordinal_encoder = pickle.load(f)
with open('model/label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)
with open('model/pca_transformer.pkl', 'rb') as f:
    pca = pickle.load(f)
with open('model/xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load feature lists
with open('model/binary_features.txt') as f:
    binary_features = [line.strip() for line in f]
with open('model/nominal_features.txt') as f:
    nominal_features = [line.strip() for line in f]
with open('model/ordinal_features.txt') as f:
    ordinal_features = [line.strip() for line in f]
with open('model/numeric_features.txt') as f:
    numeric_features = [line.strip() for line in f]

def preprocess_input(user_input):
    df = pd.DataFrame([user_input])
    X_categorical = onehot.transform(df[nominal_features + binary_features])
    X_ord_enc = ordinal_encoder.transform(df[ordinal_features])
    X_num_scaled = scaler.transform(df[numeric_features])
    X_num_pca = pca.transform(X_num_scaled)
    X_full = np.hstack([X_categorical, X_ord_enc, X_num_pca])
    return X_full

def predict(user_input):
    X = preprocess_input(user_input)
    pred_idx = model.predict(X)[0]
    pred_label = label_encoder.inverse_transform([pred_idx])[0]
    return pred_label