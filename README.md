
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

## Useful Documentation:
Django models, eg field types: https://docs.djangoproject.com/en/3.0/ref/models/fields/





