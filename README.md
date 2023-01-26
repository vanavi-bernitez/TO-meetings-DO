# TO-meetings-DO

## General description of the project

Browser extension for To-Do lists that adds the meetings and scheduled tasks of all your e-mails.

It has the function of creating a To-Do list in which new items can be added throughout the day and new activities can be scheduled using a calendar. The list automatically synchronizes meetings and scheduled tasks from the user's linked emails.  Meetings or activities that have an assigned hour are displayed as pop-up notifications.

## How to install the project

1. Create a general folder for the project. 
2. Create a virtual env inside the project folder
3. Install the next libraries inside the virtual env via PIP

- python==3.10.6
- asgiref==3.6.0
- Django==4.1.5
- djangorestframework==3.14.0
- psycopg2==2.9.5
- psycopg2-binary==2.9.5
- pytz==2022.7.1
- sqlparse==0.4.3
- tzdata==2022.7

4. Clone the current repository
5. Activate the virtual env inside your project folder and run the next command on the terminal. This will deploy the project locally
```
python manage.py runserver 
```

## All features

Create user

Login user

Configuration of the list and linking of the mail calendars.

List of the day's activities with meetings and tasks from all calendars.
- Create new item 
- Delete existing item
- Modify existing item
- The items of the calendars are not modifiable and are of different colors depending on the e-mail service they come from.

Pop-up notifications of the next task or meeting that has an assigned time.

## Features until date

CRUD API for user registration

## Postman test collection 


