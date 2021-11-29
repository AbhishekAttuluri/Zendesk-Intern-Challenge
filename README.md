# ZENTV - ZENdesk Ticket Viewer

Name : Abhishek Attuluri </br>
Github link : https://github.com/AbhishekAttuluri

## Motivation:
I strongly believe the phrase "continuous learning" and I felt it while implementing the Zendesk Ticket Viewer as a part of the Zendesk Intern Program. I am able to design and implement the assigned project keeping the following things in mind.

1. Providing a simple user interface.
2. Following standard design principles and coding practices.
3. Implementing meaningful testcases.
4. Seperation of the required concerns.
5. Notifying user when the server is down or any other issues.</br>

This project is developed using Python 3 and Django for the backend and HTML and CSS for frontend.

## Software Requirements:
Python3 </br>
Django </br>
HTML </br>
CSS </br>
Internet Browser </br>

## Installation Instructions:

1. Clone the repository to your local terminal.
2. Open terminal and navigate to the project folder path.
3. Install python3 from https://www.python.org/downloads/ and install django using ` pip3 install Django `
4. Start the server using the command `python3 manage.py runserver`
5. Open your local browser and go to:
   http://127.0.0.1:8000/ (In the local machine)

## Usage Instructions:

### Navigation of the UI:

### PART 1:

The main UI is designed so that it can display the following components:</br>
1. The Title of the application ZENTV Zendesk ticket Viewer displaying the name of the application.</br>
2. The previous and next buttons which can navigate to the next page and previous page to view tickets.</br>
3. The list of tickets (Restricted to 25 tickets as given in instructions)to view on a specific page with the following details.</br>
**ID** :  Automatically assigned to a ticket when it is created.</br>
**Subject** : The main subject line of the ticket.</br>
**Status** : The status whether ticket is open, close or pending.</br>
**Priority** : Priority if it set for some important tickets.</br>

<img width="1440" alt="Screen Shot 2021-11-28 at 8 01 12 PM" src="https://user-images.githubusercontent.com/36640099/143794069-53668ab0-accf-4cb1-8a48-88c0ee422421.png">

### PART 2:
When ever we click the ID of a specific ticket, the details of the ticket are viewed as follows.</br>

![68FC478D-98FE-4000-A32B-3B7364566994_1_201_a](https://user-images.githubusercontent.com/36640099/143794374-13bfe03c-ad3d-4fd2-9a3c-5c217c2d51cb.jpeg)


The following components are treated important to display and hence displayed.</br>
**ID** :  Automatically assigned to a ticket when it is created.</br>
**Subject** : The main subject line of the ticket.</br>
Details of the user who requested the ticket and the time requested.</br>
Details of the specific person to whom the ticket is assigned.</br>
**Description** : The detailed description of the ticket.</br>
**Status** : The status whether ticket is open, close or pending.</br>
**Priority** : Priority if it set for some important tickets.</br>
**Tags**: The tags that are assigned to a specific ticket.</br.

In the bottom we have a Go to all tickets button which can navigate to displayed all the tickets.</br>


### PART 3:
If the page is down, the authentication details are wrong or any other issues the UI is displayed as below.</br>
**CASE 1**: If the API is not available, the following message is displayed.</br>
![79F2EC47-F49A-4A54-A37F-19B47B9F12D5_1_201_a](https://user-images.githubusercontent.com/36640099/143795362-8557e9d3-6530-45a0-9781-0f06658bd80c.jpeg)

**CASE 2**: If the authentication is failed to connect to API, the following message is displayed.</br>
![AEBE8079-A592-4C74-BD36-45D01AB76A94_1_201_a](https://user-images.githubusercontent.com/36640099/143795386-eb6fe14a-0fe6-4943-aacd-a23131ea8263.jpeg)

**CASE 3**: If the response available is invalid or if any other issues in the program, an error message stating it appears.</br>


### File structure for the project in Django:

To maintain clean and clear code so that anyone can get to know how is the projct navigation, a solid file structure is followed.</br>
The components of the project are as follows:</br>

**Templates** : Templates consist the HTML, CSS and JS parts of the project to handle the frontend.</br>
            1. home.html : This handles the home page that is displayed immediately after the page is loaded.</br>
            2. detail.html : This handles the details page of a specific ticket when we click on the ticket.</br>
            3. error.html : This handles the errors or issues like page not found, api unavailable or authentication failure.</br>

**Test** : This folder contains the testcases that are to be tested in order to check the issues when we want to run the project.
testcases.py : This file contains the testcases for the project. </br>

**settings.py**: This file contains the lookup paths for our templates, static files like images and databases if they are present in our project. Whenever we create a templates, the path is specfified in settings so that any function we write in views.py can access these templates.</br>

**urls.py**: This file specifies what to display and redirectes to a specific method in views.py based on the url in the internet browser. </br>

**views.py**: This file contains the complete application logic like connection to API and fetching data, pagination of 25 tickets as specified, navigation to next and previous pages and displaying the specific details of a ticket.</br>

**manage.py**: This is a command line utility to interact with Django application in different ways. </br>

**asgi.py and wsgi.py** : These are used for external deployment which are not used for this task. </br>

**I would further like to explain about the implementation of different code blocks used in th project in detail during the interview.**

## Testing the project:

In order to run the testcases, navigate to the project folder and run the command `python3 manage.py test`

**If all the test cases are running and if there are no issues, the following message appears.**

System check identified no issues (0 silenced).

Ran 5 tests in 1.762s

OK

**If any of the testcases fail due to errors, the following message appears displaying number of errors.**

Error message

Ran 5 tests in 1.959s

FAILED (failures=1) 


