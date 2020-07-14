<p align="center">
    <img src='https://github.com/sammydowds/django-rest-automate-pm/blob/master/djangorestautomatepm/ground_control.png' width="300" height="300"/>
</p>

Table of Contents
======================

* [What is Ground Control?](#what-is-projectile)
* [End Points](#end-points)
* [Models](#data-structure)
* [File Structure](#file-structure)
* [Running Tests](#running-tests)
* [Licensing](#license)

## What is Ground Control? 
Ground Control is a REST API for storing and acessing project data. That includes storing phases related to projects, as well as how those phases change over time in the form of logs. 

The entire structure revolves around Projects (and their IDs). 

The intent is to create a platform that 3rd parties can integrate to with new applications and streamline/improve the user experience of managing projects. 

## End Points 
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods. Endpoints should be logically organized around collections and elements, both of which are resources.

Endpoint | HTTP Method | CRUD Method | Result
-- | -- | -- | -- | -- | --
`projects` | GET | READ	| Get all projects associated with user
`phases` | GET | READ | Get all phases associated with user's projects
`log`     | GET | READ | Get all log entries associated with user's projects
`projects/create`	|POST| CREATE|	Create a project
`phase/create`	|POST |CREATE	|Create a phase
`log/create`	    |POST |CREATE	|Create a log entry
`projects/update/:id` |PATCH |UPDATE| Update a Project
`phase/update/:id` |PATCH |UPDATE |Update a Phase 
`projects/delete/:id` |DELETE |DELETE| Delete a Project
`phase/delete/:id` |DELETE |DELETE |Delete a Phase  
`signup/user`     |POST |CREATE| Create a user
`api/token` | POST | CREATE | Validate user and create token (JWT) - used for login

## Models 
    Projects
    {
        "id": 0,
        "name": "Custom Web App: Fortune 100",
        "company": 0,
        "complete": false,
        "lastupdated": "2020-05-29"
    }
    
    Phases
    {
        "id": 5,
        "name": "Integration",
        "start": "2020-04-29",
        "end": "2020-04-29",
        "people": null,
        "projectId": 0,
        "active": false,
        "complete": false
    }

    Log
    {
        "id": 0,
        "description": "Something was delayed by 1 day.",
        "notes": "Personal note", 
        "projectId": 0,
        "timestamp": "2020-06-06"
    }

## File Structure 

## Running the tests

## Built With

* Django 
* Django REST Framework 
* Django Simple JWT

## Authors

* **Sammy Dowds** - *Initial work* - [Profile](https://github.com/sammydowds)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments
