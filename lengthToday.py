import requests
import tkinter as tk
from tkinter import *
from datetime import timedelta, date

def getToday(lat, lng):
    url = f"https://api.sunrise-sunset.org/v2?lat={lat}&lng={lng}"
    dataToday = requests.get(url)
    dataToday.raise_for_status()
    jsonToday = dataToday.json()
    dayLengthToday = jsonToday["day_length"]
    return dayLengthToday

def getDate(lat, lng, dateStr):
    url = f"https://api.sunrise-sunset.org/v2?lat={lat}&lng={lng}&date={dateStr}"
    dataDate = requests.get(url)
    dataDate.raise_for_status()
    jsonDate = dataDate.json()
    dayLengthDate = jsonDate["day_length"]
    return dayLengthDate

def convertSecToHHMMSS(secs):
    minutes, seconds = divmod(secs,60)
    hours, minutes = divmod(minutes,60)
    return hours, minutes, seconds
    

def main():
    lat, lng = 52.6446, 1.34646
    lengthToday = getToday(lat,lng)
    hToday, mToday, sToday = convertSecToHHMMSS(lengthToday)

    yesterday = date.today() - timedelta(days=1)
    lengthYesterday = getDate(lat,lng,yesterday)
    tomorrow = date.today() + timedelta(days=1)
    lengthTomorrow = getDate(lat,lng,tomorrow)

    diffYesterday = lengthToday - lengthYesterday
    if diffYesterday > 0:
        yDiffH, yDiffM, yDiffS = convertSecToHHMMSS(diffYesterday)
        yDiff = "longer"
    elif diffYesterday < 0:
        yDiffH, yDiffM, yDiffS = convertSecToHHMMSS(-diffYesterday)
        yDiff = "shorter"
    elif diffYesterday == 0:
        yDiffM, yDiffS = 0, 0
        yDiff = "same"

    diffTomorrow = lengthToday - lengthTomorrow
    if diffTomorrow > 0:
        tDiffH, tDiffM, tDiffS = convertSecToHHMMSS(diffTomorrow)
        tDiff = "longer"
    elif diffTomorrow < 0:
        tDiffH, tDiffM, tDiffS = convertSecToHHMMSS(-diffTomorrow)
        tDiff = "shorter"
    elif diffTomorrow == 0:
        tDiffM, tDiffS = 0, 0
        tDiff = "same"

    print(f"Today's day length: {hToday}h {mToday}m {sToday}s")
    print(f"Today is {yDiffM}m {yDiffS}s {yDiff} than yesterday.")
    print(f"Today is {tDiffM}m {tDiffS}s {tDiff} than tomorrow.")

    root = tk.Tk()
    root.title("Day Length Info")
    root.geometry("200x200")


    lbl0 = Label(root, text = f"Location: {lat}\N{DEGREE SIGN}N {lng}\N{DEGREE SIGN}W.")
    lbl0.grid(column=0, row=0, sticky="w")
    lbl1 = Label(root, text = f"Today's day length:")
    lbl1.grid(column=0, row=1, sticky="w")
    lbl2 = Label(root, text = f"{hToday}h {mToday}m {sToday}s", )
    lbl2.grid(column=0, row=2)
    lbl3 = Label(root, text = "Which is:",justify="left")
    lbl3.grid(column=0, row=3, sticky="w")
    lbl4 = Label(root, text = f"{yDiffM}m {yDiffS}s")
    lbl4.grid(column=0, row=4)
    lbl5 = Label(root, text = f" {yDiff} than yesterday, and")
    lbl5.grid(column=0, row=5, sticky="w")
    lbl6 = Label(root, text = f"{tDiffM}m {tDiffS}s")
    lbl6.grid(column=0, row=6)
    lbl7 = Label(root, text = f" {tDiff} than tomorrow.")
    lbl7.grid(column=0, row=7, sticky="w")
    root.mainloop()
    

if __name__ == "__main__":
    main()