from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """  A view to display shopping bag. """
    return render(request, 'bag/bag.html')


