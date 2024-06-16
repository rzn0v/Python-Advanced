import requests
import datetime as dt
import smtplib
import time

my_gmail = "renovardhan@gmail.com"
my_pwd = "aduazoukmitjdplu"

LAT = -40.727
LNG = -175.2869

def latlng():
    response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response1.raise_for_status()
    data1 = response1.json()

    iss_lat = float(data1["iss_position"]["latitude"])
    iss_lng = float(data1["iss_position"]["longitude"])
    if LAT-5<=iss_lat<=LAT+5 and LNG-5<=iss_lng<=LNG+5:
        return True
    else:
        return False

def is_night():
    parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}
    time = dt.datetime.now().hour
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if time>=sunset or time<=sunrise:
        return True
    else:
        return False
 
while True:
    if latlng() and is_night():
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_gmail, password=my_pwd)
            connection.sendmail(from_addr=my_gmail,
                                to_addrs="rr1148@srmist.edu.in",
                                msg="Subject:LOOK UP!!!\n\nLook up The ISS is above your head"
                        )
    else:
        print("Not yet")
    time.sleep(60)
