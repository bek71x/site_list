from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views import View

from users.forms import RegisterForm, ProfileEditForm, UserEditForm
from users.models import Profile


class UserCreateView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'user/register.html', {'form': form})

class UserLoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'user/login.html', {'form': login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, f"Siz akkauntingizga kirdingiz {user.username}!✅")
            return redirect("home")
        else:
            return render(request, 'user/login.html', {'form': login_form})

class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            messages.info(request, "Siz tizimdan chiqdingiz📤")
        return redirect("home")

class ProfileView(View):
    def get(self, request):
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        context = {
            'user': user,
            'profile': profile,
        }
        return render(request, 'user/profile.html', context)

class ProfileEditView(LoginRequiredMixin,View):
    def get(self, request):
        form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            'form': form,
            'profile_form': profile_form
        }
        return render(request, 'user/profile_edit.html', context)
    def post(self, request):
        form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('profile')