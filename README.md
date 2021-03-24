# industrielldesign.no
Webpage for the designstudents at Industrial Design, NTNU Trondheim.

## Project structure
* `Assets` – All the staticfiles in the project are located here. Static files are files not generated by the users. Can be linked to in html-files with `{% static 'path' %} (remember to add {% load static %} to the top of the file).
  * `css` – All css lies in here. It's written in Sass (.scss), which is a css preprocessor which compiles .scss files to one .css-file. A master file `stylesheet.scss` imports all the other .scss-files in the project and compiles it to one file named `stylesheet.css`.
    * `base` – Global css for all pages.
    * `components` – Css for a globally used component i.e. a button or input fields are placed in this folder.
    * `grid` – A grid system that could be used. If you're interested look into the css, it's not complicated.
    * `pages` – Page specific css. These files should be wrapped in one id to avoid unwanted changes in other pages.
  * `img` – Images not uploaded by users
    * `icons` – Icons in the project
    * `illustrations` – Illustrations in the project.
    * `Logo` – Both an inverse and normal logo in svg.
  * `js` – Javascript files for the project. 
    * `404/snake.js` – A snake game made with canvas that's used on the 404-page.
    * `ajaxSetup.js` – Add this script if you're going to use ajax somewhere. It deals with csrf-tokens.
    * `dynamicShadow.js` – A script that creates a moving shadow around an element based on the cursor position.
* `authentication` – Logic for user handling. Authentication and database.
* `books` – Logic to handle book sales
* `courses` – Logic to handle courses. Includes code that populates the database with all NTNU courses (updated spring 2019).
* `dashboard` – Future app. Create an admin dashboard to administrate the page.
* ``

## Installation

1. Install python 3 >= 3.6
2. Install pip3
3. Install Git
4. Install PostGRES, guide [here](shttps://devcenter.heroku.com/articles/heroku-postgresql#local-setup)
5. Clone the git-repository somewhere on your computer `git clone url`

#### Virtual environment
Alt 1, Manual setup:
1. Install virtualenv
2. Create a new virtualenv somewhere on your computer with the command `virtualenv webbaENV` in terminal.
3. Navigate to the folder you created the environment in with `cd`
4. Activate the virtualenv with `source webbaENV/bin/activate`

Alt 2 Virtualenv through PyCharm:
1. Open the project in PyCharm
2. Open settings and navigate to Project interpreter
3. Press the cogwheel and then Add...
4. Select a location, has to end with the name of your interpreter. I.e `/Users/Tobias/Progging/environments/webbaENV`
5. Select Python 3.*.*
6. Press ok

#### Starting the server

7. Open the project folder in terminal and type `pip3 install -r requirements.txt`
8. Now run a couple of commands to set up the database:
  - `python3 manage.py makemigrations`
  - `python3 manage.py migrate`
9. Create a superuser with the command `python3 manage.py createsuperuser`.
9. Run the server with `python3 manage.py runserver`
10. Open your browser and type in `localhost:8000` in the address-bar.

## Making changes to scss

1. Install sass (how?)
2. If a new .scss file, add it to main.scss 
3. cd assets/css/ 
4. sass --watch main.scss:main.css
5. saved changes in scss files will automatically compile to the css-file.
