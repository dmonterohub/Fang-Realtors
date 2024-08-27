from django.shortcuts import render, get_object_or_404
from .models import Listings, Contact

# Create your views here.

# Method to be called in each view to handle form requests
def contactform(request):
        if request.method == 'POST':
            # Extract data from the POST request
            firstname = request.POST['first name']
            lastname = request.POST['last name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['description']

            # Create a new Contact object and save it to the database
            newcontact = Contact(firstname=firstname, lastname=lastname, email=email, phone=phone, message=message)
            newcontact.save()

# Renders the 'Home' page
def home(request):
    contactform(request)
    return render(request, 'homepage/index.html')

# Renders the 'For Sale' page
def alllistings(request):
    contactform(request)
    listings = Listings.objects.all()
    return render(request, 'homepage\All-Listings.html', {'listings': listings})

# Renders the 'Featured Listings' page
def featuredlistings(request):
    contactform(request)
    listings = Listings.objects.all()
    flistings = Listings.objects.filter(featuredlistings__isnull=False)
    return render(request, 'homepage\Featured-Listings.html', {'listings': listings, 'flistings': flistings})

# Renders the 'Search Homes' page
def searchlistings(request):
    contactform(request)
    listings = Listings.objects.all()
    title_contains_query = request.GET.get('title_contains')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    proptype = request.GET.get('proptype')
    numbaths = request.GET.get('numbaths')
    numbeds = request.GET.get('numbeds')

    if title_contains_query != '' and title_contains_query is not None:
        listings = listings.filter(title__icontains=title_contains_query)
    if price_min != '' and price_min is not None:
        listings = listings.filter(price__gte=price_min)
    if price_max != '' and price_max is not None:
        listings = listings.filter(price__lt=price_max)
    if proptype != '' and proptype is not None and proptype != 'Property Type...':
        listings = listings.filter(propertytypeid=proptype)
    if numbaths != '' and numbaths is not None:
        listings = listings.filter(baths__gte=numbaths)
    if numbeds != '' and numbeds is not None:
        listings = listings.filter(beds__gte=numbeds)
    context = {
        'queryset':listings
    }

    #return render(request, 'homepage\Search-Listings.html', {'listings': listings})
    return render(request, 'homepage\Search-Listings.html', context)

# Renders the page for a unique listing when the listing is selected
def listingtemplate(request, listing_title):
    contactform(request)
    property_listing = get_object_or_404(Listings, title=listing_title)
    return render(request, 'homepage\listing-template.html', {'property_listing': property_listing})

#Renders the 'Contact' page
def contacts(request):
    contactform(request)
    return render(request, 'homepage\Contact.html')