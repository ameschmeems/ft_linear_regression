import sys
from train import predict
import json
import sys

def get_values():
	try:
		with open("data/values.json", "r") as f:
			file_data = json.load(f)
		return file_data["theta0"], file_data["theta1"]
	except:
		print("Something went wrong with opening values.json", sys.stderr)
		sys.exit(-1)

def main():
	theta0, theta1 = get_values()
	km = float(input("Provide kilometrage to predict the price: "))
	price = predict(theta0, theta1, km)
	print(f"Predicted price is {price}")


if __name__ == "__main__":
	main()