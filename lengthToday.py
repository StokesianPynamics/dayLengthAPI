import requests
from datetime import timedelta, date

def getToday(lat, lng):
    url = f"https://api.sunrise-sunset.org/v2?lat={lat}&lng={lng}"
    dataToday = requests.get(url)
    jsonToday = dataToday.json()
    dayLengthToday = jsonToday["day_length"]
    return dayLengthToday

def getDate(lat, lng, dateStr):
    url = f"https://api.sunrise-sunset.org/v2?lat={lat}&lng={lng}&date={dateStr}"
    dataDate = requests.get(url)
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
    

if __name__ == "__main__":
    main()