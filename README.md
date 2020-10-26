# Django diary
Web diary on the django framework.

## About
...

## Install
### Windows

Download and unzip the project source archive. Or do it with git:

```
> git clone https://github.com/light-hat/django-diary.git
```

First you have to install Python 3 on your computer. You can download python3 from [this link](https://www.python.org/downloads/).

Then you need to install virtualenv. You can do this with the following command:

```
> pip3 install virtualenv
```

Once virtualenv is installed, go to the project folder and create a virtual environment using this command:

```
> virtualenv -p python3.8 venv
```

Start the virtual environment with the command:

```
> venv\Scripts\activate
```

If you did everything correctly, (venv) will appear in front of the current folder. Like this:

```
(venv) C:\Users\th3g3ntl3man\source\repos\newenv\django-diary-master>
```

Next, you need to install the dependencies with the following command:

```
> pip3 install django Pillow
```

After that, enter this command:
```
> python manage.py migrate
```

or

```
> python3 manage.py migrate
```

The first case may not work if you have python 2 installed on your computer in parallel. 
Run the project with the command:

```
> python manage.py runserver
```

If after that you see something like this:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 20 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, days, sessions.
Run 'python manage.py migrate' to apply them.
October 26, 2020 - 07:32:58
Django version 3.1.2, using settings 'diary.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

You can safely open your browser and go to ```127.0.0.1:8000```. The site should open. If you have reached this step, I can congratulate you, you did everything right. However, this is not all. Next, you need to create a superuser to add entries. Enter the following command:

```
> python manage.py createsuperuser
```

Then enter your username, e-mail, password twice and press y at the end. It looks like this:

```
(venv) C:\Users\th3g3ntl3man\source\repos\newenv\django-diary-master>python manage.py createsuperuser
Username (leave blank to use 'th3g3ntl3man'): yourusername
Email address: youremail@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

After that, start the server and go to ```127.0.0.1:8000/admin``` and log in to the admin panel.

### Linux

...

## Usage
...

## Examples
Below are screenshots of the running diary. Main page:

![screenshot1](.github/screenshot1.jpg)

![screenshot2](.github/screenshot2.jpg)

One of the diary entries looks like this:

![screenshot3](.github/screenshot3.jpg)

![screenshot4](.github/screenshot4.jpg)

![screenshot5](.github/screenshot5.jpg)

