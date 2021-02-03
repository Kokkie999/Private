import datetime as dt
import smtplib
import random

my_email = "iwan.udemy@gmail.com"
password = "Kokkie#1"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs='iwan.udemy@yahoo.com',
            msg=f"Subject:Motivational quote\n\n{quote}"
        )
