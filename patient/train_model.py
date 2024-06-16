from ml_model import BloodDonationModel

if __name__ == "__main__":
    model = BloodDonationModel()
    X_train, X_test, y_train, y_test = model.load_and_preprocess_data(r'C:\Users\DELL\Documents\GitHub\bloodbankmanagement\transfusion.csv')
    model.train_model(X_train, y_train)
    model.save_model('model.pkl', 'scaler.pkl')

    # Optimize the model
    pipeline = model.optimize_model(X_train, y_train)
    pipeline.fit(X_train, y_train)

    # Evaluate the model
    y_pred = pipeline.predict(X_test)
    accuracy = model.evaluate_model(X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Evaluate metrics beyond accuracy
    model.evaluate_metrics(y_test, y_pred)
