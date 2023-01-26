# TO-meetings-DO

## General description of the project

Browser extension for To-Do lists that adds the meetings and scheduled tasks of all your e-mails.

It has the function of creating a To-Do list in which new items can be added throughout the day and new activities can be scheduled using a calendar. The list automatically synchronizes meetings and scheduled tasks from the user's linked emails.  Meetings or activities that have an assigned hour are displayed as pop-up notifications.

## How to install the project

Create a virtual env and install the next libraries  

- asgiref==3.6.0
- Django==4.1.5
- djangorestframework==3.14.0
- psycopg2==2.9.5
- psycopg2-binary==2.9.5
- pytz==2022.7.1
- sqlparse==0.4.3
- tzdata==2022.7

On your project location run the command: 
```
python manage.py runserver 
```
