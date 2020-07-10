
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


## Customising allauth templates and installing a Bootstrap Template

TIP:
When typing python press tab and it will finish typing the currently used version.

Copy the allauth templates to our templates folder:

`cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth`

Openid and test folders will probably not be needed - so could be deleted.

In our main templates folder, create base.html


Boostrap starter template:
https://getbootstrap.com/docs/4.3/getting-started/introduction/


Paste into base.html

Add the following:

To avoid validation errors later:
`<meta http-equiv="X-UA-Compatible" content="ie=edge">`

Clean up comments, move scripts to head section.

At top of base.html:
`{% load static %}`


* Wrap meta, core css and corejs in {% block %} tags so it can be included or replaced later if necessary.
* Add `{% block extra_meta %}` extra css and extra js blocks so they can also be included or replaced later.
* Add `{% block extra_title %}{% endblock %}` within title tags so this can be added per page later.


Add some useful body content, to be finished later:
```
    <header class="container-fluid fixed-top"></header>
    {% if messages %}
    <div class="message-container"></div>
    {% endif %}

```

The following will also be needed:

```
{% block pageheader %}
    {% endblock %}

    {% block content %}
    {% endblock %}

    {% block postloadjs %}
    {% endblock %}

```
In terminal:
`python3 manage.py startapp home`
`mkdir -p home/templates/home`

Create index.html within this new directory


```
{% extends "base.html" %}
{% load static %}

{% block content %}
<h1 class="display-4 text-success">Check Bootstrap is working.</h1>
{% endblock%}
```

To render the template go to views.py:

```
def index(request):
    """  A view to return the index page. """
    return render(request, 'home/index.html')

```

Copy the contents of project level urls.py to a new urls.py file in home folder.

Remove docstring from top.
Remove include as this is not needed.
Add one empty path to indicate this it teh route url and render views.index with url home.
Import views from current directory.

It might look like this:

```

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
]


```

PROJECT LEVEL urls.py file will need:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
]


```



Add home to installed apps in settings.py

Add template directories in settings.py eg:

```
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'templates', 'allauth'),

        ],

```


Now `python3 manage.py runserver`



## Build Homepage

Build basic Bootstrap grid inside home/index.html. Container, Row, Column.
Use h-100 on container and row then my-auto to create vertical centring.

Use Bootstrap helper classes to create content:

```
    <div class="container h-100">
        <div class="row h-100" >
            <div class="col-7 col-md-6 my-auto">
                <h1 class="display-4 logo-font text-black">
                    The new collections are here.
                </h1>
                <div>
                    <h4>
                       <a href="" class="shop-now button btn btn-lg rounded-0 text-uppercase py-3">
                       Shop Now
                       </a>
                    </h4>
                </div>
            </div>
        </div>
    </div>
```

Add page header block.

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
