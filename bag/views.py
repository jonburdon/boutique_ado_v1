from django.shortcuts import render, redirect,reverse, HttpResponse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity')) #convert to integer as the template will send this as a string
    redirect_url = request.POST.get('redirect_url') # Use the redirect variable given in the post data

    # If product size is in the product url, set the variable 'size' to this value
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Store the shopping bag data in the http request session. This will persist until user closes their browser
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys(): # Increment the quantity for this size if an item already exists with this id and this size
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity # Otherwise just update
        else: # Use a dictionary so that different item ids can be posted, and multiple sizes posted can be tracked.
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity #increment quantity if this item is already in the bag
        else:
            bag[item_id] = quantity # add or update

    request.session['bag'] = bag # override the variable in the session with the updated version
    return redirect(redirect_url)
    
def adjust_bag(request, item_id):
    """ Adjust a quantity or remove from shopping bag """
    quantity = int(request.POST.get('quantity')) #convert to integer as the template will send this as a string

    # If product size is in the product url, set the variable 'size' to this value
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Store the shopping bag data in the http request session. This will persist until user closes their browser
    bag = request.session.get('bag', {})

    # either update the product quantity or remove it
    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[items_id]['items_by_size']: #remove dictionary if product doesn't use sizes
                bag.pop(item_id)    
             
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
           bag.pop(item_id)

    request.session['bag'] = bag # override the variable in the session with the updated version
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """ Remove item from shopping bag """

    try:
        # If product size is in the product url, set the variable 'size' to this value
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        # Store the shopping bag data in the http request session. This will persist until user closes their browser
        bag = request.session.get('bag', {})

        # remove the size from the sizes dictionary for this product
        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[items_id]['items_by_size']: #remove dictionary if product doesn't use sizes
                bag.pop(item_id)
                
        else:
            bag.pop(item_id)

        request.session['bag'] = bag # override the variable in the session with the updated version
        return HttpResponse(status=200) # return successful http response
    except Exception as e:
        return HttpResponse(status=500)
    