from django.shortcuts import render, redirect
from form_app.forms import RegistrationForm
from form_app.models import User  # Assuming User model exists in models.py

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Form se data nikalna
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # User model ke instance ko banaye
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )

            # User ko save kare
            user.save()

            # Success page par redirect kare
            return redirect('success')
    else:
        form = RegistrationForm()
    return render(request, 'form_app/register.html', {'form': form})

def success(request):
    return render(request, 'form_app/success.html')