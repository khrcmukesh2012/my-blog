from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
	if request.user.is_superuser or request.user.is_staff:
		return HttpResponseRedirect('/admin/')

	page = Blog.objects.all().first()
	
	return render(request, 'home.html',{"home_page":page})

def aboutus(request):
	if request.user.is_superuser or request.user.is_staff:
		return HttpResponseRedirect('/admin/')

	page = CMSPages.objects.get(id=2)
	print(page.title)
	return render(request, 'aboutus.html',{"page":page})

def newsevent(request):
	if request.user.is_superuser or request.user.is_staff:
		return HttpResponseRedirect('/admin/')

	page = NewsEvent.objects.all()
	
	return render(request, 'newsevent.html',{"page":page})
def contactus(request):
	if request.user.is_superuser or request.user.is_staff:
		return HttpResponseRedirect('/admin/')
	form = ContactUsForm()
	if request.method=="POST":
		contact_form=ContactUsForm(data=request.POST)
		if contact_form.is_valid():
			contact_form.save()
	return render(request,"contactus.html",{"form":form})
def video(request):
	if request.user.is_superuser or request.user.is_staff:
		return HttpResponseRedirect('/admin/')
	video = Video.objects.all().order_by("-id")
	return render(request,"video.html",{"video":video})

def blog(request):
	if request.user.is_superuser or request.user.is_staff:
		return HttpResponseRedirect('/admin/')
	blog = Blog.objects.all().order_by("-id")
	return render(request,"blog.html",{"blog":blog})

def blog_read(request,id=None):
	if request.user.is_superuser or request.user.is_staff:
		return HttpResponseRedirect('/admin/')
	blog = Blog.objects.get(id=id)
	return render(request,"blog_details.html",{"blog":blog})
def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)


        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        
    # Render the template depending on the context.
    return render(request,'index.html',{'user_form': user_form,'registered': registered})


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
		

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:

            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                if request.user.is_authenticated:
                    messages.add_message(request, messages.INFO, 'You are logged in.".')
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponse("your are not logged in")
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))

            return render(request,'login.html', {"messages":"Invalid Login credentials"}, )

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
      
        return render(request,'login.html' )


def user_dashboard(request):

    
    return render(request,'dashboard.html',{"messages":message})



# Use the login_required() decorator to ensure only those logged in can access the view.

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/signup/')  