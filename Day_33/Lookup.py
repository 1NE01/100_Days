import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "100daysofpythonbyme"
MY_PASSWORD = "beifvgxozxuddlxb"
MY_LAT = 12.9111021 # Your latitude
MY_LONG = 80.1974239 # Your longitude


def finder():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the iss position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if finder() == night():
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            email_address = '100daysofpythonbyme@gmail.com'
            email_password = 'beifvgxozxuddlxb'
            connection.login(email_address, email_password)
            connection.sendmail(from_addr=email_address, to_addrs='iwontellmyemail@gmail.com',
                                msg="subject:Lookup \n\n Your Pant is flying")


