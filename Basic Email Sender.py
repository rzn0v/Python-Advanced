import smtplib

my_gmail = "youremail@gmail.com"
password = "yourpassword" #create an app password in your gmail account and use it else it wont work

connection = smtplib.SMTP(host="smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_gmail, password=password)
connection.sendmail(from_addr=my_gmail, to_addrs="ushareno@gmail.com", msg="Subject:Your Subject\n\nThis is a test mail send by using python code")
connection.close()