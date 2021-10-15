from django.shortcuts import render

# Create your views here.

def registration_login(request, template_name='registration/login.html'):
    return render(request, template_name)