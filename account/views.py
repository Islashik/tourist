from distutils.log import Log
from django.shortcuts import render
from django.contrib.auth import logout
from .forms import UserRegisterForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import LoginForm
def sign_in(request):
    print(request)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Вы успешно вошли!")
                else:
                    return HttpResponse("Аккаунт неактивирован")
            else:
                return HttpResponse("Неправильные данные пользователя")
    else:
        form = LoginForm()
    return render(request, 'login.html', {"form":form})
def logout_user(request):
    logout(request)
    return HttpResponse("Вы успешно вышли!")


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'register.html',{"user_form":user_form})

