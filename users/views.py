from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Show empty registration form.
        form = UserCreationForm()
    else:
        # Process the filled form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Authorize the user and redirect him to the main page.
            login(request, new_user)
            return redirect('smart_dogs:user_courses')
        
    # Show empty or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

