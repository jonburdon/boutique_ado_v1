
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

Add page header block in home index.html.

Add content to base.html header:

```
   <header class="container-fluid fixed-top">
        <div class="row">
            <div class="col-12 col-lg-4 my-auto py-1 py-lg-0 text-center text-lg-left"></div>
            <div class="col-12 col-lg-4 my-auto py-1 py-lg-0"></div>
           <div class="col-12 col-lg-4 my-auto py-1 py-lg-0"></div>
        </div>
    </header>
```

Use bootstrap helper classes to add further content (including search form) to header content:

```
    <header class="container-fluid fixed-top">
        <div class="row">
            <div class="col-12 col-lg-4 my-auto py-1 py-lg-0 text-center text-lg-left">
                <a href="{% url 'home' %}" class="nav-link main-logo-link">
                    <h2 class="logofont text-black my-0"><strong>Boutique</strong>Ado</h2>
                </a>
            </div>
            <div class="col-12 col-lg-4 my-auto py-1 py-lg-0">
            
                <form method="GET" action="">
                    <div class="input-group w-100">
                        <input type="text" class="form-control border border-black rounded-0" type="text" name="q" placeholder="Search our site">
                        <div class="input-group-append">
                            <button class="form-control btn btn-black border border-black rounded-0" type="submit">
                                <span class="icon">
                                    <i class="fas fa-search"></i>
                                </span>
                            </button>
                        </div>

                    </div>
                </form>
            
            </div>
            
            <div class="col-12 col-lg-4 my-auto py-1 py-lg-0">
                <ul class="list-inline list-unstyled text-center text-lg-right my-0">
                    <li class="list-inline-item dropdown">
                        <a class="text-black nav-link" href="#" id="user-options" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            <div class="text-center">
                                <div><i class="fas fa-user fa-lg"></i></div>
                                <p class="my-0">My Account</p>
                            </div>
                        </a>
                        <div class="dropdown-menu border-0" aria-labelledby="user-options">
                            {% if request.user.is_authenticated %}
                                {% if request.user.is_superuser %}
                                    <a href="" class="dropdown-item">Product Management</a>
                                {% endif %}
                                <a href="" class="dropdown-item">My Profile</a>
                                <a href="{% url 'account_logout' %}" class="dropdown-item">Logout</a>
                            {% else %}
                                <a href="{% url 'account_signup' %}" class="dropdown-item">Register</a>
                                <a href="{% url 'account_login' %}" class="dropdown-item">Login</a>
                            {% endif %}
                        </div>
                    </li>
                    <li class="list-inline-item">
                        <a class="{% if grand_total %}text-info font-weight-bold{% else %}text-black{% endif %} nav-link" href="">
                            <div class="text-center">
                                <div><i class="fas fa-shopping-bag fa-lg"></i></div>
                                <p class="my-0">
                                    {% if grand_total %}
                                        ${{ grand_total|floatformat:2 }}
                                    {% else %}
                                        $0.00
                                    {% endif %}
                                </p>
                            </div>
                        </a>
                    </li>
                </ul>
            </div>

        </div>
    </header>
```


Update css including css from Bulma framework to style font awesome icons and centre them every time they are used:

```
html {
    height: 100%;
}

body {
    background: url('/media/homepage_background_cropped.jpg') no-repeat center center fixed;
    background-size: cover;
    height: calc(100vh - 164px);
    color: #555;
    font-family: 'Lato';
}

/* from Bulma */
.icon {
    align-items: center;
    display: inline-flex;
    justify-content: center;
    height: 1.5rem;
    width: 1.5rem;
}

.logo-font {
    text-transform: uppercase;
}

.main-logo-link {
    width: fit-content;
}

.shop-now-button {
    background: black;
    color: white;
    min-width: 260px;
}

.btn-black {
    background: black;
    color: white;
}

.shop-now-button:hover,
.shop-now-button:active,
.shop-now-button:focus,
.btn-black:hover,
.btn-black:active,
.btn-black:focus {
    background: #222;
    color: white;
}

.text-black {
    color: #000 !important;
}

.border-black {
    border: 1px solid black !important;
}

/* -------------------------------- Media Queries */

/* Slightly larger container on xl screens */
@media (min-width: 1200px) {
  .container {
    max-width: 80%;
  }
}

/* fixed top navbar only on medium and up */
@media (min-width: 992px) {
    .fixed-top-desktop-only {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        z-index: 1030;
    }

    .header-container {
        padding-top: 164px;
    }
}

```

Add link for Lato to base.html core css section.

Add link to base.css to the same section: `<link rel="stylesheet" href="{% static 'css/base.css' %}">   `

Log in to Fontawesome. In Profile -> Kits. Get kit code `<script>` code and paste in core js.

### Ensure django can locate static files:

Add paths for static files to settings.py:

```
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


```

In urls.py:

```
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```



## Further Improvements to Navigation

`mkdir templates/includes`

Create two includes:
main-nav.html
mobile-header.html

Pasted in from:
https://github.com/ckz8780/boutique_ado_v1/tree/e77fa8e928e3901d3502b18e912e90d2204b8ec3/templates/includes

Update base.html to include row for Free Shipping notice.
Add bg-black class to base.css


```
<div id="delivery-banner" class="row text-center">
            <div class="col bg-black text-white">
                <h4 class="logo-font my-1">Free Delivery on orders over ${{ free_shipping_threshold }}!</h4>
            </div>
 </div>
```

## Products append

Uploaded product images to media folder.

To initiate:
`python3 manage.py startapp products`

Add in settings.py

Uploaded json fixture files to products/fixtures.

In products -> models.py:

```
class Category(models.model):
    name = models.Charfield(max_length=254)
    friendly_name = models.Charfield(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name
```

Note: null=true and blank=true make friendlyname optional.

Note: field types can be looked up here: https://docs.djangoproject.com/en/3.0/ref/models/fields/


Products model:

```
class Product(models.model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

```

Note: In the foreign key field, on_delete is set to SET_NULL so that the product will not be deleted if the category is deleted.
Note: Name, Description, Price are required, everything else is optional.
Note: field names such as CharField are case sensitive.

