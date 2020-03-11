
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

User = get_user_model()


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
            return redirect('posts:post-list')
        else:
            return redirect('members:login')
    return render(request, 'members/login.html')


def signup_view(request):
    email = request.POST['email']
    username = request.POST['username']
    name = request.POST['name']
    password = request.POST['password']

    if User.objects.filter(username=username).exists():
        return HttpResponse('이미 사용중인 username입니다')
    if User.objects.filter(email=email).exists():
        return HttpResponse('이미 사용중인 email입니다')

    user = User.objects.create_user(
        password=password,
        username=username,
        email=email,
        name=name,
    )
    login(request, user)
    return redirect('posts:post-list')

def logout_view(request):
    logout(request)
    return redirect('members:login')