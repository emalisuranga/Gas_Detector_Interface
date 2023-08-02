import requests  # Importing the requests module for making HTTP requests
import numpy as np  # Importing the numpy module for numerical operations
import matplotlib.pyplot as plt  # Importing the matplotlib module for data visualization
import tkinter as tk  # Importing the tkinter module for creating GUI windows
from tkinter import messagebox  # Importing the messagebox module from tkinter

class AirQualityAnalyzer:
    def __init__(self, city, api_key):
        self.city = city  # Initializing the city for air quality analysis
        self.api_key = api_key  # Initializing the API key for accessing air quality data
        self.url = f'http://api.waqi.info/feed/{city}/?token={api_key}'  # Generating the URL for the API request
        self.csv_file_path = 'nehru-nagar, kanpur-air-quality.csv'
        self.data = None  # Variable to store the retrieved air quality data
        self.aqi = None  # Variable to store the overall Air Quality Index (AQI)
        self.iaqi = None  # Variable to store individual Air Quality Index (AQI) values for pollutants
        self.pollutants = []  # List to store the names of pollutants
        self.values = []  # List to store the corresponding values of pollutants
        self.max_so2_value = 5

# Retrieving the air quality data
    def get_air_quality_data(self):
        air_quality_data = requests.get(self.url)  
        self.data = air_quality_data.json()['data']  
        self.aqi = self.data['aqi']  
        self.iaqi = self.data['iaqi']

# Extracting pollutant values from the data
    def extract_pollutant_values(self):
        del self.iaqi['p']  # Removing the 'p' key which is not a pollutant
        for pollutant, details in self.iaqi.items():
            self.pollutants.append(pollutant)  
            self.values.append(details['v'])  

# Printing the air quality measurements
    def print_air_quality_measurements(self):
        for pollutant, value in zip(self.pollutants, self.values):
            print(f'{pollutant}: {value}')  

 # Getting the AQI value for pollutant
    def get_pollutant_value(self, pollutant):
        return self.iaqi.get(pollutant, 'Nil')  
    
# Checking the SO2 gas level and displaying a pop-up message if it's harmful
    def check_so2_gas_level(self):
        so2_value = self.get_pollutant_value('so2')  
        if so2_value != 'Nil' and so2_value.get('v', 'Nil') > self.max_so2_value:
            messagebox.showwarning('High SO2 Level', 'The SO2 gas level is bad for humans!')  

# Plotting the pie chart
    def plot_pie_chart(self):
        explode = [0] * len(self.pollutants)  
        max_index = self.values.index(max(self.values))  
        explode[max_index] = 0.1 
        plt.figure(figsize=(8, 6))  # Creating a figure for the pie chart
        plt.pie(self.values, labels=self.pollutants, explode=explode)  # Creating the pie chart
        plt.title(f'Air pollutants and their probable amount in the atmosphere {self.city}\n')
        plt.axis('equal') 
        plt.show()  

# read csv to numpy array
    def read_csv_to_numpy_array(self):
        # Read the CSV file into a list of rows
        with open(self.csv_file_path, 'r') as file:
            lines = file.readlines()
        # Remove any leading/trailing whitespaces and split by comma to get values
        data = [line.strip().split(',') for line in lines]
        # Convert the list of lists to a NumPy array
        np_array = np.array(data) 

        return np_array


def main():
    city = 'pardubice'  # Specifying the city for air quality analysis
    api_key = '05377255c64d4375292a2a30ce2b07f244844fd7'  # Specifying the API key for accessing air quality data
    analyzer = AirQualityAnalyzer(city, api_key)
    analyzer.get_air_quality_data() 
    analyzer.extract_pollutant_values()  
    analyzer.print_air_quality_measurements()  
    dew = analyzer.get_pollutant_value('dew')  
    no2 = analyzer.get_pollutant_value('no2')  
    o3 = analyzer.get_pollutant_value('o3')  
    so2 = analyzer.get_pollutant_value('so2')  
    pm10 = analyzer.get_pollutant_value('pm10')  
    pm25 = analyzer.get_pollutant_value('pm25') 

    print(f'{city} AQI: {analyzer.aqi}\n')  
    print('Individual Air quality')
    print(f'Dew: {dew}')  
    print(f'no2: {no2}')  
    print(f'Ozone: {o3}')  
    print(f'sulphur: {so2}')  
    print(f'pm10: {pm10}')  
    print(f'pm25: {pm25}')  

    analyzer.check_so2_gas_level() 
    analyzer.plot_pie_chart()  # Plotting the pie chart
    
    numpy_array = analyzer.read_csv_to_numpy_array()
    print("Old Air Quality:")
    print(numpy_array)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    main()
    root.mainloop()
