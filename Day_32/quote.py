import random
import datetime as dt
import smtplib
email_address = '100daysofpythonbyme@gmail.com'
email_password = 'beifvgxozxuddlxb'
now=dt.datetime.now()
weekday=now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:

        connection.login(email_address, email_password)
        connection.sendmail(
            from_addr=email_address,
            to_addrs='iwontellmyemail@gmail.com',
            msg=f"Subject:Tuesday Motivation\n\n{quote}"
        )