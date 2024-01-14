
def flatten(t):
    return [item for sublist in t for item in sublist]

"""**2)** for Converting a list into a string (for easy to read print statements)"""

def list_to_string(a):  # for printing a list as single string
  sam = ''
  for i in a:
    sam = sam+', '+i
  return sam

"""# Connecting to DB"""

from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import numpy as np

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'savings-analyser-9898989.json'  #pathway to your json file

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

records_file = '{google_sheets_record_file_id}'  # record file google sheet id
keywords_file = '{google_sheets_keyword_file_id}'  # keywords file google sheet id

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()
records_rows = sheet.values().get(spreadsheetId=records_file, range='A1:K1').execute()  # whenever new category gets added, this line has to be changed. Add the column details here
keyword_rows = sheet.values().get(spreadsheetId=keywords_file, range='A:B').execute()

records = flatten(records_rows['values'])
keywords = pd.DataFrame(data=keyword_rows.get('values', []))
keywords = keywords.rename(columns=keywords.iloc[0]).drop(keywords.index[0])

"""# Taking Input"""

#title
input = """face wash 94
food 70
salon 150
gift 175
medicine 620
travel 200"""  # add expense keyword followed by value. For Multiple entries, use next line

sentences = input.split('\n')
expenses = dict()
text,integer = list(),list()
for i in sentences:
  a = i.split(' ')
  text_sub = ''
  for j in a:
    try:
      integer.append(int(j))
    except:
      text_sub = text_sub+j+' '
  text.append(text_sub.rstrip())
expenses = {text[i]: integer[i] for i in range(len(text))}

"""# Text processing

### correcting irregularities in data
"""

keywords.dropna(subset=['Keywords'], inplace=True)

keywords['Category'] = keywords['Category'].str.replace('""','')

# categories in consideration
categories = records[1:]

"""## Accepting new entries by user"""

import builtins
unique_keys = list() # unique list of keys
unique_categories = list()  # unique list of categories
for i in expenses.keys():
  if i not in list(keywords['Keywords']):
    unique_keys.append(i)

# if we get new entries, lets take its category to be placed into
if len(unique_keys) >= 1:
  print("These are the unique keys: ",unique_keys)
  print("Categories:",list_to_string(categories))
  print("What will be their categories? (add double space in between): ")
  unique_categories.append(builtins.input().split('  '))
if unique_categories:
  unique_categories = flatten(unique_categories)

"""## Taking Update frequency"""

# update frequency is the number of days for which we want our data to entered in records.
import builtins
freq_day = int(builtins.input("Enter number of days after you're updating the data (press 1 for today): "))

"""## Formatting Date

Generating list of Dates for the no. of days records needs to be added
"""

from datetime import datetime, timedelta 
start = datetime.today().date()
end = (datetime.today() - timedelta(days=freq_day)).date()
date_generated = list()
for i in range(0, freq_day):
  b = start - timedelta(days=i)
  date_generated.append(b.strftime('%d-%m-%Y'))

"""Creating single dictionary containing category and expense"""

# first extracting details from unique items
category_vals = dict()
for i in expenses.keys():
  for j,v in enumerate(unique_keys):
    if i == v:
      try:
        category_vals[unique_categories[j]] = category_vals[unique_categories[j]] + expenses[i]
      except:
        category_vals[unique_categories[j]] = expenses[i]

#for general items
for i,v in expenses.items():
  if i not in unique_keys:
    try:
      category_vals[keywords[keywords['Keywords'] == i]['Category'].iloc[0]] = category_vals[keywords[keywords['Keywords'] == i]['Category'].iloc[0]] + v
    except:
      category_vals[keywords[keywords['Keywords'] == i]['Category'].iloc[0]] =  v

"""Dividing the values amonst days"""

for i,j in category_vals.items():
  category_vals[i] = j/freq_day

"""# Creating Dataframes

For Keywords
"""

keywords_final = pd.DataFrame({'Keywords':unique_keys,'Category':unique_categories})

"""For Records"""

row = [0] * len(categories)

for i, v in enumerate(categories):
  for j in category_vals.keys():
    if v == j:
      row[i] = category_vals[j]

category_final = pd.DataFrame()
category_final['date'] = date_generated
category_final[categories] = row

"""# Pushing Values to GSheets"""

request_records = sheet.values().append(spreadsheetId=records_file, range='A:J', valueInputOption= "USER_ENTERED", insertDataOption= "INSERT_ROWS", body= {"values": category_final.values.tolist()}).execute()

if len(keywords_final) >=1:
  request_keywords = sheet.values().append(spreadsheetId=keywords_file, range='A:B', valueInputOption= "USER_ENTERED", insertDataOption= "INSERT_ROWS", body= {"values": keywords_final.values.tolist()}).execute()
