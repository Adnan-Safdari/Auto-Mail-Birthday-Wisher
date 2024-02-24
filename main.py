import smtplib
import datetime as dt
import credentials
import random
import pandas as pd

df = pd.read_csv('birthdays.csv')

birthday = str(dt.datetime(year=int(df['year']), month=int(df['month']), day=int(df['day'])))
birthday = birthday[5:10]  # Extracting month and date

live_time = str(dt.datetime.now())
live_time = live_time[5:10]  # Extracting month and date

if live_time == birthday:
    letter_index = random.randint(1,3)
    with open(file=f"letter_templates/letter_{letter_index}.txt") as file:
        data = file.read()
        email_body = data.replace("[NAME]", str(df["name"][0]))

    # Importing the email and password from credentials.py
    my_email = str(credentials.my_email)
    password = str(credentials.password)
    email_subject = credentials.email_subject
    recipient_email = df['email'][0]

    # Establishing connection and sending the final email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Securing our email with encryption
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_email,
                            msg=f"Subject:{email_subject}\n\n{email_body}\n")


