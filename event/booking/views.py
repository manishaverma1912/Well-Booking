from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # You can redirect to the same or another page
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form, 'user': request.user})

def login(request):
    return render(request, 'login.html')

# >>>>>>>
from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm  # You'll create this


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})


# this is for the booking an event 
from .models import Event
from .forms import EventForm

@login_required
def profile(request):
    user_events = Event.objects.filter(user=request.user).order_by('-date')
    return render(request, 'profile.html', {'events': user_events})

@login_required
def book_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('profile')
    else:
        form = EventForm()
    return render(request, 'book_event.html', {'form': form})


# update th event booked form

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm  # You'll need to create this form

def event_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_view', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_edit.html', {'form': form})

def event_cancel(request, pk):
    if request.method == 'POST':
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        messages.success(request, "Event has been successfully cancelled.")
        return redirect('profile')
    
    # If someone tries to GET this page, redirect them
    return redirect('profile', pk=pk)


from .forms import ContactForm
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Optional: create a thank-you page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def base(request):
    return render(request , 'base.html')
    