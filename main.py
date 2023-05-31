''' this program gets a list of the allocated roaster and sends email remainder on the day before'''
from datetime import datetime, time
import time as t
import random
from devotion_timetable import allocation


import pandas as pd
import smtplib
from email.message import EmailMessage
import ssl

print(list(allocation.keys())[2])
print(allocation)

print(allocation[1][0])
for days in allocation:
    if datetime.now().day == list(allocation.keys())[days-1]:
        print(datetime.now())
        print(days)

        file_path = 'devotion_letter.txt'
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace('[NAME]', allocation[days][0])

        my_email = 'enitanoluwatobi09@gmail.com'
        password = 'rdjlsdecvkwsieig'
        receiver = allocation[days][1]
        body = contents
        subject = 'Devotion'

        em = EmailMessage()
        em['From'] = my_email
        em['To'] = receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(my_email, password)
            smtp.sendmail(my_email, receiver, em.as_string())

#
# day_of_week = dt.datetime.now().weekday()
#
# '''our plan in this code is to send motivational emails on monday using the quotes txt given directly to email address
#    according to datetime module monday is day zero, tuesday is day one  and soon and so forth'''
# with open('quotes.txt') as quotes:
#     quote_list = quotes.readlines()
#     print(quote_list)  # note you can access your quote outside your with block
#
# if day_of_week == 1:
#     monday_quote = choice(quote_list)
#     print(monday_quote)
#
#     my_email = 'enitanoluwatobi09@gmail.com'
#     password = 'rdjlsdecvkwsieig'
#     receiver = 'damilare_enitan@yahoo.com'
#     body = monday_quote
#     subject = 'Moltivational Quote Of The Day'
#
#     em = EmailMessage()
#     em['From'] = my_email
#     em['To'] = receiver
#     em['subject'] = subject
#     em.set_content(body)
#
#     context = ssl.create_default_context()
#
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#         smtp.login(my_email, password)
#         smtp.sendmail(my_email, receiver, em.as_string())



#
# while True:
#     if list_of_names == choosen_name:
#         choosen_name.clear()
#     devotion_person = choosing_name(list_of_names, choosen_name)[0]
#     print(devotion_person)
#     print(list_of_names, choosing_name(list_of_names, choosen_name)[1])
#     # now = datetime.now()
    # if choosen_name == list_of_names:
    #     choosen_name.clear()
    # if now.time() == time(18, 0):
    #     devotion_person = choosing_name(list_of_names, choosen_name)[0]
    #
    #     today = datetime.today().strftime('%Y-%m-%d')
    #     print('Hello, today is', today)
    # t.sleep(60)

