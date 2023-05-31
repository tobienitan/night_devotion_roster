
'''  This program creates a DataFrame of the morning devotion roster for the month and saves it in a excel sheet'''
from datetime import datetime, time
import random


import pandas as pd
data =  pd.read_csv('email_data.txt')
list_of_names_and_Emails = list(zip(data.Name, data.Email))
random.shuffle(list_of_names_and_Emails)
print(list_of_names_and_Emails)

month = datetime.now().month
year = datetime.now().year
import itertools
names = itertools.cycle(list_of_names_and_Emails)
import calendar
num_days = calendar.monthrange(year, month)[1]
days = range(1, num_days + 1)

allocation = {day: next(names) for day in days}
present_month = datetime.now().strftime('%B')

'''  the code below changes the python dictionary to a excel sheet'''
#df = pd.DataFrame(allocation) # converts the dictionary to a pandas dataframe


df = pd.DataFrame(data=allocation)


#convert into excel
df.to_csv('night_devotion', index=False, sep=':')
# # Create an Excel writer using pandas
# writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
#
# # Write the DataFrame to an Excel sheet
# df.to_excel(writer, sheet_name=f'Devotion Names for the month of {present_month}', index=False)
#df.to_excel(excel_writer='xlsxwriter' ,sheet_name='Devotion timetable', index=False)

print(df)