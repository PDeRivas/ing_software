from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    login,
    logout)

class LoginView(View):

    def get(self, requests):
        return render(
            requests,
            'home/login.html'
        )
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request,
                                username=username,
                                password=password)
            if user:
                login(request, user)
                return redirect('index')
        return redirect('login')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

@login_required(login_url='login')
def index_view(request):
    return render(
        request,
        'home/index.html'
    )
