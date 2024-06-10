import smtplib
import random
import datetime as dt

my_gmail = "yourgmail@gmail.com"
password = "yourpwd"
date = dt.datetime.now()
day = date.weekday()
if day == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail, to_addrs="recipient@gmail.com", msg=f"Subject:Monday Motivational Quote\n\n{quote}")

else:
    print("It's not Monday Yet!")
