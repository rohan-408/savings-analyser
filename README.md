# Savings Analyser - Helping you to save
## Aim: 
This is a simple Machine Learning system that might be helpful to properly and quickly analyze your expense trends.

## TABLE OF CONTENTS:
- Purpose of the Project.
- Prerequisite files you will need.
- How to set up and connect Google service account.
- Basic working of the model.
- Creating a sophisticated Dashboard in Google Looker Studio.
- Tips and Tricks to better handle this system of apps.

## Purpose:
The purpose of this small project was to make use of Python to create a simple and quick report of our daily expenses without making much effort to update and maintain a records file for saving expense history. I am making this explanation as simple as possible so that everyone can understand and make use of this wonderful programming language, Python.

This project will enable users to easily enter expenses into the records file which will be stored in Google Sheets. Users won't have to even enter expense categories each time, instead, they just have to enter keywords/ things pointing to that category. Here's where Machine Learning comes into play.

The records file in the system maintains day-by-day logs of expenses based on predefined Categories. These Categories are Food/ Kitchen Accessories, Bathroom Accessories,  Maintenance, loans/ EMI,  Medical expenses,  Upskilling/ Education, travel,  Accessories, Entertainment, & Others.
So the user just needs to enter the thing on which they spent money, followed by value.

A Dashboard, in Google Looker Studio, gives a detailed Picture of the expense, and savings done by the user. It gives out details like what categories, the value spent, trend of expenditure, savings (based on current salary), etc.

The goal is to analyze the expense trend and inspire to Save some more.

## Dependencies:
You would need 5 Files for this project. 4 of which can be Google Workspace ones.
1.  A Records file (in Google Sheets)
2.  A Keywords file (in Google Sheets)
3.  A JSON file (key file from your Google service account)
4.  Google Looker Studio Dashboard (for Visualizing Results)
5.  A Python script to connect all these and run our Project.

The process of creating JSON file, I will explain in the next section `How to set up and connect Google service account`.

## Getting Started Guide
- Let's create the Keywords Google Sheets File. 

Create a Google Sheets file named "Savings analyzer Keywords". It will have 2 Columns namely: `Keywords` and `Categories`.

In this, The `Keywords` column would have the list of keywords learned by the system (or added manually) and the `Categories` would have the list of the category it must point to. A sample keywords file (csv format) is attached in git for reference.

- Getting our Records file Ready.

Create a Separate google sheets file named "Savings analyzer Records". This is our main target file where our daily expense logs has to be updated would have 2 types of Data, 'Date' of entry and 'category' and 'expense value' for that date.

Here, for Google data studio to understand our data, we need to create the file as per a special format. So basically, the columns arranged in a format as follows: `Date, Food/ Kitchen accessories, Cleaning Accessories,  Maintenance, loans/ EMI,  Medical expenses,  Upskilling/ Education, travel,  Accessories, Entertainment, Others`.
A sample records file would be attached for reference (csv format).

So for Each day of entry, we can have a separate row in the records file. The Dashboard created will show a detailed report on day wise expenses so that we can better manage your finances.

## Setup and connect Google service account:
(People who already have a google service account can skip this section)
So, creating a service account is an important step in this project through which you give your Python code the access to edit your both google sheets file. Service Account gives you ability to create a API that can be used to edit any google workspace file with  a bot.

