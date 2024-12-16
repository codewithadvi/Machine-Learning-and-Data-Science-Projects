import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Corrected file path (ensure the CSV file exists at this location)
framingham = pd.read_csv(r"E:\ADVI\Code\python\webapp\framingham.csv")

# Dropping rows with missing values
framingham = framingham.dropna()

# Display the first few rows of the dataset
print(framingham.head())

# Display value counts of the target column (TenYearCHD)
print(framingham['TenYearCHD'].value_counts())

# Prepare features (X) and target variable (y)
X = framingham.drop('TenYearCHD', axis=1)
y = framingham['TenYearCHD']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Perform oversampling on the minority class using RandomOverSampler
oversample = RandomOverSampler(sampling_strategy='minority')
X_over, y_over = oversample.fit_resample(X_train, y_train)

# Initialize and train the Random Forest model
rf = RandomForestClassifier()
rf.fit(X_over, y_over)

# Predict on the test set
preds = rf.predict(X_test)

# Print the accuracy score of the model
print("Accuracy:", accuracy_score(y_test, preds))

# Save the trained model using joblib
joblib.dump(rf, 'fhs_rf_model.pkl')
print("Model trained and saved successfully!")

