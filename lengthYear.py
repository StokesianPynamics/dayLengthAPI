from datetime import date, timedelta
import requests
import numpy as np
import matplotlib.pyplot as plt

def getYear(lat, lng, year):
    url = f"https://api.sunrise-sunset.org/v2?lat={lat}&lng={lng}&date_start={year}-01-01&date_end={year}-12-31"
    dataDate = requests.get(url)
    dataDate.raise_for_status()
    jsonDate = dataDate.json()
    days = jsonDate["days"]
    return np.array([[date.fromisoformat(day["date"]).timetuple().tm_yday, day["day_length"]] for day in days])

def main():
    lat, lng = 52.6446, 1.34646
    year = 2026
    dayLengths = getYear(lat,lng,year)
    print("moses")
    plt.plot(dayLengths[0,:], dayLengths[1,:])
    plt.show()
    print("well we got here")


if __name__ == "__main__":
    main()




