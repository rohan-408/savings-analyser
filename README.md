
Savings Analyser - Helping you to save.

{This is a simple Machine Learning system which might be used to properly and quickly analyse our expense trends.}

TABLE OF CONTENTS:
- Purpose of the Project.
- Prerequisite files you will need.
- How to setup and connect Google service account.
- Basic working of the model.
- Creating a sophesticated Dashboard in Google data studio.
- Tips and Tricks to better handle this system of apps.


-> Purpose of the Project:
The purpose of this small project was to make use of python to create a simple and quick report of our daily expenses without making much effort on updating and maintaining of a records file for saving those expense history. I am making this explaination as simple as possible so that everyone can understand and make use of this wonderful programming language, python.

This project will enable users to easily enter expenses into the records file which will be stored in thier Google drive as GSheets. Users won't have to even enter expense categories each time, instead they just have to enter keywords pointing to that category. Here's where the Machine Learning comes into play.

The records file in the system maintains a day by day logs of expense based on predefined Categories. These Categories are: Food/ Kitchen accessories, Bathroom Accessories,  Maintenance, loans/ EMI,  Medical expenses,  Upskilling/ Education, travel,  Accessories, Entertainment, & Others.


-> Prerequisite files you will need:
So basically, you would need 4 Files for this project, 3 of which can be Google workspace ones. A Records file (stored as Google Sheets), a Keywords file (stored as Google Sheets), a json file (key file for your Google service account), & a Google Data studio Dashboard.
The process of creating json file, I will explain in the next section "How to setup and connect Google service account".

So first, Let's create a Simple Keywords Google Sheets File.
It will have 2 Columns namely: 'Keywords' and 'Categories'. So the Keywords column will have the list of keywords learnt by the system and the Categories one would have the list of the category it points to.
For starters, you can add some simple and obvious entries in it for eg. keywords like maintenance (for Maintenance), loan (for loans/ EMI), travel (for Travel), etc.

For Records File, Which is our main target file where our Dialy expense logs has to be updated would have 2 types of Data, 'Date' of entry and 'category' and 'expense value' for that date.
So basically I have arranged this in vertical format with date values, and expense values as rows vs. Categories arranged in top as column.
In total, the columns in this File would be as follows: Date, Food/ Kitchen accessories, Bathroom Accessories,  Maintenance, loans/ EMI,  Medical expenses,  Upskilling/ Education, travel,  Accessories, Entertainment, & Others.
So for Each day of entry, we can have a seperate row in the records file. The Dashboard created will show a detailed report on day wise expenses so that we can better manage your finances.

In the Later stages of the using this system, you can keep records from last 5 years (deleting the rest), for year wise comparitive analysis in Google Data studio. We will create a Sample Dashboard in the last section.


-> Setup and connect Google service account:
(People who already have a google service account can skip this section) So, creating a service account is an important step in this project through which you give your python code the access to edit your both google sheets file.

Follow these steps to create a service account and get your respective json file:
- Go to 'https://console.cloud.google.com/getting-started', select your personal google account from the right hand side profile icon.
Select 'APIs and services' from the left side panel.
- (So you will land up in the Google api services dashboard) from here, select the drop down like option in top side which which lists your projects. Click on 'NEW PROJECT'.
Name the project you wanted, and click 'Create' button.
- Click on the project notification once finished.
- From the several cards you see in the dashboard, go to 'Getting Started' > Explore and enable APIs.
- Click on 'Enable APIs and services'.
- From several API options, select Google Sheets API.
Click Enable.
- Click on Create Credentials> Service Account.
- After giving appropriate name, Click 'Create'.
- From select a rule drop down, select 'Project > Editor', Continue.
(if any other options pops up, click done/continue)
- So now, Copy your service account (basically the email address you've just created) and give this id the permission to "edit" our 2 google sheets created in previous section.
- Now click onto the service account created in the Google api page. In the 'Keys' section, click on 'ADD KEY' > create new key > JSON.
This will download our required JSON file which is required for our Python code to access our service account and make changes to our Google spreadsheets.


-> Basic working of the model:
Basic architecture of this model is very easy.
Each time user enters the expense keyword with a value, it tries to match the keyword with our keyword spreadsheet, if it finds it new, it will ask for its Category name to which it best points to.
After this, it will ask for 'Frequency of the input', so it is basically asking for no. of days this expence has to be entered. This concept I have introduced this to make it more flexible to update whenever we get time even after few days. In such case, If I put no. of days = 2, this model will automatically divide the expenses into 2 days and hence, in the records file you will see 2 days which got entered, in which the expense values also gets divided into 2.

The records are added in the records file are in form of series of 0s under categories we have not expended and values only under the categories entered for the day.

In the later stages of development, I am planning to implement a NLP Algorithm in this, which can understand the meaning of the entered keywords and automatically classify it to the categories, If not, it will only ask users 1-3 options which it thinks are the best suited categories.


-> Creating Dashboard in Google data studio:
So, in this final stage of the project, we will build a simple dashboard using Google data studio.
For your reference, I have created a reference dashboard out of a randomly generated Data.
{Link: https://datastudio.google.com/reporting/ce68ff24-6286-497a-8594-e9ffa97e610c}

So first, Go to Google Data studio homepage and use the same Google account as used in all previous steps:
https://datastudio.google.com/
Lets first import our Data in Data studio.
- Click Create Button on the left > Data source
- Search for Google Sheets.
- Under All items, Find your Records google sheet file.
- (you can tick all the options) Click on Connect button.
- In the current page, you can view the data added. Check data types of each of the columns.

So, Now usually we have to create a entire new Dashboard by yourself, but there is a simple workaround.
- Click on the public copy link of the savings dashboard I have given above.
- On right side above, click on 3 dots > 'Make a copy' (this creates a copy of this dashboard and saves it in your Google drive).
- Select the records sheets file from the 'New Data source' drop down.

This dashboard was designed by me, you are free to experiment with your own designs and some more representations.


-> Tips and Tricks:
It can be overwhelming for non technical people to handle complex system of apps like the one I have created. For this, I hereby present you some tricks by which the user can run this file from any device and daily update the records in matter of few seconds.

1) For cross device usage-
For this, we need to create a new google colab file from your google drive page. Then paste every cell of our .ipynb file into this. 
After doing this, we can access the Google drive straight from colab itself. From clicking on Files icon on the left, there is a option to connect to drive. After this, just upload the .json file to drive.
From colab, browse your drive files and look for the .json file (if in case it is not visible, refresh the drive), click on the 3 dots and copy the location of .json file.
Paste this location in the code where it asks for json location.

The above process connects the code to our json file so that we don't have to run it on our local system, and also if running on cloud we don't have to upload it again and again. We can run Google colab from pc and from mobile devices, just bookmark the url your colab and you should be good to go.

2) For Easy access to colab and Dashboard-
Whether you prefer mobile or pc for runing this project, I prefer creating a couple of webapps for easy access to those files. Create a webapp for your Google colab file and another for your Dashboard file in Google data studio.

3) Effective management of daily data-
So, it is sometimes not possible for users to update the expenses on the spot. What I do is, keep the notification of the amount deducted and whenever I get some time, I note it in my local notes app. At the end of the day, I just need to paste this into the code for updation.

In case of updating for multiple days, we can follow this same process as our model will aggregate those keywords based on the corresponding categories and ask for no. of days data needs to be updated.
