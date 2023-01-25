from django.shortcuts import render

def user_login(request):
    return render(request, 'security/login.html')


def user_signup(request):
    return render(request, 'security/signup.html')
