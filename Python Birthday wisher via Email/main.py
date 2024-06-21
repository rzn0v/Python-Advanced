import pandas as pd
import datetime as dt
import random
import smtplib

data = pd.read_csv("birthdays.csv")
now = dt.datetime.now()
month = now.month
day = now.day
today = (month,day)
my_gmail = "yourmail@gmail.com"
password = "yourpwd"
letters = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]

birthday_dict = {(row["month"],row["day"]):(row["name"],row["email"],row["year"],row["month"],row["day"]) for (index, row) in data.iterrows()}
if today in birthday_dict:
    name = birthday_dict[today][0]
    recipient_email = birthday_dict[today][1]
    chosen_letter = random.choice(letters)
    with open(chosen_letter, "r") as letter:
        data = letter.read()
        data = data.replace("[NAME]", name)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail, to_addrs=recipient_email, msg=f"Subject:HAPPY BIRTHDAY!!\n\n{data}")
    