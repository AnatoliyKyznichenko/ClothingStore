from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from user.forms import UserRegistrationForm, UserLoginForm
from user.models import CustomUser


class LoginUserView(View):
    template_name = 'user/autification_user.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('product:index'))
        return render(request, self.template_name, {'form': form})


class RegistrationView(View):
    template_name = 'user/registration.html'
    form_class = UserRegistrationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()  # Сохранение пользователя, но без записи в базу данных
            user.save()
            login(request, user)

            # Вместо перенаправления, отобразим сообщение на текущей странице
            message = 'Регистрация прошла успешно!'
            #return render(request, self.template_name, {'form': form, 'message': message})
            return HttpResponseRedirect(reverse('product:index'))
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('product:index')


class GoogleLoginView(View):
    def get_google(self, request):
        # Ваш код для аутентификации через Google
        # Возможно, вам понадобится использовать библиотеку python-social-auth
        return redirect('users:products_many')  # Замените 'home' на ваш URL после успешной аутентификации


class GithubLoginView(View):
    def get_git_hub(self, request):
        # Ваш код для аутентификации через GitHub
        # Возможно, вам понадобится использовать библиотеку python-social-auth
        return redirect('users:products_many')  # Замените 'home' на ваш URL после успешной аутентификации


class Authorized_User_Page(View):
    template_name = 'user/registration.html'

    def get(self, request):
        return render(request, self.template_name)
