import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, classification_report, roc_curve

# Load the dataset
file_path = 'Data/butikken.csv'  # Update the path if needed
data = pd.read_csv(file_path)

# Inspect the dataset
print(data.info())
print(data.describe())

# Split data into features (X) and target (y)
X = data.drop(columns=['kjopt_produkt'])
y = data['kjopt_produkt']

# Handle missing values (impute missing ages with median)
imputer = SimpleImputer(strategy='median')
X['alder'] = imputer.fit_transform(X[['alder']])

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Evaluate the model
roc_auc = roc_auc_score(y_test, y_pred_proba)
classification_rep = classification_report(y_test, y_pred)

print(f"ROC-AUC Score: {roc_auc}")
print("Classification Report:")
print(classification_rep)

# Save predictions to a new DataFrame
test_results = pd.DataFrame(X_test, columns=data.drop(columns=['kjopt_produkt']).columns)
test_results['True_Label'] = y_test.values
test_results['Predicted_Probability'] = y_pred_proba
test_results['Predicted_Label'] = y_pred

# Save to CSV
test_results.to_csv('Data/prediction_results.csv', index=False)
print("Predictions saved to 'prediction_results.csv'.")

# Visualize the ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
plt.figure()
plt.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], 'k--', label="Random Guess")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()
