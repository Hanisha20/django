from typing import Any
from django import http
from django.shortcuts import render, redirect , get_object_or_404
from django.views import View
from . forms import UserRegistrationForm , UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.mixins import LoginRequiredMixin
from home.models import Post
from django.contrib.auth import views as authViews
from django.urls import reverse_lazy
class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homeApp:home') 
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):

        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(username= cd['username'], password = cd['password1'] , email= cd['email'])
            messages.success(request, 'Successfully Registered' , 'success')
            return redirect('homeApp:home')
        return  render(request, self.template_name, {'form': form})
class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homeApp:home') 
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name , {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'u logged in successfully' , 'success')
                return redirect('homeApp:home')
            messages.error(request, 'username or password is incorrect' , 'warning')
        return render(request, self.template_name, {'form': form})

# class UserRegisterView2(View):
#     def get(self, request):
#         return render(request, 'account/register2.html')

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully' , 'success')
        return redirect('homeApp:home')
    
class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User,pk=user_id)
        posts = Post.objects.filter(user=user)
        return render(request, 'account/profile.html', {'user': user , 'posts': posts})
    
class UserResetPasswordView(authViews.PasswordResetView):
    template_name = 'account/passwordResetForm.html'
    success_url = reverse_lazy('accountApp:passwordResetDone') 
    email_template_name = 'account/passwordResetEmail.html'
class UserResetPasswordDoneView(authViews.PasswordResetDoneView):
    template_name = 'account/passwordResetDone.html'

class UserPasswordResetConfirmView(authViews.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('accountApp:password_reset_complete')
class UserPasswordResetCompleteView(authViews.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'