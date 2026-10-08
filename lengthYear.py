from datetime import date, timedelta
import requests
import numpy as np
import matplotlib.pyplot as plt
from lengthToday import convertSecToHHMMSS

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
    days = dayLengths[:,0]
    lengthMins = dayLengths[:,1]/60
    dldt = np.gradient(lengthMins,days)
    d = 10
    ii = np.where(days == d)[0][0]
    print(f"Current rate of change: {dldt[ii]}")

    print(f"Max to min ratio =  {np.max(dayLengths[:,1])/np.min(dayLengths[:,1])}")

    plt.plot(dayLengths[:,0], dayLengths[:,1]/3600)
    plt.show()


if __name__ == "__main__":
    main()




