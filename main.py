# Connecting to Google sheets
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
from text_manupulation import *
import sys

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = '/home/rohan/Documents/savings-analyser-0b7653ad3c24.json'  #link to json file
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
records_file = '1_sBLT36bWPxKmCQXxzrxfxmwtnGiUdsxRQHQuYPdmx4'  # record file google sheet id
keywords_file = '1akibJBENCe8jmUMnNge0dTqH8G5FLjkY0CtQ3Ju-398'  # keywords file google sheet id
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
records_rows = sheet.values().get(spreadsheetId=records_file, range='A1:K1').execute()  # whenever new category gets added, this line has to be changed
keyword_rows = sheet.values().get(spreadsheetId=keywords_file, range='A:B').execute()
records = flatten(records_rows['values'])
keywords = pd.DataFrame(data=keyword_rows.get('values', []))
keywords = keywords.rename(columns=keywords.iloc[0]).drop(keywords.index[0])

# Taking input:
rw_input = sys.argv[1]
try:
    input_data = list()
    for i in rw_input.split('/'):
        input_data.append(i)    
except:
    print("There's some problem I've found in the data you've just entered. Please enter in the mentioned format.")

# saving these entered data into dictionary.
expenses = dict()  
for i in input_data:
    i = i.split(' ')
    expenses[' '.join(i[:-1])] = i[-1]  # Making sure space in the entered keyword does't gets categoried as different keyword.

## correcting irregularities in data
keywords.dropna(subset=['Keywords'], inplace=True)
keywords['Category'] = keywords['Category'].str.replace('""','')
categories = records[1:]  # This variable woud be used to print categories. hence ignoring first index i.e. column name.
### keywords['Keywords'] stores Keywords & keywords['Category'] stores Catogories from our keywords db.

# Accepting new entries (if any) from user:
import builtins
unique_keys = list()  # unique list of keys (from the data entered)
for i in expenses.keys():
    if i not in list(keywords['Keywords']):
        unique_keys.append(i)

## if we get new entries, lets take its category to be placed into
unique_categories = list()  # unique list of categories (to be asked by user)
if len(unique_keys) > 0:
    print("These are the unique keys I have found: ",list_to_string(unique_keys))
    print("Categories Avaialable: ",list_to_string(categories))
    print("What will be their categories? (add ',' in between): ")
    unique_categories = input().split(',')

# Taking Update frequency
## (Making it more convinient for the user to enter data as per preference)
freq_day = int(input("Enter number of days after you're updating the data (press 1 for today): "))

## Formatting Date
### (For putting it to our records sheet)
from datetime import datetime, timedelta 
start = datetime.today().date()  # has the current date in required format
end = (datetime.today() - timedelta(days=freq_day)).date()  
# has the date from the date we have missed the data updation process (if we have entered freq_day >1)
date_generated = list()  # listing the dates to be added in records db.
for i in range(0, freq_day):
  b = start - timedelta(days=i)
  date_generated.append(b.strftime('%d-%m-%Y'))

# Categorising the entered keywords into categories:
category_vals = dict()  # It contains categories + values entered from before.
## We have to make sure if user enters multiple keywords pointing to same category, the script adds them all.
for i,j in expenses.items():
    for z,v in enumerate(list(keywords['Keywords'])):
        if i == v:  # if 
            if category_vals.get(keywords['Category'][z+1]) == None:  # if that category appeared for first time
                category_vals[keywords['Category'][z+1]] = j
            else:  # if the category appeared for second time. We have to add it with the pre-existing value.
                category_vals[keywords['Category'][z+1]] = int(category_vals[keywords['Category'][z+1]])+int(j)

## Dividing the values amongst updation days passed (in case of multiple days, we have to divide the expenses amongst the days passed)
for i,j in category_vals.items():
  category_vals[i] = j/freq_day

# Creating Dataframes
## (This is done )