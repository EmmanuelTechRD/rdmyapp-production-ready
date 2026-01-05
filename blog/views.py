from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models as m
from . import forms as f

# Blog:

def post_view(request):
    
    posts = m.Post.objects.order_by('-published_date')
    return render(request, 'blog/posts.html', {'posts': posts,})

@login_required
def create_post_view(request):
    
    if request.method == 'POST':
        form = f.PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = get_user_model().objects.get(id=request.user.id)
            form.cleaned_data['author'] = user
            form.save()
            
            messages.success(request, f"Your post has been published.")
            return redirect('post_list')
        
        else:
            messages.error(request, f"There was an error creating the post.")
                    
    else:
        form = f.PostForm()
        
    return render(request, 'blog/create.html', {'form': form})

@login_required
def update_post_view(request, pk):
    
    if request.user.is_superuser:
        post = get_object_or_404(m.Post, id=pk)
    else:
        post = get_object_or_404(m.Post, id=pk, author=request.user)
    
    if request.method == 'POST':
        form = f.PostUpdateForm(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, f"Your post has been updated.")
            return redirect('post_list')
        
        else:
            messages.error(request, f"There was an error updating the post.")
                    
    else:
        form = f.PostUpdateForm(instance=post)
        
    return render(request, 'blog/create.html', {'form': form})

@login_required
def delete_post_view(request, pk):
    
    if request.user.is_superuser:
        post = get_object_or_404(m.Post, id=pk)
    else:
        post = get_object_or_404(m.Post, id=pk, author=request.user)
        
    post.delete()
    
    messages.success(request, f"Your post has been deleted.")
    
    return redirect('post_list')

# User:

def login_view(request):
    
    if request.method == 'POST':
        form = f.LoginForm(request.POST)
    
        if form.is_valid():
            
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome!')
                return redirect('post_list')
                
            else:
                messages.error(request, 'Invalid email or password.')
            
            
    else:
        form = f.LoginForm()
            
    return render(request, 'user/login.html', context={'form': form,})

@login_required
def logout_view(request):
    
    logout(request)
    
    messages.success(request, 'Goodbye!')
    
    return redirect('login')

def signup_view(request):
    
    if request.method == 'POST':
        form = f.SignUpForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            messages.success(request, 'Account created successfully!')
            
            return redirect('login')
                          
    else:
        form = f.SignUpForm()
        
    return render(request, 'user/signup.html', context={'form': form,})

# App:

def about_view(request):
    return render(request, 'app/about.html')

def license_view(request):
    return render(request, 'app/mit_license.html')