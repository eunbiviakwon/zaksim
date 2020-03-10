from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print('username:', username)
        print('password:', password)
        user = authenticate(request, username=username, password=password)
        print('user:', user)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('members:login')
    return render(request, 'members/login.html')
