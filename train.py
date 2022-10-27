import sys
import pandas as pd
import numpy as np
import json

def error(predictions, targets):
	return predictions - targets

def predict(theta0, theta1, x):
	return theta0 + (theta1 * x)

def cost(theta0, theta1, features, targets):
	pass

def train(features, targets, theta0, theta1, l_rate):
	predictions = predict(theta0, theta1, features)
	errors = error(predictions, targets)
	delta0 = l_rate * (1 / errors.size) * np.sum(errors)
	delta1 = l_rate * (1 / errors.size) * np.sum(errors * features)
	return theta0 - delta0, theta1 - delta1

def export_values(theta0, theta1):
	try:
		with open("data/values.json", "r") as f:
			file_data = json.load(f)
		file_data["theta0"] = theta0
		file_data["theta1"] = theta1
		with open("data/values.json", "w") as f:
			json.dump(file_data, f)
	except:
		print("Something went wrong with opening/writing to values.json", sys.stderr)
		sys.exit(-1)

def main():
	data = pd.read_csv("data/data.csv")
	# Normalize the values to aviod overflow
	max_km = data["km"].max()
	max_price = data["price"].max()
	data["km"] = data["km"] / max_km
	data["price"] = data["price"] / max_price
	data = data.to_numpy()
	features = data[:, 0]
	targets = data[:, 1]
	epochs = 1000
	l_rate = 0.1
	theta0 = 0
	theta1 = 0
	for epoch in range(epochs):
		theta0, theta1 = train(features, targets, theta0, theta1, l_rate)
	# un-normalize to have proper predictions
	theta0 *= max_price
	theta1 *= max_price / max_km
	export_values(theta0, theta1)


if __name__ == "__main__":
	main()