from django.shortcuts import render, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.

def all_products(request):
    """  A view to show, sort and search queries. """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # set up variables for case insentive searching
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                # Now we have lower name in the sortkey variable, but we have preserved the sort term in the variable 'sort'

            # Use RELATIONS. Use double underscore syntax to allow connection to RELATED category
            if sortkey == 'category':
                sorkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # if direction is descending, add a - in from of the sortkey using string formatting which will reverse the order
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # order the products using the sortkey
            # implement the search using the oderby model method
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # We can look for the name field in the category model using __ because they are related with a foreign key
            products = products.filter(category__name__in=categories)
            # Capture categories so the currently selected categories can be displayed
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # Search query will check product name AND product description. The Pipe | is the OR statement and the i makes this insensitive
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # pass this query to the filter method to filter products
            products = products.filter(queries)


# Current sorting will be None_None if no sorting has happened.
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """  A view to show single product view. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)