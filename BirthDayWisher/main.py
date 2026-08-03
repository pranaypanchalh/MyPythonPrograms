import smtplib

myEmail = "pranay.ali118@gmail.com"
myEmailPassword = 
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=myEmail,password=)