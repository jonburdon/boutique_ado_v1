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
    