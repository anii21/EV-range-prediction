import serial
import pandas as pd
from sklearn.linear_model import LinearRegression
import warnings

# Load the CSV dataset
data = pd.read_csv('ev_dataset.csv')

# Prepare data
X = data[['Battery Capacity', 'Average Speed', 'Battery Temperature', 'AC Usage']]
y = data['Range']

# Train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Ignore UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

# Establish serial communication with Arduino
ser = serial.Serial('COM11', 9600)  # Update 'COM11' with the correct port and baud rate if needed

# Read temperature and battery percentage from Arduino
temperature = None
battery_percentage = None

while temperature is None or battery_percentage is None:
    line = ser.readline().decode().rstrip()
    if line.startswith("Temperature:"):
        temperature = float(line.split(":")[1])
    elif line.startswith("Battery:"):
        battery_percentage = float(line.split(":")[1])  # Convert to float instead of int

# AC usage input from user
ac_usage = int(input("Enter AC usage (0 for off, 1 for on): "))

# Make prediction using the inputs
battery_capacity_new = 70  # Example battery capacity
speed = float(input("Enter the average speed (in km/h): "))\
X_new = [[battery_capacity_new, speed, temperature, ac_usage]]
range_predicted = 2*(model.predict(X_new))
print("temp =",temperature)
print("battery percentage =",battery_percentage)
# Print the predicted range
print(f"Predicted Range: {range_predicted[0]}")
# Close serial communication with Arduino
ser.close()
