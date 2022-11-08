import smtplib
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
    email_address = '100daysofpythonbyme@gmail.com'
    email_password = 'beifvgxozxuddlxb'
    connection.login(email_address, email_password )
    connection.sendmail(from_addr=email_address, to_addrs='iwontellmyemail@gmail.com',
    msg="subject:Hello Bero \n\n Welcome to the jungle")