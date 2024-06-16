import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

class BloodDonationModel:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.scaler = StandardScaler()
        self.is_trained = False

    def load_and_preprocess_data(self, file_path):
        df = pd.read_csv(file_path)
        features = df[['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time (months)']]
        labels = df['whether he/she donated blood in March 2007']
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
        self.scaler.fit(X_train)  # Fit the StandardScaler on training data
        X_train_scaled = self.scaler.transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        return X_train_scaled, X_test_scaled, y_train, y_test

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        self.is_trained = True

    def predict(self, features):
        if not self.is_trained:
          raise ValueError("Model must be trained before prediction.")
        scaled_features = self.scaler.transform(features.reshape(1, -1))
        return self.model.predict(scaled_features)

    def save_model(self, model_path, scaler_path):
        joblib.dump(self.model, model_path)
        joblib.dump(self.scaler, scaler_path)

    def load_model(self, model_path, scaler_path):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.is_trained = True

    def evaluate_model(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy
    def optimize_model(self, features, labels):
        models = {
            'Random Forest': RandomForestClassifier(),
            'Gradient Boosting': GradientBoostingClassifier(),
        }
        ensemble_model = VotingClassifier([(name, model) for name, model in models.items()])

        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', ensemble_model)
        ])

        cv_scores = cross_val_score(pipeline, features, labels, cv=5)
        print("Cross-validation Scores:", cv_scores)
        print("Mean Cross-validation Score:", cv_scores.mean())

        return pipeline

    def evaluate_metrics(self, y_test, y_pred):
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred)

        print("Precision:", precision)
        print("Recall:", recall)
        print("F1-score:", f1)
        print("ROC-AUC Score:", roc_auc)

# Example usage
# model = BloodDonationModel()
# X_train, X_test, y_train, y_test = model.load_and_preprocess_data('path/to/blood_transfusion.csv')
# model.train_model(X_train, y_train)
# model.save_model('model.pkl', 'scaler.pkl')
