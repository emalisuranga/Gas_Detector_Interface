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


def main():
    city = 'pardubice'  # Specifying the city for air quality analysis
    api_key = '05377255c64d4375292a2a30ce2b07f244844fd7'  # Specifying the API key for accessing air quality data
    analyzer = AirQualityAnalyzer(city, api_key)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    main()
    root.mainloop()