`python3 manage.py makemigrations --dry-run`

`pip3 install pillow`

Look good now.

`python3 manage.py makemigrations`

`python3 manage.py migrate --plan` to check there are no issues with the new models.

`python3 manage.py migrate`

Note: If not using the plan flag, specify which model you are migrating to avoid making unintentional changes to other models.

In products -> admin.py:

```
from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)

```

`python3 manage.py loaddata categories` Will load data from fixtures to the database. Start with categories as products have a foreign key dependent on this.

`python3 manage.py loaddata products`

## Changes to Admin panel

Change plural of Category from Categorys to Categories
In models.py:
```
    class Meta:
        verbose_name_plural='Categories'
```

In admin.py, add columns in the admin panel:

```
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
# Display order in admin panel
# These could be in any order and the display order would change
# Make sure new classes are registered below.
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
#sort by sku. This is a tuple because multiple sorts could be added eg 'category', 'name'. To reverse it, put a minus in front of sku.
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

```

## View Set Up for products:

Copy basic view from Home View and alter:

```
from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """  A view to show, sort and search products. """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
```

Copy home urls file and use as basis for products urls.py (need to create this)

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
]

```

Include this in global file:
`    path('products/', include('products.urls')),`

`mkdir -p products/templates/products`

Create products.html in this directory. Copy home template in as a shell.

Note: Product variable from product view is used in this template: {{ products }}

```
{% extends "base.html" %}
{% load static %}


{% block page_header %}
    <div class="container header-container">
        <div class="row">
            <div class="col">
            
            </div>
        </div>
    </div>
{% endblock %}


{% block content %}

    <div class="container">
        <div class="row" >
            <div class="col">
                {{ products }}
            </div>
        </div>
    </div>

{% endblock %}
```


Paste in code from here if needed:
https://github.com/ckz8780/boutique_ado_v1/tree/e3c29afef63a8e5a8dae3fdc6b1277eb32206dbc

Note: if statements are used: if forloop.container|divisibleby:2 to only display hr if the column display is 12,6,3,4 etc.

```
<!-- Add an hr after every row (depending on screen size) -->

                        <div class="col-12 d-sm-none mb-5">
                        <hr>
                        </div>
                        <!-- Only show this if the loop counter is divisible by 2 ie this would be a col-6 -->
                        {% if forloop.counter|divisibleby:2 %}
                        <div class="col-12 d-none d-sm-block d-md-block d-lg-none mb-5">
                        <hr>
                        </div>
                        {% endif %}

                        <!-- Only show this if the loop counter is divisible by 3 ie this would be a col-4 -->
                        {% if forloop.counter|divisibleby:3 %}
                        <div class="col-12 d-none d-lg-block d-xl-none mb-5">
                        <hr>
                        </div>
                        {% endif %}

                        <!-- Only show this if the loop counter is divisible by 4 ie this would be a col-4 -->
                        {% if forloop.counter|divisibleby:4 %}
                        <div class="col-12 d-none d-xl-block mb-5">
                        <hr>
                        </div>
                        {% endif %}