Follow these steps to create a service account and get your respective JSON file:
- Go to [Google Cloud Console](https://console.cloud.google.com/getting-started), select your personal google account from the right hand side profile icon.
- (You'll land up in the Google API services dashboard) From here, select the drop down like option in top side which which lists your projects. Click on `NEW PROJECT`.
Name the project you want, and click `Create` button.
- Click on the project notification once finished.
- From the several cards you see in the dashboard, go to 'Getting Started' > `Explore and enable APIs`.
- Click on `Enable APIs and services`.
- From several API options, select 'Google Sheets API'.
Click `Enable`.
- Click on `Create Credentials`> Service Account.
- After giving appropriate name, Click `Create`.
- From select a rule drop down, select 'Project > Editor', Continue.
(if any other options pops up, click done/continue)
- So now, Copy your service account (basically the email address you've just created) and give this id the permission to edit our 2 google sheets created in previous section.
- Now click onto the service account created in the Google API page. In the `Keys` section, click on `ADD KEY` > create new key > JSON.
This will download our required JSON file which is required for our Python code to access our service account and make changes to our Google spreadsheets.
(Make a note of this new Email ID (service ID) created.)

## Connecting your Service Account to Google Sheet:
Once you've created the account, its super easy to link it to the files in google sheets. Simple go to the sheets file, Click `Share` Button > Add that email ID you've just created and click `Share`. Do the same for other sheet as well.

Also, Do make a note of the Google sheet id of these files. It would be required in the Python code. Where to find it?
Its simply in the URL of those files, the portion between `/d/` and `/edit` is your sheet ID.

## Working
Basic architecture of this model is very simple.
Each time user enters the expense keyword with a value, it tries to match the keyword with our keyword spreadsheet, if it finds it new, it will ask for its Category name to which it best points to.
After this, it will ask for 'Frequency of the input', so it is basically asking for no. of days this expense has to be entered. This concept I have introduced this to make it more flexible to update whenever we get time even after few days. In such case, If I put no. of days = 2, this model will automatically divide the expenses into 2 days and hence, in the records file you will see 2 days which got entered, in which the expense values also gets divided into 2.

The records are added in the records file are in form of series of `0`s under categories we have not expended and values only under the categories entered for the day.

{In the later stages of development, I am planning to implement a NLP Algorithm in this, which can understand the meaning of the entered keywords and automatically classify it to the categories, If not, it will only ask users 1-3 options which it thinks are the best suited categories.}

## Creating Dashboard in Google data studio:
So, in this final stage of the project, we will build a simple dashboard using Google Looker studio [Link](https://lookerstudio.google.com/overview).

I have attached a snapshot of the final dashboard we're going to create in this project. This would not only give a overall assessment of our expense, but also help us save more.

Now, To create such a beautiful Dashboard using this tool, let's first visit its homepage from [This link](https://lookerstudio.google.com/navigation/reporting).

Steps for creating our Dashboard:
- Click `Create` Button on the left > "Data source"
- Search for Google Sheets.
- Under All items, Find your Records google sheet file.by 
- (you can tick all the options) Click on `Connect` button.
- In the current page, you can view the data added. Check data types of each of the columns.

Let's add elements into this Dashboard:
{Adding ScoreCards}
- From `Add a Chart` option from top menu > Add a Scorecard (compact one would be a better choice as we don't want to unnecessarily complicate data for us.
Drag to a desired place and click once.
- Now a new panel would be opened on your Right, It's called Preference Tab. Here you can adjust and customize everything related to that selected card/ visualization element.
- In here, Keep the Date Range Dimension as `Date` column itself (It would most probably select it automatically).
- Under `Metric`, Select The first category column (or any other based on your preference). You'll see the operation to be performed on this column is automatically selected, which is SUM.
You'll see, the card now has a number which is sum of all values for that selected category column. If we don't have any, it would simply have 0.
- Similarly create more scrorecards for all our categories.
(If you want, you can customize them at your own preference. Drag them and align them in single line or change their colours, etc.)

{Adding Date Filter}
- From Add a Control option in top menu, select `Date range Control`.
- Place it on top of the dashboard.

{Creating a Total Expense card}
- From Add a Chart > select a `Gauge` ('Gauge with ranges' would be preferable)
- Coming to preference tab, select the Metric option > Select ADD FIELD (as we want the total of all the categories in this visualization, we have to add a new field in this existing dataset. It can be done directly using Looker studio)
- Under `Name`, Enter "Total Expense". 
- Under `Formula`, Start adding names of categories one by one adding a `+` in between like: Accessories+Food/ Kitchen accessories+loans/ EMI+....
The interface will autofill your typing, so don't worry about spelling errors here.
Click `Apply` button when finished.
- You could now see the total value spent in this selected date range.
But we actually need this value subtracted from our current salary to calculate Savings.
- In the same preference tab, Go to `Style` section > Go little down and you'll find `Axis` > Under Axis Max value, add your current salary. (Shh!, keep it secret...)

{Creating Trend line of Expenses}
- From Add a Chart > select Line > `Line Chart`.
- Under Preference tab > Dimension > select the pre-existing selection and change it to `Date`.
- Now go down to Metric > select the pre-existing option and change it to any of our category column.
Now below that, Click on Add metric > and one by one select all other categories which we have.

## Future Plans:
In future, I am planing to add a bit of NLP in here to make the process of entry more streamlined and simple. So Stay Tuned.
