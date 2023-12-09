from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from app.forms import LoginForm, PostForm, SignUpForm
from .models import Post, PostImage, Comment
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('login')        
        return render(request,'signup.html', {'form': form})
        

class Login(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('posts')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Неправильный логин или пароль')
        return render(request,'login.html',{'form': form})


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request,f'Ты вышли с сайта')
        return redirect('login')


class PostListView(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    template_name = "create-post.html"
    form_class = PostForm
    success_url = reverse_lazy('posts')

class PostDeleteView(DeleteView):
    model = Post
    template_name = "delete-post.html"
    success_url = reverse_lazy('posts')

class PostDetailView(DetailView):
    model = Post
    template_name = ".html"

    def get():
        pass

    def post():
        pass

class PostUpdateView(UpdateView):
    model = Post
    template_name = ".html"

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = ".html"