```

Add products url to main nav:
`<a href="{% url 'products' %}" class="dropdown-item">All Products</a>`

and in index.html Shop Now button:

`<a href="{% url 'products' %}" class="shop-now button btn btn-lg rounded-0 text-uppercase py-3">
                       Shop Now
                       </a>`

## Single Product View

This needs to take the product id as a parameter and then display the product.

Update views in products app:

```
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def all_products(request):
    """  A view to show, sort and search queries. """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """  A view to show single product view. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
```

Update urls.py in products.
`path('<product_id>', views.product_detail, name="product_detail"),`

Duplicate and rename products.html as product_detail.html

Add layout for product detail.

Add links to product detail page in products.html: `<a href="{% url 'product_detail' product.id %}">`
Note: In the product page we are working with a django object so djando.id is needed.


Bugfix: Pad the top on mobile view when navbar is collapsed. This displays body at 100% of the viewport but minus the height of the header.

```
@media (max-width: 991px) {
    .header-container {
        padding-top: 116px;
    }

    body {
        height: calc(100vh - 116px);
    }

}
```


## Queries and Categories

Search function:

Change Action in search form on base.html: `<form method="GET" action="{% url 'products' %}">`

And in mobile version of the header: `<form class="form" method="GET" action="{% url 'products' %}">`


In  products -> Views.py:

This checks if get is in the url and then creates the query variable if present.

```
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # Search query will check product name AND product description. The Pipe | is the OR statement and the i makes this insensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # pass this query to the filter method to filter products
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }


```

The following will be needed for this to work:
```
from django.contrib import messages
from django.db.models import Q
```

`from django.shortcuts import render, redirect, reverse, get_object_or_404`

NOTE:
Q handles the search request so that the search request could be in the product name OR in the description etc.
See django documentation: https://docs.djangoproject.com/en/3.0/topics/db/queries/

## Add Category Filter:

Add category parameter to url links in main_nav.html:
```
<a href="{% url 'products' %}?category=activewear,essentials" class="dropdown-item">Activewear &amp; Essentials</a>
                <a href="{% url 'products' %}?category=jeans" class="dropdown-item">Jeans</a>
                <a href="{% url 'products' %}?category=shirts" class="dropdown-item">Shirts</a>
                <a href="{% url 'products' %}?category=activewear,essentials,jeans,shirts" class="dropdown-item">All Clothing</a>
 
```

In products -> views.py

`from .models import Product, Category`

```
    products = Product.objects.all()
    query = None
    categories = None
```

```
    if request.GET:

        if 'category' in request.GET:
            categories = request.GET[]'category'].split(',')
            # We can look for the name field in the category model using __ because they are related with a foreign key
            products = products.filter(category__name__in=categories)
            # Capture categories so the currently selected categories can be displayed
            categories = Category.objects.filter(name__in=categories)
```

Use idencial syntax for Homewear and Special Offers nav.


## Sorting Products

Add url links get parameters to main-nav.html with sort and direction:

```
            <div class="dropdown-menu border-0" aria-labelledby="all-products-link">
                <a href="{% url 'products' %}?sort=price&direction=asc" class="dropdown-item">By Price</a>
                <a href="{% url 'products' %}?sort=rating&direction=desc" class="dropdown-item ">By Rating</a>
                <a href="{% url 'products' %}?sort=category&direction=asc" class="dropdown-item ">By Category</a>
                <a href="{% url 'products' %}" class="dropdown-item">All Products</a>
            </div>
```

Add code to handle get parameters in products/views.py. See comments in the code for explanation.

```
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # set up variables for case insentive searching
            if sortkey == 'name'
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                # Now we have lower name in the sortkey variable, but we have preserved the sort term in the variable 'sort'

            if 'direction' in request.GET:
                # if direction is descending, add a - in from of the sortkey using string formatting which will reverse the order
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            order the products using the sortkey
            # implement the search using the oderby model method
            products = products.order_by(sortkey)

# Current sorting will be None_None if no sorting has happened.
current_sorting = f'{sort}_{direction}'


 context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
```


## Further Sorting 

Display category, with link, in the product page:

In products.html AND product_detail.html:

```
{% if product.category %}
                                            <p class="small mt-1 mb-0">
                                                <a class="text-muted" href="{% url 'products' %}?category={{ product.category.name }}">
                                                    <i class="fas fa-tag mr-1"></i>{{product.category.friendly_name}}
                                                </a>
                                            </p>
                                            {% endif %}
```

Add in products.html:
```
                {% for c in current_categories %}
                    <a class="category-badge text-decoration-none" href="{% url 'products' %}?category={{ c.name }}">
                        <span class="p-2 mt-2 badge badge-white text-black rounded-0 border border-dark">{{ c.friendly_name }}</span>
                    </a>
                {% endfor %}
```

Add to products html. This will put a sort select box first on mobile using order-first by order-last on larger screens. 

Create a select field using the value from the current sorting template variable and select this by default. This will not work for sorting (YET) but it will update according the the current sorting selected.


```

<div class="col-12 col-md-6 my-auto order-md-last d-flex justify-content-center justify-content-md-end">
                        <div class="sort-select-wrapper w-50">
                            <select id="sort-selector" class="custom-select custom-select-sm rounded-0 border border-{% if current_sorting != 'None_None' %}info{% else %}black{% endif %}">
                                <option value="reset" {% if current_sorting == 'None_None' %}selected{% endif %}>Sort by...</option>
                                <option value="price_asc" {% if current_sorting == 'price_asc' %}selected{% endif %}>Price (low to high)</option>
                                <option value="price_desc" {% if current_sorting == 'price_desc' %}selected{% endif %}>Price (high to low)</option>
                                <option value="rating_asc" {% if current_sorting == 'rating_asc' %}selected{% endif %}>Rating (low to high)</option>
                                <option value="rating_desc" {% if current_sorting == 'rating_desc' %}selected{% endif %}>Rating (high to low)</option>
                                <option value="name_asc" {% if current_sorting == 'name_asc' %}selected{% endif %}>Name (A-Z)</option>
                                <option value="name_desc" {% if current_sorting == 'name_desc' %}selected{% endif %}>Name (Z-A)</option>
                                <option value="category_asc" {% if current_sorting == 'category_asc' %}selected{% endif %}>Category (A-Z)</option>
                                <option value="category_desc" {% if current_sorting == 'category_desc' %}selected{% endif %}>Category (Z-A)</option>
                            </select>
                        </div>
                    </div>
                    <div class="col-12 col-md-6 order-md-first">
                        <p class="text-muted mt-3 text-center text-md-left">
                            {% if search_term or current_categories or current_sorting != 'None_None' %}
                                <span class="small"><a href="{% url 'products' %}">Products Home</a> | </span>
                            {% endif %}
                            {{ products|length }} Products{% if search_term %} found for <strong>"{{ search_term }}"</strong>{% endif %}
                        </p>
                    </div>
```

Note: USING RELATIONS IN ANOTHER MODEL. In this case, related category:
Add to views.py:

```
            # Use RELATIONS. Use double underscore syntax to allow connection to RELATED category
            if sortkey == 'category'
                sorkey = 'category__name'
```

Add js to bottom of products.html to operate the select field. Do this by splitting the current search term in to sort and direction and then replacing the url in the window.

Import Lower in views.py

Add back to top button to bottom of products.html and add js and css for this.


## Shopping Basket Setup

Create a new app called bag:

`python3 manage.py startapp bag`

Add this to list of installed apps in settings.py

Set up the view to render the template in bag -> views.py

```
def view_bag(request):
    """  A view to display shopping bag. """
    return render(request, 'bag/bag.html')from django.shortcuts import render

```

Create templates folder and bag.html

Copy in index.html from the home app.

Copy home urls file and paste into a new urls.py file in the new app.

```

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name="view_bag"),
]

```

Add reference the new url file in the project level urls file.

Add link to view bag in base.html `<a class="{% if grand_total %}text-info font-weight-bold{% else %}text-black{% endif %} nav-link" href="{% url 'view_bag' %}">` and also in mobile-top-header.html

Add layout grid to bag.html with if bag_items conditional to display message if bag is empty.

Create `contexts.py` in the bag app.


Define contexts processor to make a dictionary of bag items available to all templates in the application.

```
def bag_contents(request)
""" Return a dictionary called contexts which we are about to create """
""" This is a contexts processor - makes this dictionary available to all templates in the application"""
    context= {}

    return context
```

Add this to settings.py:
Templates -> Options -> context processors:
` 'bag.contents.bag_contents', `
Bag contents can now be accessed from any template in the app.

Also add the following variables in settings.py:

```
FREE_DELIVERY_THRESHOLD = 50
STANDARD_DELIVERY_PERCENTAGE = 10
```

Set up basic calculations for shopping cart and make these variables available to all apps using Context:

```
from decimal import Decimal
from django.conf import settings

def bag_contents(request):
# Return a dictionary called contexts which we are about to create 
# This is a contexts processor - makes this dictionary available to all templates in the application
    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
```

## Adding and Handling Products

* In product_detail.html write a form to submit the product to the shopping cart:


```
<form class="form" action="{% url 'add_to_bag' product.id %}" method="POST">
                        {% csrf_token %} <!-- Use django Cross Site Protect Forgery Protection because we are using post -->
                        <div class="form-row">
                            <div class="col-12">
                                <p class="mt-3"><strong>Quantity:</strong></p>
                                <div class="form-group w-50">
                                    <div class="input-group"> <!-- Select how many of this item to purchase -->
                                        <input class="form-control qty_input" type="number" name="quantity" value="1" min="1" max="99" data-item_id="{{ product.id }}" id="id_qty_{{ product.id }}">
                                    </div>
                                </div>
                            </div>

                            <div class="col-12">
                                <a href="{% url 'products' %}" class="btn btn-outline-black rounded-0 mt-5">
                                    <span class="icon">
                                        <i class="fas fa-chevron-left"></i>
                                    </span>
                                    <span class="text-uppercase">Keep Shopping</span>
                                </a>
                                <input type="submit" class="btn btn-black rounded-0 text-uppercase mt-5" value="Add to Bag">
                            </div>
                            <input type="hidden" name="redirect_url" value="{{ request.path }}"> <!-- Submit current url as a hidden field so we can be directed accordingly -->
                        </div>
                    </form>

```

* Update base.css with btn-outline-black class

* Define add_to_bag in views.py

```
from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity')) #convert to integer as the template will send this as a string
    redirect_url = request.POST.get('redirect_url') # Use the redirect variable given in the post data
    # Store the shopping bag data in the http request session. This will persist until user closes their browser
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity #increment quantity if this item is already in the bag
    else:
        bag[item_id] = quantity # add or update

    request.session['bag'] = bag # override the variable in the session with the updated version
    print(request.session['bag'])
    return redirect(redirect_url)
    
```

* Update url

* Add action to the form to include product id user is adding `<form class="form" action="{% url 'add_to_bag' product.id %}" method="POST">`

* This can now be tested - Click add to bag and the quantity added and product id will be visible in console.

## Update context processor to make bag data available across entire application

Access the bag variable stored in the browser session from the Context Processor in bag -> contexts.py

```

    # Using the bag from the session data... update total, product count
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
```
* import the model and get_object_or_404

* Add `{{ bag_items}}` to bag.html just to check this data is displaying.

* Update bag.html with table to display shopping bag data.
* Use bootstrap scope=col in th elements.
* Use bootstrap classes such as p-3 w-25 my-0 text-muted to format td elements

## Adding functionality for product variations

* In products -> models.py
`has_sizes = models.BooleanField(default=False, null=True, blank=True)`

* Note this would not allow for full functionality in a production site eg stock management for each size of each product

* REMEMBER! This is a change to the models, so...

* Dry run the make migrations... `python3 manage.py makemigrations --dry-run`

* Looks ok so `python3 manage.py makemigrations`

* `python3 manage.py migrate --plan`

* `python3 manage.py migrate`

* `python3 manage.py shell`

In shell:
- from products.models import Product
- kdbb = ['kitchen_dining', 'bed_bath']   
- clothes = Product.objects.exclude(category__name__in=kdbb)  
- clothes.count()

```
for item in clothes: 
    item.has_sizes = True 
   item.save() 
```
- Press enter to execute
- Product.objects.filter(has_sizes=True)  

- exit()

* This shows how shell can be used to manipulate the database programatically from the back end.

* Add size selector to the product_detail.html template

```
{% with product.has_sizes as s %}
                            {% if s %}
                                <div class="col-12">
                                    <p><strong>Size:</strong></p>
                                    <select class="form-control rounded-0 w-50" name="product_size" id='id_product_size'>
                                        <option value="xs">XS</option>
                                        <option value="s">S</option>
                                        <option value="m" selected>M</option>
                                        <option value="l">L</option>
                                        <option value="xl">XL</option>
                                    </select>
                                </div>
                            {% endif %}
```


* Adjust grid conditionally for the next row `<div class="col{% if s %}-12 mt-2{% endif %}">`

* Add `{% endwith %}` after appropriate point in grid - line 91 in this case.

* Add size to product detail on shopping bag page bag -> bag.html:

`<p class="my-0"><strong>Size: </strong>{% if item.product.has_sizes %}{{ item.size|upper }}{% else %}N/A{% endif %}</p>`


In django admin panel, update the few products in clothing that don't have sizes.


In bag app, views.py set the product size variable to that posted:

```
# If product size is in the product url, set the variable 'size' to this value
    size = None
    if 'product_size' in request.POST:
        size = request.POST['size']
```

Update to store this in a dictionary:

```
if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else: # Use a dictionary so that different item ids can be posted, and multiple sizes posted can be tracked.
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity #increment quantity if this item is already in the bag
        else:
            bag[item_id] = quantity # add or update

```

* In bag -> Contexts.py

- Change 'quantity' to 'item_data' because this variable is now a dictionary with quantity and size for each time this item is purchased
- Add logic to handle this differently if it is a dictionary with the new data

```
 # Using the bag from the session data... update total, product count
    for item_id, item_data in bag.items():
        if isinstance(item_data, int): #implement this if iteme data exists as an integer
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else: # this must be a dictionary so it must be handled differently.
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': size,
                })


```

* USEFUL! In bag.html render the variables we need to view and format just to see what need to be accessed and how:

```
{{ bag_items }}<br><br>

                    {{ request.session.bag }}
```

Tip: In Chrome -> Dev Tools -> Applications -> Storage -> Cookies -> Right click and clear the cookie for this session to clear the bag.

Currently there is a KEY ERROR:

Fix: `     size = request.POST['product_size']`

## Updates to Product Detail page to allow for product quantity updating

* update input group to include bootstrap buttons 

* Add js to handle this updating quantities to an include as this will be used elsewhere (create includes directory in the templates/ products folder)

* Create quantity_input_script.html (See comments in the code for functionality)

* include this in the postloadjs block at the bottom of product_detail.html

```
{% block postloadjs %}
{{ block.super }}
{% include 'products/includes/quantity_input_script.html' %}
{% endblock %}

```

## Update product quantity from the shopping bag

* Add form with method of post and class of update-form
* use csrf_token
* paste from product detail and reformat css
* update product template variables to item.item_id
* submit this in a hidden input field if the product does have sizes:

```
{% if item.product.has_sizes %}
<input type="hidden" name="product_size" value="{{ item.size }}">
{% endif %}
```

* Update contexts.py to display quantity for products with sizes: `'quantity': quantity,`

* To submit this, use js ( bottom of bag.html):

```
<script type="text/javascript">
    // Update quantity on click
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    })

    // Remove item and reload on click
    $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var size = $(this).data('size');
        var url = `/bag/remove/${itemId}`;
        var data = {'csrfmiddlewaretoken': csrfToken, 'size': size};

        $.post(url, data)
         .done(function() {
             location.reload();
         });
    })
</script>
```

* Update base.css to style cursor pointer over Update and Remove links.


## Adjust Quantity

Copy and paste add_to_bag in bad views.py, rename to adjust_bag

Remove the redirect (we always want to stay on the bag page)

Change logic to update quantity or remove it:

```
   if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]    
             
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
           bag.pop[item_id]

    request.session['bag'] = bag # override the variable in the session with the updated version
    return redirect(reverse('view_bag'))

```

* update url

* in bag.html update the form `<form class="form update-form" method="POST" action="{% url 'adjust_bag' item.item_id %}">`

## Remove directly without setting quantity to zero via adjust_bag

* copy adjust_bag

* update logic to remove  item via the remove_from_bag function

* NOTE: try block was added using http response

* update urls

* update js in bag.html to use consistent variables (change size to product_size)

* change slim version of jquery that loads with bootstrap to the full version from : https://code.jquery.com/ and load in base.html


## Using a template filter to change the subtotal to quantity x product price

* in bag folder create new folder called templatetags

* create bag_tools.py
* create __init__.py to make this module available in templates

* To use this filter create register which is an instance of template.Library. Use this to register this function as a template filter

```
from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
```

* load in bag.html with `{% load bag_tools %}`

* Pass it the price `<p class="my-0">${{ item.product.price | calc_subtotal:item.quantity }}</p>`

* Subtotal now updates in bag.html

## Adding Toasts

* in main folder -> templates -> includes create folder called toasts then 4 files for error, info, success and warning .html

* use data-autohide="false" to allow the user to dismiss this when they have read the message.

* Paste in bootstrap toast code and customise.

* in base.html:

```
    {% if messages %}
        <div class="message-container">
            {% for message in messages %}
                {% include 'includes/toasts/toast_success.html' %}
            {% endfor %}
        </div>
    {% endif %}

```
* in bag views.py

```
from django.contrib import messages
from products.models import Product
```
* in add_to_bag `product = Product.objects.get(pk=item_id)` and `messages.success(request, f'Added {product.name} to your bag')`

* In base.html call the toast method from Bootstrap with an option of 'show' on any elements with the toast class:

```
    <script type="text/javascript">
    $('.toast').toast('show');
    </script>
```

* In Settings.py - store messages in the browser session: `MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'`

* Add if statements for different message types. These are message levels in django: 40 is an error, 30 is a warning, 20 is success, info toast will be used as default

* Add css to position toasts in top right of screen and use z-index to position on top

* Add further messages:
- Add to bag:
- `messages.success(request, f'Updated {product.name} quanity to {bag[item_id]}')`
- `messages.success(request, f'Added size {size.upper()} {product.name} to your bag')` (two locations)
- `messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')`
- Adjust bag:
- `messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')`
- `messages.success(request, f'Removed {product.name} from your bag')`
- etc

* Add `product = Product.objects.get(pk=item_id)` to adjust_bag so the strings will work
* update to `product = get_object_or_404(Product, pk=item_id)` in case product isn't found

* Add messages to remove_from_bag
including `messages.error(request, f'Error removing item {e}')`

* Add css to style arrows etc - copied from Bootstrap

* Update success toast:
- Add a preview of the bag in the notifcation if there is a grand total
- Add bag notification wrapper to base.css to restrict size of the success toast

## Checkout App (Anonymous Checkout)

* python3 manage.py startapp checkout

* Add this to list of installed apps in settings.py

* Create data structure in -> Models.py

* Create methods to handle the checkout process

* dryrun creating the models

* python3 manage.py makemigrations --dry-run

* python3 manage.py makemigrations

* Plan their execution

* python3 manage.py migrate --plan

* python3 manage.py migrate


## Adding Orders to Admin

* In checkout, admin.py:
- import order and order_line_item models
- create class order_admin
- read only fields for order number, date, del cost, order total and grand total
- use fields option so we can specify the order of these fields
- Use list display option to restrict which columns display in admin
- order by date in reverse chronological order
- Make orderlineitems editable in the order admin display using TabularInline class

* Need to update costs as users add line items to the order
- Need to call the method we already created each time a line item is created. Built in django feature signals can do this
- Create file signals.py
- import the signals Postsave and Postdelete
- These signals are sent to the entire app after a model is saved or deleted
- These use dispatch and reciever from django.dispatch
- define update_on_save with the parameters sender (sender of signals), instance (which models sent it) and created (is this new or not?) key word arguments - kwargs.
- Call the update total
- use the @receiver decorator to tell post save signals from the orderlineitem model is used
- update checkout -> apps.py to override ready method and import signals module.

## Checkout form

* create forms.py in checkout app
- import forms and order model
- create order form class with meta options for model and fields
- set up default form with a dictionary or placeholders
- insert placeholder data in to the form, remove the labels and add a css class for use later

## The checkout views and templates
- in views.py get bag from session, add an error message if there is nothing in bag, create instance of order form, create template and context, render it.
- create checkout -> urls.py
- update project level urls file
-  create checkout/templates/checkout/checkout.html
- Use shopping bag as a structure
- use separate extra css block static/checkout/css/checkout.css
- install crispyforms in terminal. This allows us to style forms with bootstrap automatically
- `pip3 install django-crispy-forms`
- Add `    'crispy_forms',` to installed apps in settings.py
- in settings.py `CRISPY_TEMPLATE_PACK = 'bootstrap4`
- Add list 'builtins' to settings.py - this installs Crispy-forms to all our templates by default:

```
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]

```

- `pip3 freeze > requirements.txt`
- Create checkout form in three fieldsets with different styling.
- use as_crispy-fields template tag to style
- include option to save this delivery into to my profile, sign up or login.
- include two empty divs for card-element and card-errors to be built by stripe
- MEDIA_URL template tag will not work without a processor for this.
- Add this to settings.py in templates - options: `'django.template.context_processors.media',`

- add checkout url to the checkout button in bag.html

## Stripe payments setup:

In checkout.css add styling to the bootstrap form to match site styles.

* Visit stripe.com and create an account or log in

* We need test API keys (later)

* Follow https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details
- Include Stripe js in base.html
- In postload.js block in checkout.html:
    - Use json_script template filter to access variables.
    - Use stripe_public_key and client_variables
- Add these to checkout app -> Views ... contexts"

```
    context = {
        'order_form': order_form,
        'stripe_public_key': 'the public key',
        'secret_key': 'test client secret',
    }
```
- Now if you check the rendered front end html you will see both values displayed for the world to see! They are matched to what we sent into the json_script built in template filter.
- Create stripe_elements.js inside checkout js folder within checkout / static
- In checkout.css add `stripe-style-input` class to ensure the styles from stripe apply to all form elements.
- Add the new stripe_elements.js to the checkout.html postload.js block
- Pass stripe error to messaging display in stripe_elements.js

* In checkout.views.py import bag contents function from bag.context to make it available for use. `from bag.contexts import bag_contents`

* in checkout method:
    - calculate checkout total round it to an integer for Stripe.
* `pip3 install stripe`
* import stripe in views.py

* In Settings.py:
- Add stripe currency
- Add stripe public key to get from environment
- Add stripe secret key to get from environment

To set these in gitpod, (also works on Mac but in windows use SET command) use the export command:
In Terminal:
`export STRIPE_PUBLIC_KEY=Paste-yours-here`
`export STRIPE_SECRET_KEY=Paste-yours-here`

Don't forget this is not permanent! They need to be added each time workspace is started.
To make these permanent in Gitpod: 
- Account icon (upper right)
- Settings
- Enter them in the environment variables section

* In views.py
- Add the public and secret key variables
- Set these on stripe.api_key
- pass stripe.paymentintent.create  amount and currency
- for now just print(intent) - refresh page, this intent variable will be seen in terminal
- update context to use the key from above and change client_secret to intent.client_secret
- Add alert message if public key not set

- Add listener to the payment forms submit event. Copy this from Stripe documentation and make a few changes. (https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details)
- Paste in to stripe_elements.js - see comments for changes
- Change variable names to Camel Case for best practise

* Test - use card number 4242 4242 4242 4242 any CVC, and date in the future and any 5 digit postal code

* In Stripe Dashboard - click Developers -> Events -> Check payment was successful. MAKE SURE you select 'Viewing test data.'

## Adding functionality to checkout flow

* Creating the order in the database
- In checkout views.py, add an if method == post.
- Wrap current code in an else block
- See comments in the code

- Create checkout success view.
- Create url for checkout success 
- Create checkout_success.html

- Get signals working. in Checkout init.py tell django the config class for the apps. Without this, django would not know custom ready methods therefore signals would not work
- restart signals.

- In models.py add `or 0` line to:
- `self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0`
- This will set the order total to zero instead of 'none' if the line items are manually removed, and avoids an error.

- restart server - check checkout success works in stripe and in database
- signals are not yet working (total is not updating in order model in admin)
- change second function name to update_on_delete in signals.py

# Creating an order summary and redundancy Handling
- In checkout success, add order summary. Note we are using one row for each form field in the order summary. Use a for loop to generate a new row for each line item and then insert product name, quantity and price etc.
- Use if statements to only show unrequired fields if they have been completed.

- Add loading overlay div to checkout.html (after main container div, last div in main block)
- in checkout.css add the css to cover whole page and display loading-spinner
- in stripe_elements.js, trigger the overlay when user clicks submit button and reverse this if there is an error:

```
$('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
```

* Use different test card number, this time with extra authentication from Stripe: 4000002500003155

- Now when the stripe popup asks for authentication if we cancel, the form data should be intact but if we authenticate, the process should work and remove the popup

## Adding Stripe webhooks

If the user accidentallt closes the window after communicating stripe this order would not be completed and all sorts of errors could occur. Therefore redundancy must be built in. Use Webhooks to listen for this data.

- Create webhook_handler.py
- Create class method called handle event. Accept this from stripe and send http response indicating it was received.
- By creating a class, they code is easily reuseable.
- Create an event map to handle different events.
- Get event type from Stripe eg succeeded failed
- Look up it's type in dictionary

Add wh secret in settings.py
In Stripe Developers -> Add endpoint, receive all. Copy signing secret

NB for webhooks to connect they must be exported to the environment using `export STRIPE_WH_SECRET=thesecretkeygoeshere` - best to also save in Github Settings

* In Stripe - Developers -> Webhooks -> check test and then test webhooks. The messaeges in Webhook handler should be displayed conditionally according to the webhook sent. Try testing by using a different message for failed.

Add to Checkout / Static / js / stripe_elements.js to include payment_method address and shipping_address data.

### Adding Meta data to pass through Stripe webhooks

Add logic to the webhook to determine whether the user checked the save data option in the form.
This is not supported in the card payment method, so it needs to be added server side:

Create cache_checkout_data view in views.py
import require_POST

```
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)
```
* Include a json dump of their shopping bag. VERY USEFUL for later!

* Create a url to access the new view.

### Summary of Stripe Elements.js functionality:

* If form is submitted, form submission is prevented (line 51). Card element is hidden and loading overlay is displayed.
* Form is captured in variables that aren't sent to stripe, post to cached_checkout_data view.
* If card payment success, form is submitted
* If fail - re-enable card element and display error for the user.

### Handling checkout data after this has passed through payment success webhook

* If everything was successful, the order should now exist in our database.
* Check if this is the case in webhook handler py and pass success or 500 back to Stripe.
* Use while loop and python time function to cause webhook handler to find the order 5 times over 5 seconds before giving up and creating the order.
* To handle a case where the user has already ordered the same item...
* Change models.py to contain original_bag and stripe_pid

```
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
```
* change admin.py fields to contain original_bag and stripe_pid fields and read only fields.

* change views.py to add those fields when the form is submitted.

* Add to checkout.html template:
```
<!-- Pass the client secret to the view so we can get the payment intent id -->
<input type="hidden" value="{{ client_secret }}" name="client_secret">
```

* In views.py save payment id and rest of shopping bag data:
```
order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
```

* Ensure webhook handler is using the pid and original_bag fields.
* import the models it now uses.
```
from .models import Order, OrderLineItem
from products.models import Product

import json
import time
```

## Updates to checkout.

* change order of fields in checkout.html
* change country fields to a dropdown box to prevent confusing users with unfriendly errors.
`pip3 install django-countries`
`pip3 freeze > requirements.txt`

* In models.py
`from django_countries.fields import CountryField`
Change to use select field:
`country = CountryField(blank_label='Country *', null=False, blank=False)`

```
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
```

* In static checkout_css grey out the select field if nothing is selected.
```
select, select option {
    color: #000000;
}

select:invalid, select option[value=""] {
    color: #aab7c4 !important;
}
```

## User Profile App

* Create an app called profile and add it to installed apps in boutique_ado -> settings.py -> intalled_apps

`python3 manage.py startapp profiles`


* In profiles -> models.py

- Create OneToOne relationship field. One to one will mean each user can only create one profile.
- Add defaults for phone number, country, post code etc.
- These are optional so null and blank can be set to true.
- Import django-countries to use select field for countries.
- Create string method to return the username
- Add a receiver for post save event. Each time a user is created, create a profile or save it if the user already exists.
- import save and receiver for the signal to work

* In checkout -> models.py
- `from profiles.models import UserProfile`
- Create a foreign key to it 

```
python3 manage.py makemigrations --dry-run
python3 manage.py makemigrations
python3 manage.py migrate --plan
python3 manage.py migrate
```

* Create views.py for profile app
* create url for this view.
* Add urls in project level file.
* Create templates and css file.

## Adjust Allauth to add top padding

* Login has it's own base template block. So modify allauth account/base template.
* Rename login.html content block to inner content.
* Change to {{form|crispy}} to render as a form not a paragraph
* Adjust styling
* Add home button
* Add inner_content to ALL other allauth templates in the folder.
* Update base.css with allauth formatting styles

NOTE:
Problem with previous accounts having no profile can be worked around by commenting out code in profiles -> models.py as follows and then logging in with that account:

```
   # if created:
    UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
  #  instance.userprofile.save()

```

* Update base.html with link to profile. `<a href="{% url 'profile' %}" class="dropdown-item">My Profile</a>`
* Update profile -> views.py to get profile and return it to the template.
* Update profile template to display ` {{ profile }}`

* Create forms.py in profile app by refactoring code from checkout app
* Add this form to views.py

* Update profile.html
* Update models.py
* Update profile.css and countryfield.js to style the country field correctly.

* Update Toasts `   {% if grand_total and not on_profile_page %}`

* Add Order History display code to profile.html
* Define order history in views.py
* Use checkout/checkout_success.hmtl as template
* Create the url `path('order_history/<order_number>', views.order_history, name='order_history'),`
* Update checkout success page to render a back button instead of latest deals button that would otherwise appear.

* Add order fields in checkout apps admin.py
* Update checkout views.py to pre fill checkout information from profile if user is authenticated. Otherwise render an empty form.

* Update webhook handler to use profile data in meta data key.

* Update webhook handler to send confirmation email when webhook from Stripe received.
* Create email .txt template files.
```
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
```
* Store customer email as variable
* Render template files as strings
* This creates email content:

```
    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )        

```
* Add default from email to settings.py

* This should now send confirmation email (printed to terminal)

## Store Owner Product Admin - allow django superusers to Add, Update and Delete products in the store

* Create forms.py in product app. Use friendly names to display forms.

```
from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
```

* Create a new view:

```
def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
```
 Import the form:

 `from .forms import ProductForm`

 Create the url
 `path('add/', views.add_product, name='add_product'),`


 Create add_products.html by refactoring code from checkout.html

Update form handler for add product:

```
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
```

* Update toast_success.html to handle no image.
* Add fix on shopping bag page too.

* Add link to Add Product page in base template and mobile top header.

### Editing Products

* Create edit_product.html page template.
* Send form to a new url - edit_product - and send product ID with it.
* Add a new view to render the template
* Add the url to urls.py `path('edit/<int:product_id>/', views.edit_product, name='edit_product'),`

```
def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
```

### Delete products

* Add url
* Add View

```
def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
```

* Update product view to redirect to product detail page:

```
def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
```

* Add delete buttons on products cards and on product detail pages.
```
{% if request.user.is_superuser %}
                                                <small class="ml-3">
                                                    <a href="{% url 'edit_product' product.id %}">Edit</a> | 
                                                    <a class="text-danger" href="{% url 'delete_product' product.id %}">Delete</a>
                                                </small>
                                            {% endif %}
```

### Secure view so that only super users can delete products

* In product app -> views.py:
* `from django.contrib.auth.decorators import login_required`
* Add `@login_required` above all views that are for admin only.
* Add similar functionality to the profile view.

* Add super user conditionality to product admin views:
```
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
```

### Tidy up image field form.

* django uses widgets to display, for example image input form elements.
* The clearable file input widget can be seen here: https://github.com/django/django/blob/master/django/forms/widgets.py
* The template we need to override can be found here: https://github.com/django/django/blob/master/django/forms/templates/django/forms/widgets/clearable_file_input.html

* In products -> widgets.py:
```
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
```
* In products/custom_widget_templates/custom_clearable_file_input.html:
```

{% if widget.is_initial %}
    <p>{{ widget.initial_text }}:</p>
    <a href="{{ widget.value.url }}">
        <img width="96" height="96" class="rounded shadow-sm" src="{{ widget.value.url }}">
    </a>
    {% if not widget.required %}
        <div class="custom-control custom-checkbox mt-2">
            <input class="custom-control-input" type="checkbox" name="{{ widget.checkbox_name }}" id="{{ widget.checkbox_id }}">
            <label class="custom-control-label text-danger" for="{{ widget.checkbox_id }}">{{ widget.clear_checkbox_label }}</label>
        </div>
    {% endif %}<br>
    {{ widget.input_text }}
{% endif %}
<span class="btn btn-black rounded-0 btn-file">
    Select Image <input id="new-image" type="{{ widget.type }}" name="{{ widget.name }}"{% include "django/forms/widgets/attrs.html" %}>
</span>
<strong><p class="text-danger" id="filename"></p></strong>
```
* in forms.py `from .widgets import CustomClearableFileInput`
* `image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)`

* Add /* Product Form */ styling to base.css

* In edit_product and add_product templates, only render a field as a crispy field if it's not our custom image widget:
```
{% for field in form %}
                        {% if field.name != 'image' %}
                            {{ field | as_crispy_field }}
                        {% else %}
                            {{ field }}
                        {% endif %}
                    {% endfor %}
```
* Add js to notify of what the new image will be:
```
{% block postloadjs %}
    {{ block.super }}
    <script type="text/javascript">
        $('#new-image').change(function() {
            var file = $('#new-image')[0].files[0];
            $('#filename').text(`Image will be set to: ${file.name}`);
        });
    </script>
{% endblock %}
```

# Deployment

* On Heroku Website https://dashboard.heroku.com/apps , New -> Create New App
* Choose App name and region.
* Use Resources - Addons - Heroku Postgres

* In gitpod:
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 freeze > requirements.txt

* In settings.py
- `import dj_database_url`

```
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}


DATABASES = {
    'default': dj_database_url.parse('postgress-url-goes-here')
}
```
* NB Get url from Heroku App settings tab / reveal config vars.

* Run migrations again (different database)

* `python3 manage.py showmigrations` Will show none exist

* `python3 manage.py migrate`

* To import product data, use fixtures:
- `python3 manage.py loaddata categories`
- `python3 manage.py loaddata products`
- NB categories must be created first as products depend on them.

* Create superuser account in the new database
- `python3 manage.py createsuperuser`


NB DO NOT COMMIT DATABASE URL TO VERSION CONTROL.

* Update settings.py to connect to a different database depending on if this is deployed or production version:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

* `pip3 install gunicorn`
* `pip3 freeze > requirements.txt`
* Create `Procfile` in root folder with the contents `web: gunicorn boutique_ado.wsgi:application`

* NB: Check folder for Procfile is correct

* In terminal:
- 'heroku login' or 'heroku login -i'
- `heroku config:set DISABLE_COLLECTSTATIC=1 --app jb-boutique-ado`

* In settings.py `ALLOWED_HOSTS = ['jb-boutique-ado.herokuapp.com', 'localhost']`
* NB must be wrapped in `` above.

* If the app was created on the heroku website, set the remote repo. `heroku git:remote -a jb-boutique-ado`

* to check: `git remote -v`

* The great moment! `git push heroku master`

* To deploy to github automatically:
- In Heroku web interface:
- Deploy -> Github
- Select repo and connect.
- Enable automatic deploys

* https://miniwebtool.com/django-secret-key-generator/ 
- Add this to Heroku -> Config Vars -> Add the secret_key
-  Update settings.py to contain it: `SECRET_KEY = os.environ.get('SECRET_KEY', '')`
- Set `DEBUG = 'DEVELOPMENT' in os.environ` in settings.py

## Creating an AWS Account

* Use AWS s3 to store static files.
- Create account at https://aws.amazon.com/
- Account type personal
- Go to AWS Management Console.
- Open s3
- Create new bucket
- In Set Permissions, uncheck Block All Public Access

* Bucket settings:
- Properties -> Static Website Hosting
- Use default values index.html and error.html
- Save
- Permissions:
- CORS Configuration:
```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
<AllowedOrigin>*</AllowedOrigin>
<AllowedMethod>GET</AllowedMethod>
<MaxAgeSeconds>3000</MaxAgeSeconds>
<AllowedHeader>Authorization</AllowedHeader>
</CORSRule>
</CORSConfiguration>
```
- Bucket Policy -> Policy Generator
- Policy Type: s3 Bucket Policy
- Principal: *
- Action: GetObject
- Copy ARN from the other tab eg `arn:aws:s3:::jb-boutique-ado`
- Add statement
- Generate Policy
- Copy Policy into other tab 'Bucket Policy'
- BEFORE SAVING: add /* into the resource key `"Resource": "arn:aws:s3:::jb-boutique-ado/*",`
- Access Control list -> Public Access -> Tick 'List Objects' and save.

* Use AWS service 'IAM' to connect to the bucket
- Go to IAM
- Click Access Management -> Groups
- Create New Group 'manage-boutique-ado'
- Click next twice (no policy to attach yet)
- Create Group
- Policies -> Create Policy
- Create Policy
- json tab -> Import managed policy
- Search for s3 and import the s3 Full Access Policy.
- From Bucket Policy in s3, get the arn and edit the json accordingly.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::jb-boutique-ado",
                "arn:aws:s3:::jb-boutique-ado/*"
                ]
        }
    ]
}
```
- Review Policy
- Add name and description. 
- Create
- Go to Groups -> Select the group -> Permissions tab -> Attach policy -> search and attach.

* users
- Add user
- Include static files access.
- Next: Permisssions
- Add user to group.
- Create user
- ESSENTIAL: Download .csv file.

* Connecting django to Amazon s3.

- `pip3 install boto3`
- `pip3 install django-storages`
- `pip3 freeze > requirements.txt`
- Add 'storages' to installed apps in settings.py

- in settings.py:

```
if 'USE_AWS' in os.environ:
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'jb-boutique-ado'
    AWS_S3_REGION_NAME = 'EU (London)'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

- Add these config vars in Heroku: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, USE_AWS.
- Delete Config Var for DISABLE_COLLECTSTATIC

- create custom_storages.py in main project folder. NB CHECK this location carefully. It should be at the same level as README.md
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

## Useful Documentation:
Django models, eg field types: https://docs.djangoproject.com/en/3.0/ref/models/fields/

Stripe: https://stripe.com/docs/payments/accept-a-payment#web-collect-card-details



