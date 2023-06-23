import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the dataset
data = pd.read_csv('charging_station_dataset.csv')

# Separate features (X) and target variable (y)
X = data[['latitude', 'longitude', 'solar_intensity', 'wind_speed']]
y = data['suitable_location']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
clf = RandomForestClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))

# Predict suitable locations for each district
districts = ['Bengaluru', 'Vijayawada', 'Chennai']

for district in districts:
    district_data = data[data['district'] == district]
    district_locations = district_data[['latitude', 'longitude', 'solar_intensity', 'wind_speed']]
    predicted_labels = clf.predict(district_locations)
    suitable_locations = district_data[predicted_labels == 'Yes']
    
    print(f"Best-suited locations for {district}:")
    print(suitable_locations)
    print('\n')
