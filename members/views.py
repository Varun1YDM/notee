from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import note
from datetime import datetime



class LoginView(TemplateView):
    template_name = 'members/login.html'
    
    def post(self, request):
        username = request.POST.get('lusername')
        password = request.POST.get('lpassword')
        print()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("sucess")
            login(request, user)
            return redirect('user')
        else:
            messages.success(request,("Enter Valid Credentials"))
            return render(request, 'members/login.html', {})


class RegisterView(TemplateView):
    template_name = 'members/register.html'
    
    def post(self, request):
        username = request.POST.get('rusername')
        email = request.POST.get('remail')
        password = request.POST.get('rpassword')
        # confpassword = request.POST.get('confpassword')
        
        # if password != confpassword:
        #     messages.error(request, "Passwords do not match.")
        #     return render(request, self.template_name)

        try:
            User.objects.create_user(username=username, email=email, password=password)
            
            messages.success(request,("Registration is succesful"))
            return redirect('login')
        except IntegrityError:
            messages.success(request,("User already Exists"))
            return render(request, self.template_name)


def logout_view(request):
    logout(request)
    return redirect('home')
  
# -------------------------------------------------

class HomeView(TemplateView):
    template_name = 'members/home.html'

class NotesView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'members/user.html'
    
    def get_context_data(self):
        context = super().get_context_data()
        context["user"] = self.request.user.username
        context["symbol"] = self.request.user.username[:1]
        user = User.objects.get(username=self.request.user.username)
        context["notes"] = note.objects.filter(username=user)
        return context
    
    def post(self, request):
        title = request.POST.get('title')
        notes = request.POST.get('description')
        current_datetime = datetime.now()
        user = User.objects.get(username=request.user.username)
        note.objects.create(username=user, title=title, notes=notes, last_modified = current_datetime)
        return redirect('user')
    
class UpdateView(TemplateView):
    template_name = 'members/user.html'
    def post(self, request):
        title = request.POST.get('title')
        notes = request.POST.get('description')
        id = request.POST.get('uuid')
        current_datetime = datetime.now()
        note_data = note.objects.all().get(id=id)
        note_data.title = title 
        note_data.notes = notes
        note_data.last_modified = current_datetime
        note_data.save()
        return redirect('user')
    
class DeleteView(TemplateView):
    template_name = 'members/user.html'
    def post(self, request):
        id = request.POST.get('uuid')
        note_data = note.objects.all().get(id=id)
        note_data.delete()
        return redirect('user')