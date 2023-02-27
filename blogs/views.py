
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import CreateClubForm, LogInForm, SignUpForm, UserForm
from .models import User
from .helpers import login_prohibited


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = form_class = UserForm
    template_name = "account_details.html"
    extra_context = {"nbar": "account"}

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, "Your profile updated successfully!"
        )
        return reverse_lazy("home")


class ChangePasswordView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = "change_password.html"
    success_url = reverse_lazy("home")
    extra_context = {"nbar": "password"}

    def get_success_url(self):
        messages.add_message(
            self.request, messages.SUCCESS, "Your password changed successfully!"
        )
        return reverse_lazy("home")


def home(request):
    if request.user.is_authenticated:
        return render(request, 'feed.html', {'user': request.user})
    return render(request, 'home.html', {'form': LogInForm()})

def about(request):
    return render(request, 'about.html')

@login_required
def profile(request, username):
    if User.objects.filter(username=username).exists():
        return render(
            request, 'profile.html', {'user': User.objects.get(username=username)}
        )
    raise Http404

@login_prohibited
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password_confirmation'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

@login_prohibited
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    return render(request, 'log_in.html', {'form': LogInForm()})



@login_required
def log_out(request):
    logout(request)
    return redirect('home')

@login_required
def create_club(request):
    if request.method == 'POST':
        form = CreateClubForm(request.POST)
        if form.is_valid():
            club = form.save()
            club.admins.add(request.user)
            club.members.add(request.user)
            return redirect('home') # should take you to the newly created club's page - not implemented yet

    form = CreateClubForm()
    return render(request, 'create_club.html', {'form': form})

