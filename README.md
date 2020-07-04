
# Ado Boutique Project



## Developer Aims
1. Develop a fully functioning django ecommerce store
2. Provide sufficient documentation through readme.md and comments in code to act as a base for future projects.


## Setup

Go to https://github.com/code-institute-org/gitpod-full-template and click Use This Template, then open in Gitpod.

* pip3 install django
* django-admin startproject boutique_ado .
* touch .gitignore

In .gitignore:
```
*.sqlite3
*.pyc
__pycache__
```

`python3 manage.py runserver`

Check it runs. Thens stop.

`python3 manage.py migrate`

`python3 manage.py createsuperuser`

## Use Allauth to set up user account creation and authentication

`pip3 install django-allauth`

Documentation is here:
https://django-allauth.readthedocs.io/en/latest/installation.html


Add the following to settings.py:

Check request context_processors exists in settings.py

This allows allauth to access the http request object in our templates.

```
AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]
```
Allow users to log in with their email address.


Add these to installed apps:

```
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
```
All user account registration etc. Allow logging in via facebook and google etc.

Under authentication backends add:

`SITE_ID = 1`

In urls.py:

add to urls list:
`    path('accounts', include('allauth.urls')),`

Add include here:
`from django.urls import path, include`


In terminal:
`python3 manage.py migrate` as new apps have been added.

`python3 manage.py runserver` 

Go to project url/admin:

Log in.

In sites, change domain name to eg. boutiqueado.example.com and Display Name.
NB:
This would be critical for social media authentication.

Log out of admin at stop dev server.

In urls.py

Add a / after accounts to ensure in the allauth urls are generated properly.

In settings.py we need to be able to access the email addresses as they are logged.

`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

Add to settings.py:

```
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_VERIFICATION_REQUIRED = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/success'
```

`python3 manage.py runserver`

Check that /accounts/login url is working.



in /admin/ May need to log in and add email address, and make verified and primary to convince allauth this is verified and primary.


At this point as long as the /success url is seen when logging in, we know allauth is working and can remove 'success' from the end of the url in settings.py `LOGIN_REDIRECT_URL = '/'`


In terminal:
`pip3 freeze > requirements.txt`


`mkdir templates`
`mkdir templates/allauth`






## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`



A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!
