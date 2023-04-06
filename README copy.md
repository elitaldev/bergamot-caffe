# bergamot cafe - Introduction

**bergamot cafe** this website is developed using Django Framework as part of Portfolio Project 4 for my Full Stack Software Development at Code Institute.

> It targets **customers** of cafe, where user can view the menu and the prices. the customer can view the menu images.
when they log in they would be able to choose a diffrent type of items from the menu and make there way to the payment page.  



You can view the live site here:- https://incredible-india.herokuapp.com/


![mockup](assets/mockup.jpg)

----

## [Content](#content)
- [bergamot cafe - Introduction](#)
  - [User Experience - UX](#user-experience---ux)
    - [Site Aims](#site-aims)
    - [Agile Methodology](#agile-methodology)
      - [Tasks](#tasks)
  - [Design](#design)
    - [Colours](#colours)
    - [Typography](#typography)
    - [Imagery](#imagery)
    - [Wireframes](#wireframes)
  - [Database Diagram](#database-diagram)
  - [Features](#features)
    - [Home Page](#home-page)
      - [Navbar](#navbar)
      - [Hero Image](#hero-image)
      - [Destination Section](#destination-section)
      - [Footer](#footer)
    - [User Page](#user-page)
    - [About Page](#about-page)
    - [Register](#register)
    - [Login](#login)
    - [Destinations](#destinations)
    - [Search Button](#search-button)
    - [Alert Messages](#alert-messages)      
  - [Admin Panel/Superuser](#admin-panelsuperuser)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Django Packages](#django-packages)
    - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
    - [Bugs](#bugs)
      - [Fixed Bugs](#fixed-bugs)
      - [Unfix Bugs](#unfix-bugs)
     - [Deployment](#deployment)
      - [Creating the Django project](#creating-the-django-project)
      - [Set up Environment Variables](#set-up-environment-variables)
      - [Final Deployment](#final-deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Information Sources / Resources](#information-sources--resources)
  - [Acknowledgement](#acknowledgement)

-----

# User Experience - UX

## Site Aims

* bergamot cafe is a cafe website mainly meant to explore the iranian food with a best quality and a good user experience.
* The site aims to provide user with a visually pleasing and informative website that is intuitive to use and easy to navigate.
*  this website gives users the easiest way to make theie order online.
* the website offers diffrent type of foods and drinks and users can make payment by cash or paypal.


## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board. Through the use of the Kanban board in the projects view in Github, the project was divided into a few different sections: 

* To Do- (All the User stories were initially entered in the 'To Do' column)
* In Progress- (then during development story they were moved into the 'In Progress' column)
* Done- (and then finally they get moved into 'Done' once the development completes)

Please find my Kanban Board with my user stories [here](https://github.com/users/jyotiyadav2508/projects/3/views/1).



#### Related User Stories:
* As a site user I can easily see the purpose of the site from the landing page so that I can see if the site is relevant to my needs.
* As a site user I can view a list of destinations which can take me to the diffrent pages. 
* As a site user I can view a diffrent type of food and drink to order.
* As a site user I can click on submitting my order to going back to the home page.
* As a site user I can use a search bar to search for a specific food, drink, dessert i am looking for.



#### Related User Stories:
* As a site user, I can register and submit my order.
* As a registered user, I can login and logout of the site so that I can access my content.
* As a site user, I can view my order history and total amount of products.
* As a site user, I can pay with my own paypal account.



## Tasks

The tasks for the website development process was closely followed as mentioned in CI's Django module "I Think Therefore I Blog" walkthrough project. The task is generally the developers step towards preparing the app.
The tasks that I have followed during the development phase were carried out in this order.

**Before Project Inception**

- Design ERD and Data 
- Create Repository in GitHub
- Create Project, User Stories and prepare Kanban Board

**Creation of Project in GitPod**

- Create the django project. Check details in [deployment-section](#deployment)
- Deploying app to Heroku - Details in [deployment](#deployment) section
- Create Database Models
	- Set up models.py file in "blog" directory
- Build Admin site
- Set up Templates
	- Create base.html - Navbar and Footer content, which gets extended to all the other template files
	- Add responsiveness to navigation and footer
  - Create index.html, view and style
	- Set up template file features with views.py and urls.py
  - about.html (Description about bergamot cafe)
  - order-confirmation (to submit your order)
  - (to allow user to edit his post)
  - naviation.html (to allow user to get access to other pages )
  - Install Allauth for sign in, sign up and sign out templates with-  pip3 install django-allauth 
  - Install crispy-forms to add styles to Django account templates with-  pip3 install crispy-bootstrap5
  - Final Deployment steps

-----



## Design

### Colours

The colour scheme has considered based on easy accessibility for all and have been consistently maintained throughout the website. The colours were modified using 

![Color Palette](/coderscafe/cafe/assets/image/cooler.png)

### Typography

Fonts were imported using Google Fonts. Roboto was used throughout with a backup of kurale, sans-serif. It was chosen for easy readability for users.

### Imagery

All the imagery is related to the Indian tourist destination and website design. Some images including carousel are static. The remaining imagery was uploaded by the author to the database.

### Wireframes

The wireframes for this projected were generated using canva. 
![Wieframes for menu](/coderscafe/cafe/assets/image/menu-page.png)
![Wieframes for home](/coderscafe/cafe/assets/image/home-page.png)
![Wieframes for submit](/coderscafe/cafe/assets/image/submit-page.png)
![Wieframes for about](/coderscafe/cafe/assets/image/about-page.png)
![Wieframes for paypal](/coderscafe/cafe/assets/image/paypal.png)


----

## Database Diagram

Smart Draw was used to create a database schema to visualise the types of custom models the project requires. This schema was used as a guide to what needed to be added to each model. Below is the Database structure that this project is based on. The relationship between Entities Post, Author, Destination and Comment are shown in this diagram.

![ERD Diagram](/coderscafe/cafe/assets/image/RED.png)


----

# Features

## Home Page

At the very first page, user can see a Navigation menu with a order button and a background images on the homepage. Homepage provides the user with big image of the friendly cafe and a relaxing place to spend some times with family. User do not need to be registered to view the menu. The responsive navigation bar is featured on all pages. 

![Homepage](/coderscafe/cafe/assets/image//homepage.png)

----

## Navbar

- The navigation bar is present at the top of every page and navigates all links to the respective pages.
- The navbar is fully responsive, collapsing into a hamburger menu when the screen size becomes smaller.
- The navbar has linked to three diffrent pages.
![Navbar](/coderscafe/cafe/assets/image/navbar.png)

![hamburger Navbar](/coderscafe/cafe/assets/image/burger-menu.png)




----

## Footer

- On the website footer, users can see basic information such, copyright, and cafe login.

![Navbar](/coderscafe/cafe/assets/image/footer.png)

----

## About Page

- The About Page gives, users information about the bergamot cafe with a brief discription of iranian food and culture.

![About Us](/coderscafe/cafe/assets/image/aboutpage.png)






----

## order Button 

On the top middle of the landing page, an order buttonwill take you to the order and submite your order page. input field is provided along with a button to submit. This allows the user to choose the food and make threr way to the payment.

![Search button](/coderscafe/cafe/assets/image/order-button.png)

- On the search results page, users can see posts related to their search. If there are posts for the user's search input, the user can click on the card result to go to the post detail page.

![order menu](/coderscafe/cafe/assets/image/order-menu.png)

- On the order menu page, users will see the menu images and can search what they are looking for through the search bar.

![input form](/coderscafe/cafe/assets/image/inpur-orde.png)


- users can submit their order by clicking the submit button below.

![submit button](/coderscafe/cafe/assets/image/submit-button.png)

- On the order page, users will be able to search for the item they are looking for via the search bar below.

![search bar](/coderscafe/cafe/assets/image/search-bar.png)

- when a user made their order and submited it, they shall go to the payment and pay throght paypal.

----


## Admin Panel/Superuser

- Admin accesses the project via logging into Django admin panel with a superuser id and password. The page appears as shown ![search bar](/coderscafe/cafe/assets/image/admin-page.png).
- A superuser "admin" was created for this project to manage the admin panel.
- On the Admin Panel, as an admin I have full access to CRUD functionality so I can view, create, edit, add and delete the following ones:
  - groups
  - Category
  - menu item
  - order model
- As admin I can also add menu image, approve users and change the status and give other permissions to the users.

### Admin login

- this is where admin can sign in with username and password.

 ![search bar](/coderscafe/cafe/assets/image/signin.png).



----

## Technologies Used

### Languages Used

* [HTML 5](https://en.wikipedia.org/wiki/HTML/)- Used to structure all the templates on the site
* [CSS 3](https://en.wikipedia.org/wiki/CSS)- to provide extra styling to the site
* [JavaScript](https://www.javascript.com/)- Minimum javascript was used to fade out alerts after a few seconds.
* [Python](https://www.python.org/)- To provide the functionality to the site. Packages used in the project can be found in requirements.txt

### Django Packages

* [Cloudinary](https://cloudinary.com/)- Was used to host the static files and media for the site.
* [Dj_database_url](https://pypi.org/project/dj-database-url/)- To parse the database URL from the environment variables in Heroku.
* [Psycopg2](https://pypi.org/project/psycopg2/)- As an adaptor for Python and PostgreSQL databases.
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)- For authentication, registration, account management.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)- To style the forms.

### Frameworks - Libraries - Programs Used

* [Django](https://www.djangoproject.com/) was used as the framework for the back-end logic of the project. Django enables rapid and secure development.
* [Bootstrap](https://getbootstrap.com/)- Used to style the website, add responsiveness and interactivity.
* [Git](https://git-scm.com/)- Used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
* [GitHub](https://github.com/)- Used to store the project's code after being pushed from Git.
* [PostgreSQL](https://www.postgresql.org/)- Database used through ORM.
* [Google Fonts:](https://fonts.google.com/) used for the Kurale, serif font
* [Font Awesome:](https://fontawesome.com/) was used to add icons for DJANGO and UX purposes.

-----



## Testing

### Validation
I used the following validation tools to validate CSS. Below the link of TESTING.md file, which includes all validation results.  

- CSS using [Jigsaw CSS validator](/coderscafe/cafe/assets/image/w3%20css.png)


### Manual Testing
Testing has taken place continuously throughout the development of the project. Each view was tested regularly. When the outcome was not as expected, debugging took place at that point. An exhaustive list of features were checked on different devices and browsers. They were performed and their scrrenshots can be found in the features section on how the distinct features render. All clickable links redirect to the correct pages.

- Link for TESTING.md file:- [Testing Results Here](TESTING.md)

----

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| In menu page, I had issue uploadind images.| I finally  manged to fixed it going through out my downloaded files. |
| I had issue with hovering on the striped table  | After searching on w3 school website and going through bootstrap I was able to fix the problem. |
| I had problem seprating two card in my dashboard  | Copy code from bootstrap alert and customized it.|
| I had small issue positioning my logo image to the bottom left of the page | I did manage to put it in right place after searching and with help of my teacher  |


| **Unfix Bug** |
| ----------- | 
| I have a unsolved bug in making my website responsive in all type of screen<br><summary>unfortunately i couldn't find a way to fix this.but I will try to find a solution for my future project.</summary>

----


[Back to top ⇧](#content)


## Deployment

### 1. Creating the Django Project
* Go to the Code Institute Gitpod Full Template [Template](https://github.com/Code-Institute-Org/gitpod-full-template).
* Click on `Use This Template` button, then create new repository.
* Name our repository and click on `Create repository from template` button.
* Once the template is available in your repository click on `Gitpod` button.
* When the image for the template and the Gitpod are ready, open a new terminal to start a new Django App.
* Install Django and gunicorn: `pip3 install 'django<4' gunicorn`.
* Install supporting database libraries dj_database_url and psycopg2 library: `pip3 install dj_database_url==0.5.0 psycopg2`.
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`.
* Create file for requirements: `pip freeze --local > requirements.txt`.
* Create project:`django-admin startproject project_name .`.
* Create app: `python manage.py startapp app_name`.
* Add app to list of `installed apps` in settings.py file: `'app_name'`.
* Migrate changes: `python manage.py migrate`.
* Test server works locally: `python manage.py runserver`.
* If the app has been installed correctly the window will display- The install worked successfully! Congratulations!



### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory.
* Add env.py to the .gitignore file.
* In env.py import the os library.
* In env.py add `os.environ["DATABASE_URL"]` = "Paste the link copied from Heroku DATABASE_URL".
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`.
* In Heroku Settings tab Config Vars enter the same `SECRET_KEY` created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### Functions
* In my Django 'views.py' file:

![search bar](/coderscafe/cafe/assets/image/views.py.png)

* the below code shows how to costomize the paypal button.
 ![search bar](/coderscafe/cafe/assets/image/payment-confirmation.png)




* Commit and push the code to the GitHub Repository.


### 6. Final Deployment
In the IDE:
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the `DISABLE_COLLECTSTATIC` value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

----

[Back to top](#content)

# Credits


## Learning Resources
- Code Institutes Full Stack Framework Module.
- Youtube videos by [food delivery](https://www.youtube.com/playlist?list=PLPSM8rIid1a0qiCpbfujex5lZoXr2SRFC)
- [W3CSchool](https://www.w3schools.com/django/)
- [Django Documentation](https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types)(For different quaries while doing project. For example query about models, fields, form widgets, auth and many more)
- Other open source to understand and solve following types of error : UnboundedLocalError, MultivalueDictKeyError,  ProgrammingError, InvalidCursorName etc.


## Content and Media

Mostly images are taken from [canva](https://www.canva.com/).

----

## Acknowledgement

I would like to acknowledge my Code Institute mentor, Richey Malhotra, for his guidance and encouragement on this project.
My family for testing my work and offering positive thoughts and hot cups of tea throughout the project.

[Back to top](<#content>)
   