# Introduction

I want to build an application that could be a household management app. The features would include a calendar to add appointments to, a board like a Trello or MSFT Planner board to add tasks and goals to, and a basic daily habit tracker if it fits. My basic app will accept new appointments and tasks and show appointments and tasks.

# Endpoints

### Appointments
```
POST /appointments
{
  "title": "Doctor's Office",
  "date time": "YYYY-MM-DD hh:mm:ss",
  "address": "3921 North 44th St, Bellevue WA 12345",
  "description": "Chiro appointment for shoulder"
}

Response:
{
  "id": 1,
  "title": "Doctor's Office",
  "date_time": "YYYY-MM-DD hh:mm:ss",
  "address": "3921 North 44th St, Bellevue WA 12345",
  "description": "Chiro appointment for shoulder"
}

GET /appointments/1
{
  "id": 1,
  "title": "Doctor's Office",
  "date time": "YYYY-MM-DD hh:mm:ss",
  "address": "3921 North 44th St, Bellevue WA 12345",
  "description": "Chiro appointment for shoulder"
}
```
### Tasks
```
POST /tasks
{
  "title": "Clean the house",
  "due_date": "YYYY-MM-DD",
  "assignee": "Daniel Classon"
  "description": "kitchen, bedroom, kids rooms, bathrooms, sweep/mop floors"
  "group": "Today's Tasks"
  "completed": false
}

Response:
{
  "id": 1
  "title": "Clean the house",
  "due_date": "YYYY-MM-DD",
  "assignee": "Daniel Classon"
  "description": "kitchen, bedroom, kids rooms, bathrooms, sweep/mop floors"
  "group": "Today's Tasks"
  "completed": false
}

GET /tasks/1
{
  "id": 1
  "title": "Clean the house",
  "due_date": "YYYY-MM-DD",
  "assignee": "Daniel Classon"
  "description": "kitchen, bedroom, kids rooms, bathrooms, sweep/mop floors"
  "group": "Today's Tasks"
  "completed": false
}
```

# Database Design

Database: household_db

    Table: appointments
    Columns: date, time, title, body, primary_key id
	  
    Table: tasks
		Columns: title, due date, body, assigned user, task group, primary_key id